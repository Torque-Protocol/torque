# Demand, measured: USDG borrowed against stock tokens

Every Morpho Blue market on Robinhood Chain that lends USDG against a Robinhood Stock Token, read at block **79,510,989** (2026-10-04 00:28 UTC) by [`research/morpho_demand.py`](https://github.com/Torque-Protocol/torque/blob/main/research/morpho_demand.py). The figures move with the markets; the block is the reference.

**167 markets.** Lenders have supplied $1,507,781 of USDG; borrowers have taken $1,456,850, **96.6%** of it. Of the 63 markets with at least $1 supplied, 10 are 90% or more borrowed.

**What is measured** is borrowing: people posting stock tokens and taking USDG. **What is our inference** is that part of it is demand for leverage on stocks, which a knock-out with a hard floor would also serve. The last column is the most a loop can reach in that market, 1 / (1 − LLTV), before any safety margin; TORQUE offers up to 5×.

## By stock

| Stock | Markets | USDG supplied | USDG borrowed | Borrowed |
|---|---|---|---|---|
| NVDA | 15 | $630,265 | $614,208 | 97.5% |
| SPCX | 7 | $446,258 | $436,240 | 97.8% |
| GOOGL | 12 | $211,822 | $204,561 | 96.6% |
| AAPL | 15 | $197,264 | $197,215 | 100.0% |
| SPY | 11 | $11,262 | $4,343 | 38.6% |
| COIN | 2 | $113 | $71 | 62.9% |
| MSTR | 2 | $100 | $66 | 66.0% |
| CRCL | 3 | $100 | $45 | 45.0% |
| TTWO | 1 | $100 | $40 | 40.0% |
| PLTR | 2 | $33 | $30 | 90.9% |
| TSLA | 12 | $6,576 | $13 | 0.2% |
| INTC | 3 | $101 | $5 | 5.4% |
| MSFT | 5 | $32 | $5 | 15.8% |
| RDDT | 2 | $110 | $4 | 3.3% |
| SNDK | 3 | $101 | $4 | 3.5% |
| USO | 3 | $3 | $0 | 0.0% |
| SGOV | 4 | $111 | $0 | 0.0% |
| QQQ | 6 | $10 | $0 | 0.0% |
| SLV | 3 | $103 | $0 | 0.0% |
| GME | 3 | $103 | $0 | 0.0% |
| USAR | 2 | $125 | $0 | 0.0% |
| META | 3 | $101 | $0 | 0.0% |
| AMD | 3 | $101 | $0 | 0.0% |
| MU | 3 | $101 | $0 | 0.0% |
| CRWV | 2 | $125 | $0 | 0.0% |
| ORCL | 2 | $100 | $0 | 0.0% |
| TSM | 4 | $100 | $0 | 0.0% |
| ASML | 2 | $100 | $0 | 0.0% |
| BABA | 2 | $111 | $0 | 0.0% |
| DELL | 3 | $103 | $0 | 0.0% |
| IONQ | 1 | $100 | $0 | 0.0% |
| RGTI | 2 | $110 | $0 | 0.0% |
| RKLB | 1 | $100 | $0 | 0.0% |
| NBIS | 1 | $125 | $0 | 0.0% |
| CLSK | 1 | $100 | $0 | 0.0% |
| EWY | 2 | $100 | $0 | 0.0% |
| GLD | 1 | $111 | $0 | 0.0% |
| COST | 2 | $103 | $0 | 0.0% |
| DJT | 1 | $103 | $0 | 0.0% |
| NFLX | 2 | $100 | $0 | 0.0% |
| RBLX | 1 | $100 | $0 | 0.0% |
| MRNA | 1 | $100 | $0 | 0.0% |
| RIVN | 1 | $100 | $0 | 0.0% |
| HIMS | 2 | $100 | $0 | 0.0% |
| AMC | 1 | $100 | $0 | 0.0% |
| LLY | 1 | $100 | $0 | 0.0% |
| LULU | 1 | $125 | $0 | 0.0% |
| IBM | 1 | $94 | $0 | 0.0% |
| F | 1 | $281 | $0 | 0.0% |

## Every market with USDG supplied

| Market | Stock | Liquidation threshold | USDG supplied | USDG borrowed | Borrowed | Loop at most |
|---|---|---|---|---|---|---|
| `0x8b16891f…` | NVDA | 62.5% | $623,584 | $614,176 | 98.5% | 2.67× |
| `0x9b4b47cd…` | SPCX | 62.5% | $446,156 | $436,236 | 97.8% | 2.67× |
| `0x7fa81b10…` | GOOGL | 62.5% | $211,811 | $204,560 | 96.6% | 2.67× |
| `0xdeb4782d…` | AAPL | 62.5% | $197,238 | $197,214 | 100.0% | 2.67× |
| `0x50bc39b5…` | SPY | 62.5% | $11,229 | $4,343 | 38.7% | 2.67× |
| `0x508b47fb…` | COIN | 62.5% | $110 | $68 | 61.8% | 2.67× |
| `0x01baec96…` | MSTR | 62.5% | $100 | $66 | 66.0% | 2.67× |
| `0xf0959f62…` | CRCL | 62.5% | $100 | $45 | 45.0% | 2.67× |
| `0xe6284cf1…` | TTWO | 38.5% | $100 | $40 | 40.0% | 1.63× |
| `0x66306c08…` | NVDA | 62.5% | $6,579 | $31 | 0.5% | 2.67× |
| `0xb5ba72c0…` | PLTR | 62.5% | $33 | $30 | 90.9% | 2.67× |
| `0xf4dff250…` | TSLA | 77.0% | $15 | $12 | 79.2% | 4.35× |
| `0xda558463…` | INTC | 62.5% | $101 | $5 | 5.4% | 2.67× |
| `0x2e1859aa…` | MSFT | 62.5% | $30 | $5 | 16.9% | 2.67× |
| `0x298e8ff9…` | RDDT | 38.5% | $110 | $4 | 3.3% | 1.63× |
| `0x74fece47…` | SNDK | 62.5% | $101 | $4 | 3.5% | 2.67× |
| `0x3ebd43d9…` | COIN | 38.5% | $3 | $3 | 100.0% | 1.63× |
| `0x597227ca…` | SPCX | 38.5% | $101 | $3 | 3.1% | 1.63× |
| `0x95312f02…` | NVDA | 62.5% | $2 | $1 | 45.5% | 2.67× |
| `0x10151e2a…` | SPCX | 62.5% | $1 | $1 | 90.9% | 2.67× |
| `0x947ae981…` | AAPL | 62.5% | $1 | $1 | 90.9% | 2.67× |
| `0xe29c7d37…` | TSLA | 62.5% | $1 | $1 | 90.9% | 2.67× |
| `0x7408b08b…` | GOOGL | 77.0% | $1 | $1 | 90.9% | 4.35× |
| `0x077088f9…` | SPY | 77.0% | $33 | $0 | 0.0% | 4.35× |
| `0x6b8a1f62…` | USO | 62.5% | $3 | $0 | 0.0% | 2.67× |
| `0x4edbd2f2…` | SLV | 62.5% | $103 | $0 | 0.0% | 2.67× |
| `0x7e6ebfdc…` | GOOGL | 62.5% | $10 | $0 | 0.0% | 2.67× |
| `0x315b99ab…` | QQQ | 62.5% | $10 | $0 | 0.0% | 2.67× |
| `0x4979137c…` | GME | 62.5% | $103 | $0 | 0.0% | 2.67× |
| `0xafc86936…` | MSFT | 62.5% | $2 | $0 | 0.0% | 2.67× |
| `0x2ab6a14c…` | USAR | 38.5% | $125 | $0 | 0.0% | 1.63× |
| `0xb41b34c5…` | TSLA | 62.5% | $6,560 | $0 | 0.0% | 2.67× |
| `0x69400cfe…` | META | 62.5% | $101 | $0 | 0.0% | 2.67× |
| `0x4d207583…` | AMD | 62.5% | $101 | $0 | 0.0% | 2.67× |
| `0x9df4f54a…` | MU | 62.5% | $101 | $0 | 0.0% | 2.67× |
| `0xf6f3dbe0…` | SGOV | 86.0% | $111 | $0 | 0.0% | 7.14× |
| `0xee04847a…` | ORCL | 62.5% | $100 | $0 | 0.0% | 2.67× |
| `0x243ac165…` | TSM | 62.5% | $100 | $0 | 0.0% | 2.67× |
| `0xbe881499…` | ASML | 62.5% | $100 | $0 | 0.0% | 2.67× |
| `0xdd578ca5…` | BABA | 62.5% | $111 | $0 | 0.0% | 2.67× |
| `0xd8b502d5…` | DELL | 62.5% | $103 | $0 | 0.0% | 2.67× |
| `0xc85eb4a6…` | IONQ | 62.5% | $100 | $0 | 0.0% | 2.67× |
| `0x003390b0…` | RGTI | 62.5% | $110 | $0 | 0.0% | 2.67× |
| `0x30a2a5f1…` | AAPL | 62.5% | $25 | $0 | 0.0% | 2.67× |
| `0x14973a16…` | RKLB | 62.5% | $100 | $0 | 0.0% | 2.67× |
| `0xf049167e…` | NBIS | 62.5% | $125 | $0 | 0.0% | 2.67× |
| `0x8114b65d…` | CLSK | 62.5% | $100 | $0 | 0.0% | 2.67× |
| `0x96d3d5f9…` | CRWV | 62.5% | $125 | $0 | 0.0% | 2.67× |
| `0x1b3555f7…` | EWY | 62.5% | $100 | $0 | 0.0% | 2.67× |
| `0x6c12c025…` | GLD | 38.5% | $111 | $0 | 0.0% | 1.63× |
| `0xb33399a6…` | COST | 38.5% | $103 | $0 | 0.0% | 1.63× |
| `0x3be7fe1b…` | DJT | 38.5% | $103 | $0 | 0.0% | 1.63× |
| `0x0066bc47…` | NFLX | 38.5% | $100 | $0 | 0.0% | 1.63× |
| `0x8338aed3…` | RBLX | 38.5% | $100 | $0 | 0.0% | 1.63× |
| `0xe8d9b45c…` | MRNA | 38.5% | $100 | $0 | 0.0% | 1.63× |
| `0x46eea143…` | RIVN | 38.5% | $100 | $0 | 0.0% | 1.63× |
| `0xbe3a5355…` | NVDA | 38.5% | $100 | $0 | 0.0% | 1.63× |
| `0x43c51f6f…` | HIMS | 38.5% | $100 | $0 | 0.0% | 1.63× |
| `0x8c170f5c…` | AMC | 38.5% | $100 | $0 | 0.0% | 1.63× |
| `0x0f18d4fd…` | LLY | 38.5% | $100 | $0 | 0.0% | 1.63× |
| `0x7d4313cf…` | LULU | 38.5% | $125 | $0 | 0.0% | 1.63× |
| `0xa85928d7…` | IBM | 38.5% | $94 | $0 | 0.0% | 1.63× |
| `0x9d61e320…` | F | 38.5% | $281 | $0 | 0.0% | 1.63× |

104 more markets exist with under $1 supplied. Full data, including every market id: [`research/morpho-demand.json`](https://github.com/Torque-Protocol/torque/blob/main/research/morpho-demand.json).
