# Exact Cheapest Experiment — Experiment 004

Copyright (C) 2026 Mohammad Amir Khusru Akhtar  
Apache License 2.0

## Objective
Given the admissible climate worlds retained by the pattern-cloud stress test, find the globally cheapest subset of candidate passive diagnostics that distinguishes every pair whose +100-year surface temperature differs by at least 0.50 K.

## Exact formulation
Create the future-incompatibility edge set

E_tau = {(i,j): |T100_i-T100_j| >= tau}.

For each diagnostic q, define S_q as the incompatible edges whose endpoints q distinguishes. Then solve

min_Q sum_{q in Q} c_q  subject to union_{q in Q} S_q = E_tau.

Thus the finite candidate problem is an exact weighted set-cover instance on *future-incompatibility edges*, not on climate states themselves.

## Certificate on Experiment 003 benchmark
Under unit diagnostic costs and structural (zero-resolution) distinguishability, no one-scalar candidate covers all incompatible pairs. Exhaustive enumeration certifies optimum cost 2 and minimum dimension 2. The exact lexicographic winner is printed by `python experiments/exact_cheapest_experiment.py`; tests independently assert that every singleton fails and the optimum is exactly two.

## Novelty boundary
The generic optimization machinery is not claimed as new: minimum sensor placement / discriminability is established in systems and diagnosis literature and is commonly reducible to set cover. The climate-specific scientific question here is narrower: construct observationally admissible Earth-system worlds, define incompatibility by materially divergent climate futures, and identify the least observational burden required to eliminate all such future-confounding pairs.

## Status
This closes the current synthetic benchmark exactly. It does not yet establish a new universal climate law, nor a real-world monetary optimum. Before a paper claims a substantive climate result, replace synthetic worlds/resolutions with observationally constrained ensembles and defensible measurement uncertainty/cost models.
