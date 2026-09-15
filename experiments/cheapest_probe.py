"""Cheapest separating experiment for Climate Future Equivalence.

Copyright (C) 2026 Mohammad Amir Khusru Akhtar
Licensed under the Apache License, Version 2.0.

This first benchmark is intentionally simple and falsification-oriented.
It searches bounded radiative-forcing pulses in a two-layer energy-balance
model for the minimum integrated forcing cost that separates two climate
worlds which differ in equilibrium climate sensitivity and ocean heat uptake.
"""

from __future__ import annotations

from dataclasses import dataclass
import math


@dataclass(frozen=True)
class World:
    name: str
    C_surface: float
    C_deep: float
    feedback_lambda: float
    ocean_exchange: float


HIGH_SENSITIVITY = World(
    name="high_sensitivity_strong_uptake",
    C_surface=8.0,
    C_deep=100.0,
    feedback_lambda=3.7 / 4.5,
    ocean_exchange=0.70,
)

LOW_SENSITIVITY = World(
    name="low_sensitivity_weak_uptake",
    C_surface=8.0,
    C_deep=100.0,
    feedback_lambda=3.7 / 2.2,
    ocean_exchange=0.35,
)


def simulate(world: World, amplitude: float, duration: float, horizon: float = 30.0, dt: float = 0.05):
    """Euler-integrate a two-layer EBM under a square forcing pulse."""
    n = int(horizon / dt) + 1
    t = 0.0
    surface = 0.0
    deep = 0.0
    series = [(t, surface, deep)]

    for _ in range(n - 1):
        forcing = amplitude if t < duration else 0.0
        ds = (
            forcing
            - world.feedback_lambda * surface
            - world.ocean_exchange * (surface - deep)
        ) / world.C_surface
        dd = world.ocean_exchange * (surface - deep) / world.C_deep
        surface += dt * ds
        deep += dt * dd
        t += dt
        series.append((t, surface, deep))
    return series


def nearest(series, year: float):
    return min(series, key=lambda row: abs(row[0] - year))


def response(world: World, amplitude: float, duration: float):
    series = simulate(world, amplitude, duration)
    years = (0.5, 1.0, 2.0, 5.0, 10.0, 20.0, 30.0)
    return [nearest(series, y) for y in years]


def distinguishability(amplitude: float, duration: float):
    """Dimensionless separation using configurable observational scales.

    Current benchmark scales:
      * 0.01 K for surface-temperature response
      * 0.005 K for the deep-layer temperature proxy

    A score >= 1 is treated as detectable in this toy benchmark.
    """
    a = response(HIGH_SENSITIVITY, amplitude, duration)
    b = response(LOW_SENSITIVITY, amplitude, duration)

    max_surface = max(abs(x[1] - y[1]) for x, y in zip(a, b))
    max_deep = max(abs(x[2] - y[2]) for x, y in zip(a, b))
    score = math.sqrt((max_surface / 0.01) ** 2 + (max_deep / 0.005) ** 2)
    return max_surface, max_deep, score


def main():
    amplitudes = (0.05, 0.10, 0.20, 0.50, 1.00)
    durations = (0.25, 0.50, 1.00, 2.00, 5.00)

    candidates = []
    for amplitude in amplitudes:
        for duration in durations:
            surface, deep, score = distinguishability(amplitude, duration)
            cost = abs(amplitude) * duration
            candidates.append(
                {
                    "amplitude": amplitude,
                    "duration": duration,
                    "cost": cost,
                    "surface_gap": surface,
                    "deep_gap": deep,
                    "score": score,
                }
            )

    candidates.sort(key=lambda r: (r["cost"], -r["score"]))
    feasible = [r for r in candidates if r["score"] >= 1.0]

    print("amplitude,duration,cost,max_surface_gap,max_deep_gap,detectability")
    for r in candidates:
        print(
            f'{r["amplitude"]:.2f},{r["duration"]:.2f},{r["cost"]:.4f},'
            f'{r["surface_gap"]:.6f},{r["deep_gap"]:.6f},{r["score"]:.6f}'
        )

    if not feasible:
        raise SystemExit("No candidate reached the detectability threshold.")

    best = feasible[0]
    print("\nCHEAPEST_DETECTABLE_EXPERIMENT")
    for key, value in best.items():
        print(f"{key}={value}")


if __name__ == "__main__":
    main()
