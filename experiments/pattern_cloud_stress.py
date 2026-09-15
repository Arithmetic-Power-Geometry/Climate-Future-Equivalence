"""Pattern-cloud stress test for cheapest incompatible-world experiment.

Copyright (C) 2026 Mohammad Amir Khusru Akhtar
Licensed under the Apache License, Version 2.0.

This deliberately simplified experiment adds two hidden dimensions to the calibrated
two-layer EBM: a discrete SST-pattern state and a cloud-response sensitivity. It asks
for the smallest NUMBER of scalar diagnostics whose joint values are non-identical
for every pair of calibrated worlds whose +100-year surface temperatures differ by
at least 0.50 K.

This is a structural falsification benchmark, not a calibrated Earth-system model.
"""
from itertools import combinations

import numpy as np

CS, CD, F2X, DT, HIST_YEARS = 8.0, 100.0, 3.7, 0.2, 170.0
FUTURE_GAP = 0.50


def simulate(ecs, gamma, aerosol, pattern, cloud_sensitivity):
    lam = F2X / ecs
    s = d = 0.0
    hist = []
    for i in range(int(HIST_YEARS / DT) + 1):
        t = i * DT
        ghg = 3.2 * t / HIST_YEARS
        ramp = max(0.0, (t - 100.0) / (HIST_YEARS - 100.0))
        forcing = ghg + aerosol * ramp + 0.15 * pattern * ramp
        lam_eff = lam - 0.15 * cloud_sensitivity * pattern * ramp
        nflux = forcing - lam_eff * s
        hist.append((t, s, d, nflux))
        ds = (forcing - lam_eff * s - gamma * (s - d)) / CS
        dd = gamma * (s - d) / CD
        s += DT * ds
        d += DT * dd

    future = []
    for i in range(int(100.0 / DT) + 1):
        t = i * DT
        # Stress-test assumption: the SST pattern evolves toward a common warm-pattern
        # endpoint, while worlds retain different cloud sensitivities.
        p_future = pattern + (1.0 - pattern) * (t / 100.0)
        lam_eff = lam - 0.35 * cloud_sensitivity * p_future
        forcing = 3.2
        nflux = forcing - lam_eff * s
        future.append((t, s, d, nflux))
        ds = (forcing - lam_eff * s - gamma * (s - d)) / CS
        dd = gamma * (s - d) / CD
        s += DT * ds
        d += DT * dd
    return hist, future


def ensemble():
    worlds = []
    for ecs in np.arange(2.0, 5.01, 0.5):
        for gamma in np.arange(0.3, 1.21, 0.3):
            for aerosol in np.arange(-1.8, -0.39, 0.4):
                for pattern in (-1.0, 0.0, 1.0):
                    for cloud_sensitivity in (0.5, 1.0, 1.5):
                        h, f = simulate(ecs, gamma, aerosol, pattern, cloud_sensitivity)
                        if abs(h[-1][1] - 1.20) <= 0.10 and abs(h[-1][3] - 0.70) <= 0.25:
                            worlds.append((ecs, gamma, aerosol, pattern, cloud_sensitivity, h, f))
    return worlds


def value(world, name):
    if name == "aerosol_ERF_now": return world[2]
    if name == "deep_temperature_now": return world[5][-1][2]
    if name == "SST_pattern_index": return world[3]
    if name == "cloud_pattern_sensitivity": return world[4]
    if name == "pattern_cloud_product": return world[3] * world[4]
    raise KeyError(name)


def future100(world):
    return world[6][-1][1]


def separates_all(worlds, subset, tol=1e-12):
    incompatible = 0
    min_joint_distance = float("inf")
    witness = None
    for i in range(len(worlds)):
        for j in range(i + 1, len(worlds)):
            if abs(future100(worlds[i]) - future100(worlds[j])) >= FUTURE_GAP:
                incompatible += 1
                # Dimensionless structural test: zero means exact confounding on all
                # selected diagnostics. Nonzero means the pair is distinguishable in
                # principle; no cross-unit precision ranking is claimed here.
                diffs = [abs(value(worlds[i], q) - value(worlds[j], q)) for q in subset]
                joint = max(diffs)
                if joint < min_joint_distance:
                    min_joint_distance = joint
                    witness = (i, j)
                if joint <= tol:
                    return False, incompatible, 0.0, (i, j)
    return True, incompatible, min_joint_distance, witness


def search():
    worlds = ensemble()
    diagnostics = ["aerosol_ERF_now", "deep_temperature_now", "SST_pattern_index",
                   "cloud_pattern_sensitivity", "pattern_cloud_product"]
    one_scalar = []
    for q in diagnostics:
        ok, _, md, _ = separates_all(worlds, (q,))
        one_scalar.append((q, ok, md))
    winners = []
    for k in range(1, len(diagnostics) + 1):
        for subset in combinations(diagnostics, k):
            ok, count, md, witness = separates_all(worlds, subset)
            if ok:
                winners.append((k, subset, md, count, witness))
        if winners:
            break
    return worlds, one_scalar, winners


def main():
    worlds, one_scalar, winners = search()
    print(f"calibrated_worlds={len(worlds)}")
    print("single_diagnostic,guarantees_all_incompatible_pairs,min_joint_distance")
    for q, ok, md in one_scalar:
        print(f"{q},{ok},{md:.12g}")
    print(f"MINIMUM_SCALAR_COUNT={winners[0][0]}")
    for k, subset, md, count, _ in winners:
        print(f"WINNER={'+'.join(subset)},count={k},min_joint_distance={md:.12g},incompatible_pairs={count}")


if __name__ == "__main__":
    main()
