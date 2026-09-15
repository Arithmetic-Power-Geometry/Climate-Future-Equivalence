from experiments.cheapest_probe import distinguishability


def test_known_cheapest_candidate_detectable():
    surface, deep, score = distinguishability(1.0, 1.0)
    assert score >= 1.0
    assert surface > 0.01
    assert deep > 0.0


def test_half_year_unit_pulse_not_detectable_at_current_threshold():
    _, _, score = distinguishability(1.0, 0.5)
    assert score < 1.0


def test_response_scales_linearly_for_small_forcing_in_linear_ebm():
    s1, d1, _ = distinguishability(0.5, 1.0)
    s2, d2, _ = distinguishability(1.0, 1.0)
    assert abs(s2 / s1 - 2.0) < 1e-9
    assert abs(d2 / d1 - 2.0) < 1e-9
