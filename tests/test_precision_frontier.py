from experiments.precision_frontier import precision_frontier


def test_precision_frontier_has_calibrated_diagnostics():
    rows = precision_frontier()
    assert len(rows) == 5
    assert all(r["epsilon"] >= 0 for r in rows)


def test_aerosol_is_cheapest_under_resolution_burden():
    rows = precision_frontier()
    assert rows[0]["diagnostic"] == "aerosol_ERF_now"
    assert abs(rows[0]["epsilon"] - 0.2) < 1e-12
    assert abs(rows[0]["resolution_burden"] - 2.5) < 1e-12


def test_deep_ocean_requires_much_finer_resolution_for_uniform_guarantee():
    rows = {r["diagnostic"]: r for r in precision_frontier()}
    assert rows["deep_temperature_now"]["epsilon"] < 0.001
    assert rows["deep_temperature_now"]["resolution_burden"] > 300
