# Results

Copyright (C) 2026 Mohammad Amir Khusru Akhtar

## Experiment 001 — Cheapest separating perturbation in a two-layer climate model

### Objective
Find the minimum-cost bounded forcing pulse whose predicted response is detectably different between two mutually incompatible climate worlds that differ in equilibrium climate sensitivity and ocean heat uptake.

### Worlds
- World HSA: ECS = 4.5 K; stronger ocean exchange = 0.70 W m^-2 K^-1.
- World LSW: ECS = 2.2 K; weaker ocean exchange = 0.35 W m^-2 K^-1.

These are deliberately simplified diagnostic worlds. They are not asserted to be calibrated reconstructions of the real climate system.

### Experiment family
Square radiative-forcing pulses with amplitudes

0.05, 0.10, 0.20, 0.50, 1.00 W m^-2

and durations

0.25, 0.50, 1, 2, 5 years.

Cost is integrated absolute forcing:

c = |A| * duration  [W yr m^-2].

### Detection rule
Responses are sampled at 0.5, 1, 2, 5, 10, 20, and 30 years. A dimensionless detection score combines the maximum surface-temperature separation and deep-layer-temperature separation, normalized by provisional scales of 0.01 K and 0.005 K respectively. Score >= 1 is considered detectable for this benchmark.

### Result
The smallest tested cost reaching the threshold is

c* = 1.0 W yr m^-2.

Three tested pulses share that integrated cost:

- 1.0 W m^-2 for 1 year — score ~1.455; max surface gap ~0.01362 K; max deep gap ~0.00255 K.
- 0.5 W m^-2 for 2 years — score ~1.430.
- 0.2 W m^-2 for 5 years — score ~1.303.

Under a secondary objective of minimizing duration among minimum-cost experiments, the selected benchmark is therefore:

**1.0 W m^-2 for 1 year.**

### Interpretation
This proves only a computational statement about the configured linear two-layer model and candidate grid: compensating climate worlds can be separated more efficiently by a targeted transient-response measurement than by treating their common historical fit as equivalence.

It does **not** establish that a 1 W m^-2 real-world intervention should be performed. The forcing pulse is a mathematical probe. Real experiments must respect safety, ethics, feasibility, spatial structure, natural variability, measurement uncertainty, and known climate physics.

### Next falsification targets
1. Construct worlds that are explicitly calibrated to the same historical GMST and ocean-heat observations.
2. Add aerosol forcing as a third uncertain mechanism.
3. Replace arbitrary detection scales with covariance-aware observational likelihoods.
4. Search passive/natural experiments (volcanic forcing, aerosol changes, seasonal/ENSO responses) before considering artificial perturbations.
5. Compare value-of-information per cost across surface temperature, TOA radiation, ocean heat content, spatial warming patterns, and cloud/aerosol observations.
6. Test whether the optimal experiment remains optimal in nonlinear and state-dependent models.
7. Seek counterexamples where every low-cost finite-horizon experiment fails to separate long-horizon-divergent worlds.
