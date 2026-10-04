#!/usr/bin/env python3
"""Independent check of the landing page's Morpho-loop-vs-TORQUE calculator (components/torque/compare-math.ts).

Same rules, written separately: Morpho liquidates once debt/collateral > LLTV, the liquidator repays the debt and seizes
debt * LIF of collateral (LIF = min(1.15, 1/(0.3*LLTV + 0.7)), Morpho's documented formula); TORQUE knocks out at
1.05 x the worth-zero level, sells 0.2% below the print, repays the vault first and pays no bonus. A weekday crossing
executes at the threshold; a Monday gap through it executes at Monday's price. Interest is not modelled.
Prints a table; pass --json to emit it for the page's test.
"""
import json, sys

LLTV = 0.625
LIF = min(1.15, 1 / (0.3 * LLTV + 0.7))


def morpho(m, lev, week, gap):
    if lev >= 1 / (1 - LLTV) - 1e-9:
        return None
    coll_units, debt = m * lev, m * (lev - 1)
    liq_price = debt / (coll_units * LLTV)
    fri, mon = 1 + week, (1 + week) * (1 + gap)
    px = liq_price if fri <= liq_price else (mon if mon <= liq_price else None)
    if px is None:
        return {"back": coll_units * mon - debt, "bonus": 0.0, "ended": False}
    coll = coll_units * px
    seized = min(coll, debt * LIF)
    return {"back": coll - seized, "bonus": seized - min(coll, debt), "ended": True}


def torque(m, lev, week, gap):
    fee = m * lev * 0.001
    equity = m - fee
    notional = equity * lev
    borrow = notional - equity
    ko = borrow / notional * 1.05
    fri, mon = 1 + week, (1 + week) * (1 + gap)
    px = ko if fri <= ko else (mon if mon <= ko else None)
    if px is None:
        return {"back": notional * mon - borrow, "bonus": 0.0, "ended": False}
    return {"back": max(0.0, notional * px * 0.998 - borrow), "bonus": 0.0, "ended": True}


rows = []
for lev in (2.0, 2.5, 3.0, 5.0):
    for week, gap in ((0.0, 0.0), (-0.03, -0.08), (-0.10, 0.0), (0.0, -0.25), (0.05, 0.05)):
        rows.append({"lev": lev, "week": week, "gap": gap, "morpho": morpho(100, lev, week, gap), "torque": torque(100, lev, week, gap)})
if "--json" in sys.argv:
    print(json.dumps(rows))
else:
    print(f"LIF {LIF:.4f} (bonus {LIF - 1:.1%}), loop max {1 / (1 - LLTV):.2f}x")
    for r in rows:
        mo = r["morpho"]
        ms = "n/a" if mo is None else "back {:.2f} bonus {:.2f}".format(mo["back"], mo["bonus"])
        print("{}x week {:+.0%} gap {:+.0%} | Morpho: {} | TORQUE: back {:.2f}".format(r["lev"], r["week"], r["gap"], ms, r["torque"]["back"]))
