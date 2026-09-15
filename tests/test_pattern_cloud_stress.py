from experiments.pattern_cloud_stress import search


def test_hidden_pattern_cloud_requires_at_least_two_scalars():
    worlds, one_scalar, winners = search()
    assert len(worlds) >= 2
    assert all(not ok for _, ok, _ in one_scalar)
    assert winners
    assert winners[0][0] == 2


def test_deep_plus_cloud_sensitivity_is_a_minimal_separator():
    _, _, winners = search()
    subsets = {tuple(row[1]) for row in winners}
    assert ("deep_temperature_now", "cloud_pattern_sensitivity") in subsets
