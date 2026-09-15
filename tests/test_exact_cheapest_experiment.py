"""Copyright (C) 2026 Mohammad Amir Khusru Akhtar; Apache-2.0."""
from experiments.exact_cheapest_experiment import exact_minimum, DIAGNOSTICS


def test_no_single_diagnostic_covers_all_incompatible_futures():
    worlds,edges,best,cover=exact_minimum()
    assert len(worlds)>=2 and len(edges)>0
    assert all(cover[q] != edges for q in DIAGNOSTICS)


def test_exact_minimum_has_two_diagnostics():
    _,_,best,_=exact_minimum()
    assert best is not None
    assert best[0] == 2.0
    assert best[1] == 2
