# Pre-Manuscript Falsification and Novelty Audit 005

Copyright (C) 2026 Mohammad Amir Khusru Akhtar
Licensed under the Apache License, Version 2.0.

## Research question
Given current knowledge K defining an admissible set of climate worlds W_K, and a future target G, find the minimum-cost experiment set Q that separates every pair of worlds whose future target differs by at least a material threshold tau.

D_tau(K) = min_Q C(Q) subject to: for every wi,wj in W_K with |G(wi)-G(wj)| >= tau, at least one q in Q distinguishes wi and wj.

## Computational chain
1. Two-world forcing-pulse benchmark: demonstrates active separation but is not a real-world intervention recommendation.
2. Calibrated ensemble benchmark: 194 worlds satisfy common coarse present constraints while retaining materially different futures.
3. Precision frontier: maximum ensemble spread and worst-case guaranteed discrimination select different diagnostics.
4. Pattern/cloud stress test: expanding hidden climate mechanisms destroys every one-scalar guarantee.
5. Exact cheapest experiment: exhaustive finite-library search establishes the global optimum for the synthetic benchmark under its stated cost and diagnostic library.

## Current synthetic result
For the pattern/cloud stress benchmark, no candidate scalar diagnostic separates every pair whose +100-year surface temperature differs by at least 0.50 K. The minimum equal-cost diagnostic cardinality is 2. This is a benchmark result, not an observational claim about Earth.

## Novelty boundary
Do NOT claim novelty for:
- generic optimal experimental design;
- minimum sensor placement;
- functional observability;
- set-cover reduction;
- information gain or Fisher-information design;
- generic equifinality;
- generic climate data targeting.

These have substantial prior literature.

Potentially defensible contribution to test in the manuscript:
- define admissibility by present climate knowledge rather than a single fitted state;
- define incompatibility directly in a future decision target G and material threshold tau;
- optimize observations only over pairs that are present-knowledge-equivalent yet future-incompatible;
- expose the minimum observational burden needed to collapse those future-incompatible equivalence classes;
- demonstrate that the identity and dimension of the cheapest experiment can change when hidden climate mechanisms are enlarged.

## Relation to prior work
Climate optimal experimental design already targets observations in regions/times that maximize parameter information or reduce uncertainty. Functional observability already asks for minimum sensors sufficient to reconstruct target variables, and minimum placement can reduce to set cover. Therefore the manuscript must distinguish future-targeted pair separation from parameter estimation, full-state reconstruction, and generic sensor placement.

## Claims allowed now
- The repository contains a reproducible synthetic climate benchmark for future-targeted discrimination.
- In the current finite pattern/cloud benchmark, no single candidate scalar diagnostic is sufficient and the minimum equal-cost diagnostic count is two.
- The optimum is exact only relative to the finite candidate diagnostic library, model grid, calibration tolerances, future target, incompatibility threshold, and zero-noise structural distinguishability criterion.

## Claims not allowed now
- This is not yet a new law of climate physics.
- It is not proven that two real-world measurements are sufficient.
- It is not proven that the selected synthetic pair is the cheapest real observing program.
- It is not proven that D_tau is mathematically novel across all fields.
- It is not proven that arbitrary-dimensional separation is required by real Earth-system physics.

## Manuscript readiness gate
A theory/method paper can now be drafted as a falsifiable methodological contribution, provided the limitations above are explicit. A stronger climate-science claim requires observationally calibrated ensembles, realistic covariance/noise, real acquisition costs, and spatial diagnostics or GCM/ESM ensembles.
