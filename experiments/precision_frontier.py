"""Precision-cost frontier for separating incompatible climate futures.

Copyright (C) 2026 Mohammad Amir Khusru Akhtar
Licensed under the Apache License, Version 2.0.

A pair of calibrated worlds is declared future-incompatible when their +100 y
surface temperatures differ by at least FUTURE_GAP. For each scalar diagnostic,
we compute the largest symmetric measurement error epsilon that still prevents
any such incompatible pair from being observationally confounded. We then use
span/(2 epsilon) as a dimensionless resolution burden: approximately the number
of resolvable bins required across that diagnostic's ensemble range. Lower is
cheaper under this explicit information-resolution cost.
"""
from experiments.calibrated_worlds import ensemble, interp

FUTURE_GAP = 0.50


def diagnostics():
    return {
        "historical_surface_120y": lambda w, h: interp(h, 120, 1),
        "historical_surface_150y": lambda w, h: interp(h, 150, 1),
        "historical_TOA_150y": lambda w, h: interp(h, 150, 3),
        "deep_temperature_now": lambda w, h: h[-1][2],
        "aerosol_ERF_now": lambda w, h: w.aerosol,
    }


def precision_frontier(future_gap=FUTURE_GAP):
    worlds = ensemble()
    future = [interp(f, 100, 1) for _, _, f in worlds]
    rows = []
    for name, fn in diagnostics().items():
        values = [fn(w, h) for w, h, _ in worlds]
        min_sep = float("inf")
        witness = None
        incompatible_pairs = 0
        for i in range(len(worlds)):
            for j in range(i + 1, len(worlds)):
                if abs(future[i] - future[j]) >= future_gap:
                    incompatible_pairs += 1
                    sep = abs(values[i] - values[j])
                    if sep < min_sep:
                        min_sep = sep
                        witness = (i, j)
        if witness is None:
            continue
        epsilon = min_sep / 2.0
        span = max(values) - min(values)
        burden = float("inf") if epsilon == 0 else span / (2.0 * epsilon)
        i, j = witness
        rows.append({
            "diagnostic": name,
            "epsilon": epsilon,
            "min_pair_separation": min_sep,
            "span": span,
            "resolution_burden": burden,
            "incompatible_pairs": incompatible_pairs,
            "future_gap_witness": abs(future[i] - future[j]),
        })
    rows.sort(key=lambda r: (r["resolution_burden"], -r["epsilon"]))
    return rows


def main():
    rows = precision_frontier()
    print("diagnostic,epsilon,min_pair_separation,span,resolution_burden,incompatible_pairs,witness_future_gap")
    for r in rows:
        print(f'{r["diagnostic"]},{r["epsilon"]:.9f},{r["min_pair_separation"]:.9f},'
              f'{r["span"]:.9f},{r["resolution_burden"]:.6f},'
              f'{r["incompatible_pairs"]},{r["future_gap_witness"]:.6f}')
    print(f'CHEAPEST_RESOLUTION_EXPERIMENT={rows[0]["diagnostic"]}')


if __name__ == "__main__":
    main()
