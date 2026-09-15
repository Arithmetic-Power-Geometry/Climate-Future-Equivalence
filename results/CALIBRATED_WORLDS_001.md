# Calibrated Worlds Experiment 001

Copyright (C) 2026 Mohammad Amir Khusru Akhtar

## Question
Find the cheapest experiment for which shared coarse historical climate knowledge leaves mutually incompatible possible worlds.

## Construction
A grid of two-layer energy-balance worlds varies equilibrium climate sensitivity (ECS), ocean exchange, and idealized present aerosol forcing. Worlds are retained only if they simultaneously match the same coarse present-day constraints used by this benchmark: surface warming 1.20 +/- 0.08 K and TOA imbalance 0.70 +/- 0.20 W m^-2.

This is deliberately a structural-identifiability benchmark, not a calibrated assessment of the real climate.

## Result
194 worlds survive calibration. Their ECS values span 2.0--3.7 K and their idealized aerosol ERF spans -1.4-- -0.4 W m^-2. Under the same future forcing (3.2 W m^-2, aerosol removed), the ensemble produces surface temperatures spanning approximately 1.432--2.205 K at +50 years and 1.518--2.430 K at +100 years. Thus coarse historical agreement does not force future agreement in this model class.

Candidate one-scalar diagnostics were assigned equal dimensional cost = 1 and normalized by explicit benchmark observation scales. The ranking was:

1. deep_temperature_now: normalized separation 18.4733; raw span 0.36947 K
2. historical_surface_120y: 6.2224; raw span 0.31112 K
3. aerosol_ERF_now: 5.0000; raw span 1.0 W m^-2
4. historical_surface_150y: 4.3259; raw span 0.21629 K
5. historical_TOA_150y: 1.2786; raw span 0.19179 W m^-2

## Cheapest experiment under the current cost definition
All candidates cost one scalar measurement, so the maximum-separation unit-cost diagnostic is **deep_temperature_now**.

This does NOT establish that deep-ocean temperature is cheapest in monetary, logistical, or real-world observational terms. The current cost is deliberately only measurement dimensionality. The next benchmark must replace unit cost with empirical observation cost/availability and use real historical datasets or established uncertainty distributions.

## Interpretation
The important result is not the winning diagnostic itself. It is that 194 mutually incompatible parameter worlds survive the same coarse knowledge and later diverge strongly. A single additional observable can have radically different power to collapse this equivalence class. This creates a concrete experiment-selection problem for Climate Future Equivalence.
