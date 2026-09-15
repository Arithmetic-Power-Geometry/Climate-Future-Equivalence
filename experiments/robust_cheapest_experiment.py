"""Robust uncertainty-aware future-incompatibility experiment.

Copyright (C) 2026 Mohammad Amir Khusru Akhtar
Licensed under the Apache License, Version 2.0.

This extends the exact zero-noise benchmark.  A diagnostic distinguishes a pair only
when its predicted difference exceeds a stated two-sided uncertainty tolerance.
The uncertainty values below are deliberately stress-test scales, not claims about
instrument specifications or present observational uncertainty.  The purpose is to
ask whether the exact two-diagnostic result survives finite uncertainty.
"""
from itertools import combinations
from experiments.pattern_cloud_stress import ensemble, future100, value, FUTURE_GAP

DIAGNOSTICS = (
    "aerosol_ERF_now",
    "deep_temperature_now",
    "SST_pattern_index",
    "cloud_pattern_sensitivity",
    "pattern_cloud_product",
)

# Stress-test half-widths in each diagnostic's native units.  A pair is robustly
# distinguished if at least one selected diagnostic differs by > 2*half_width.
HALF_WIDTH = {
    "aerosol_ERF_now": 0.20,
    "deep_temperature_now": 0.002,
    "SST_pattern_index": 0.25,
    "cloud_pattern_sensitivity": 0.20,
    "pattern_cloud_product": 0.25,
}


def incompatible_pairs(worlds):
    return [(i, j) for i in range(len(worlds)) for j in range(i + 1, len(worlds))
            if abs(future100(worlds[i]) - future100(worlds[j])) >= FUTURE_GAP]


def robustly_separates(worlds, pair, subset, scale=1.0):
    i, j = pair
    return any(abs(value(worlds[i], q) - value(worlds[j], q)) >
               2.0 * scale * HALF_WIDTH[q] for q in subset)


def exact_robust_minimum(scale=1.0):
    worlds = ensemble()
    pairs = incompatible_pairs(worlds)
    for k in range(1, len(DIAGNOSTICS) + 1):
        winners = []
        for subset in combinations(DIAGNOSTICS, k):
            unresolved = [p for p in pairs if not robustly_separates(worlds, p, subset, scale)]
            if not unresolved:
                winners.append(subset)
        if winners:
            return worlds, pairs, k, winners
    return worlds, pairs, None, []


def robustness_frontier(scales=(0.0, 0.25, 0.5, 1.0, 2.0)):
    rows = []
    for scale in scales:
        worlds, pairs, k, winners = exact_robust_minimum(scale)
        rows.append((scale, len(worlds), len(pairs), k, winners))
    return rows


def main():
    print("scale,worlds,incompatible_pairs,minimum_count,winner")
    for scale, nw, npairs, k, winners in robustness_frontier():
        winner = "+".join(winners[0]) if winners else "NONE"
        print(f"{scale},{nw},{npairs},{k if k is not None else 'INF'},{winner}")


if __name__ == "__main__":
    main()
