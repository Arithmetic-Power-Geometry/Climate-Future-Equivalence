from experiments.robust_cheapest_experiment import exact_robust_minimum, robustness_frontier


def test_zero_uncertainty_recovers_finite_solution():
    _, pairs, k, winners = exact_robust_minimum(scale=0.0)
    assert pairs
    assert k is not None
    assert winners


def test_uncertainty_cannot_improve_minimum_count():
    rows = robustness_frontier((0.0, 0.25, 0.5, 1.0))
    finite = [(s, k) for s, _, _, k, _ in rows if k is not None]
    counts = [k for _, k in finite]
    assert counts == sorted(counts)
