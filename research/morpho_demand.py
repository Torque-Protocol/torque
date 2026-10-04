#!/usr/bin/env python3
"""Measured demand for USDG credit against stock tokens: every Morpho Blue market on Robinhood Chain that lends USDG
against a Robinhood Stock Token, read at one block. For each: the collateral, the liquidation threshold (LLTV), USDG
supplied, USDG borrowed and utilisation; plus the most a loop could reach at that threshold, 1 / (1 - LLTV).

Markets come from morpho_markets_2026-10-02.json (the CreateMarket scan by morpho_stock_markets.py). Values are read live
with batched eth_call. Writes morpho-demand.json and MORPHO_DEMAND.md next to this file.

That this borrowing is demand TORQUE would serve is an inference; what is measured is the borrowing.

  python3 research/morpho_demand.py      (RH_RPC_URL optional)
"""
import datetime as dt, json, os, time, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
RPC = os.environ.get("RH_RPC_URL", "https://rpc.mainnet.chain.robinhood.com")
USDG = "0x5fc5360D0400a0Fd4f2af552ADD042D716F1d168"
MORPHO = "0x9D53d5E3bd5E8d4Cbfa6DB1ca238AEA02E651010"
MARKET_SEL, PARAMS_SEL = "0x5c60e39a", "0x2c3c9157"  # market(bytes32), idToMarketParams(bytes32)


def rpc(calls):
    body = json.dumps([{"jsonrpc": "2.0", "id": i, "method": m, "params": p} for i, (m, p) in enumerate(calls)]).encode()
    for attempt in range(8):
        try:
            req = urllib.request.Request(RPC, body, {"Content-Type": "application/json", "User-Agent": "torque-morpho-demand"})
            out = sorted(json.load(urllib.request.urlopen(req, timeout=60)), key=lambda r: r["id"])
            if any("error" in r for r in out):
                raise RuntimeError(next(r["error"] for r in out if "error" in r))
            return [r["result"] for r in out]
        except Exception as e:  # the public RPC rate-limits: retry, then fail loudly rather than return partial data
            if attempt == 7:
                raise
            time.sleep(2 * (attempt + 1))


markets = json.load(open(os.path.join(HERE, "morpho_markets_2026-10-02.json")))
mk = [m for m in markets if "Robinhood Token" in (m.get("collName") or "") and m["loan"].lower() == USDG.lower()]
block = int(rpc([("eth_blockNumber", [])])[0], 16)
ts = int(rpc([("eth_getBlockByNumber", [hex(block), False])])[0]["timestamp"], 16)
words = lambda h: [int(h[2 + 64 * i: 2 + 64 * (i + 1)], 16) for i in range((len(h) - 2) // 64)]
rows = []
for i in range(0, len(mk), 25):
    chunk = mk[i: i + 25]
    calls = []
    for m in chunk:
        calls.append(("eth_call", [{"to": MORPHO, "data": MARKET_SEL + m["id"][2:]}, hex(block)]))
        calls.append(("eth_call", [{"to": MORPHO, "data": PARAMS_SEL + m["id"][2:]}, hex(block)]))
    res = rpc(calls)
    for j, m in enumerate(chunk):
        mkt, params = words(res[2 * j]), words(res[2 * j + 1])
        supplied, borrowed, lltv = mkt[0] / 1e6, mkt[2] / 1e6, params[4] / 1e18
        rows.append({"id": m["id"], "collateral": m["collSym"], "lltv": lltv, "supplied": supplied, "borrowed": borrowed,
                     "utilisation": borrowed / supplied if supplied else 0.0, "maxLoop": 1 / (1 - lltv) if lltv < 1 else None})
    time.sleep(0.3)

rows.sort(key=lambda r: -r["borrowed"])
tot_s, tot_b = sum(r["supplied"] for r in rows), sum(r["borrowed"] for r in rows)
active = [r for r in rows if r["supplied"] >= 1]
full = [r for r in active if r["utilisation"] >= 0.9]
when = dt.datetime.fromtimestamp(ts, dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
by_coll = {}
for r in rows:
    c = by_coll.setdefault(r["collateral"], {"supplied": 0.0, "borrowed": 0.0, "markets": 0})
    c["supplied"] += r["supplied"]; c["borrowed"] += r["borrowed"]; c["markets"] += 1
out = {"block": block, "time": when, "markets": len(rows), "supplied": tot_s, "borrowed": tot_b, "utilisation": tot_b / tot_s if tot_s else 0,
       "marketsWithSupply": len(active), "marketsAt90pctOrMore": len(full), "byCollateral": by_coll, "rows": rows}
json.dump(out, open(os.path.join(HERE, "morpho-demand.json"), "w"), indent=1)

f = lambda x: f"${x:,.0f}"
lines = [
    "# Demand, measured: USDG borrowed against stock tokens",
    "",
    f"Every Morpho Blue market on Robinhood Chain that lends USDG against a Robinhood Stock Token, read at block **{block:,}** ({when}) by "
    "[`research/morpho_demand.py`](https://github.com/Torque-Protocol/torque/blob/main/research/morpho_demand.py). The figures move with the markets; the block is the reference.",
    "",
    f"**{len(rows)} markets.** Lenders have supplied {f(tot_s)} of USDG; borrowers have taken {f(tot_b)}, **{tot_b / tot_s:.1%}** of it. "
    f"Of the {len(active)} markets with at least $1 supplied, {len(full)} are 90% or more borrowed.",
    "",
    "**What is measured** is borrowing: people posting stock tokens and taking USDG. **What is our inference** is that part of it is demand for "
    "leverage on stocks, which a knock-out with a hard floor would also serve. The last column is the most a loop can reach in that market, "
    "1 / (1 − LLTV), before any safety margin; TORQUE offers up to 5×.",
    "",
    "## By stock",
    "",
    "| Stock | Markets | USDG supplied | USDG borrowed | Borrowed |",
    "|---|---|---|---|---|",
]
for c, v in sorted(by_coll.items(), key=lambda kv: -kv[1]["borrowed"]):
    if v["supplied"] >= 1:
        lines.append(f"| {c} | {v['markets']} | {f(v['supplied'])} | {f(v['borrowed'])} | {v['borrowed'] / v['supplied']:.1%} |")
lines += ["", "## Every market with USDG supplied", "", "| Market | Stock | Liquidation threshold | USDG supplied | USDG borrowed | Borrowed | Loop at most |", "|---|---|---|---|---|---|---|"]
for r in active:
    lines.append(f"| `{r['id'][:10]}…` | {r['collateral']} | {r['lltv']:.1%} | {f(r['supplied'])} | {f(r['borrowed'])} | {r['utilisation']:.1%} | {r['maxLoop']:.2f}× |")
lines += ["", f"{len(rows) - len(active)} more markets exist with under $1 supplied. Full data, including every market id: "
          "[`research/morpho-demand.json`](https://github.com/Torque-Protocol/torque/blob/main/research/morpho-demand.json)."]
open(os.path.join(HERE, "MORPHO_DEMAND.md"), "w").write("\n".join(lines) + "\n")
print(json.dumps({k: v for k, v in out.items() if k not in ("rows", "byCollateral")}, indent=1))
