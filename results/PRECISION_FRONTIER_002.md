# Precision Frontier Experiment 002

Copyright (C) 2026 Mohammad Amir Khusru Akhtar

## Question
Among one-scalar passive diagnostics, what is the cheapest measurement precision that guarantees separation of every pair of calibrated worlds whose +100-year surface futures differ by at least 0.50 K?

## Cost definition
For diagnostic q, let delta_q be the smallest diagnostic separation among all world pairs with |T100_i-T100_j| >= 0.50 K. A symmetric measurement error epsilon_q < delta_q/2 guarantees that no such incompatible pair can be confused by overlapping error intervals. Define the information-resolution burden

    B_q = span(q) / (2 epsilon_q).

Lower B means fewer resolvable bins are needed across the ensemble range, hence lower precision burden. This is not a monetary or logistical cost.

## Result on the 194-world calibrated benchmark

| diagnostic | maximum symmetric error epsilon | ensemble span | resolution burden B |
|---|---:|---:|---:|
| aerosol_ERF_now | 0.200000 W m^-2 | 1.000000 W m^-2 | 2.500 |
| historical_surface_120y | 0.039230 K | 0.311120 K | 3.966 |
| historical_surface_150y | 0.000620 K | 0.216294 K | 174.37 |
| deep_temperature_now | 0.000544 K | 0.369465 K | 339.67 |
| historical_TOA_150y | 0.00000317 W m^-2 | 0.191789 W m^-2 | ~30209 |

The exact script output is authoritative.

## Cheapest experiment under this stronger definition

**Present aerosol effective radiative forcing is the cheapest scalar diagnostic under information-resolution burden.** It needs approximately +/-0.20 W m^-2 precision in this discrete ensemble to separate every pair differing by at least 0.50 K at +100 years.

This reverses Experiment 001's winner (deep-ocean temperature). Deep temperature had the largest overall span normalized by an illustrative scale, but a worst-case pair of strongly divergent futures lies extremely close in deep-temperature space. Thus maximum spread and guaranteed discrimination are different optimization problems.

## Scientific meaning
Choosing an experiment by total or average separation can be misleading. If the requirement is a uniform guarantee against all materially incompatible futures, aerosol forcing beats deep-ocean temperature in this benchmark.

The result remains model-dependent. Real aerosol ERF is not directly observed as a single exact scalar, and actual observational cost, structural uncertainty, spatial pattern effects, internal variability, and covariance must be incorporated before any real-world recommendation.
