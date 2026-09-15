# Climate Future Equivalence

A mathematical and computational research framework for testing whether climate states and interventions that are indistinguishable over finite horizons can diverge in their long-term futures, and for finding the lowest-cost experiment that separates climate-consistent but mutually incompatible possible worlds.

## Research question

Given a knowledge set K that admits multiple climate worlds W={w1,...,wn}, find the cheapest admissible experiment e such that the experiment's predicted observations are mutually incompatible for at least two worlds.

Formally, with experiment cost c(e) and response R(w,e), solve

    e* = argmin_e c(e)

subject to a distinguishability requirement

    d(R(w_i,e), R(w_j,e)) >= tau

for at least one pair of worlds w_i,w_j consistent with current knowledge.

The initial benchmark uses a two-layer energy-balance model and contrasts two compensating climate worlds: a higher-sensitivity/stronger-ocean-uptake world and a lower-sensitivity/weaker-ocean-uptake world. Candidate experiments are bounded radiative-forcing pulses. The benchmark searches pulse amplitude-duration pairs for the lowest integrated forcing cost that produces a detectable difference in surface and deep-ocean response.

## Why this benchmark

Historical warming alone can leave materially different combinations of climate sensitivity, aerosol forcing, and ocean heat uptake compatible with observations. The repository tests whether targeted perturbations can separate such worlds more efficiently than passive waiting.

## Current status

This repository is a falsification-oriented lab, not a claim of a new climate theory. Results from simplified models are diagnostic only. Every candidate result should later be tested against stronger physical models, realistic forcing channels, observational noise, ethical/safety constraints, and prior art.

## Run

```bash
python experiments/cheapest_probe.py
```

The script prints all candidate experiments and the cheapest one meeting the configured distinguishability threshold.

## License

Apache License 2.0.

Copyright (C) 2026 Mohammad Amir Khusru Akhtar
