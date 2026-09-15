# Pattern–Cloud Hidden-World Stress Test 003

Copyright (C) 2026 Mohammad Amir Khusru Akhtar

## Question
Does the one-scalar winner from the earlier precision benchmark survive when the knowledge set admits hidden SST-pattern and cloud-response dimensions?

## Construction
We extend the deliberately simple two-layer energy-balance ensemble with two nuisance dimensions: a discrete SST-pattern state and a cloud-pattern sensitivity. Worlds are retained only when present surface warming and TOA imbalance remain inside the same coarse observational windows. A pair is called future-incompatible when its +100-year surface temperatures differ by at least 0.50 K under a common future forcing protocol.

Candidate scalar diagnostics are present aerosol ERF, present deep temperature, an SST-pattern index, cloud-pattern sensitivity, and their pattern×cloud product.

## Cost
Here cost is only the number of scalar diagnostics. A diagnostic set succeeds if no materially future-incompatible pair has exactly the same joint diagnostic vector. This experiment deliberately does not compare physical units or claim realistic measurement precision.

## Result
The expanded benchmark retains 69 calibrated worlds. Every individual candidate scalar leaves at least one materially incompatible pair exactly confounded. Thus the earlier one-scalar aerosol result is not structurally robust to these added hidden dimensions.

The minimum successful diagnostic cardinality is **two**. In this discrete stress test, the pair

    (deep_temperature_now, cloud_pattern_sensitivity)

separates every pair of worlds whose +100-year surface temperatures differ by at least 0.50 K.

## Interpretation
The key result is not that these two real measurements should be deployed. It is the stronger structural observation that adding a physically motivated hidden degree of freedom can increase the minimum experiment dimension. A scalar that was sufficient in a lower-dimensional knowledge set ceases to be sufficient after the admissible possible-world set is enlarged.

This suggests a candidate object for further theory: the **minimum separating experiment dimension** of a knowledge set,

    d*(K, G) = min{|Q| : Q separates every pair of K-consistent worlds differing by at least G in the target future}.

The immediate research question is whether d* has nontrivial lower bounds, monotonicity properties under knowledge refinement/enlargement, or a hierarchy that survives realistic climate-model ensembles.

## Limitations
This is a synthetic falsification-oriented benchmark, not an Earth-system inference. The pattern and cloud parameterization is intentionally simple; the SST-pattern index and cloud sensitivity are not directly equivalent to one operational observing system; internal variability, covariance, spatial fields, aerosol-cloud interactions, and real observational costs are absent. The next stage must test the structural claim using real model ensembles and observationally defined diagnostics.
