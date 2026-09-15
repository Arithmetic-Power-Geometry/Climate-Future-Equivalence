"""Exact cheapest experiment as a weighted incompatibility-cover problem.

Copyright (C) 2026 Mohammad Amir Khusru Akhtar
Licensed under the Apache License, Version 2.0.

For the calibrated pattern-cloud benchmark, construct an incompatibility graph:
vertices are admissible climate worlds and an edge joins two worlds when their
+100-year surface outcomes differ by at least FUTURE_GAP. A diagnostic covers an
edge iff it distinguishes its endpoints at the stated resolution. The cheapest
experiment is the minimum-cost subset of diagnostics covering every incompatible
edge. Exhaustive enumeration is exact for this deliberately small candidate set.
"""
from itertools import combinations
from experiments.pattern_cloud_stress import ensemble, future100, value, FUTURE_GAP

DIAGNOSTICS = (
    "aerosol_ERF_now",
    "deep_temperature_now",
    "SST_pattern_index",
    "cloud_pattern_sensitivity",
    "pattern_cloud_product",
)


def incompatible_edges(worlds, gap=FUTURE_GAP):
    return {(i,j) for i in range(len(worlds)) for j in range(i+1,len(worlds))
            if abs(future100(worlds[i])-future100(worlds[j])) >= gap}


def covered_edges(worlds, diagnostic, edges, resolution=0.0):
    # resolution=0 is the structural/in-principle benchmark used in Experiment 003.
    return {(i,j) for i,j in edges
            if abs(value(worlds[i],diagnostic)-value(worlds[j],diagnostic)) > resolution}


def exact_minimum(costs=None, resolutions=None, gap=FUTURE_GAP):
    worlds=ensemble(); edges=incompatible_edges(worlds,gap)
    costs = costs or {q:1.0 for q in DIAGNOSTICS}
    resolutions = resolutions or {q:0.0 for q in DIAGNOSTICS}
    cover={q:covered_edges(worlds,q,edges,resolutions[q]) for q in DIAGNOSTICS}
    feasible=[]
    for k in range(1,len(DIAGNOSTICS)+1):
        for subset in combinations(DIAGNOSTICS,k):
            union=set().union(*(cover[q] for q in subset))
            if union==edges:
                feasible.append((sum(costs[q] for q in subset),len(subset),subset))
    if not feasible:
        return worlds,edges,None,cover
    feasible.sort(key=lambda x:(x[0],x[1],x[2]))
    return worlds,edges,feasible[0],cover


def certificate():
    worlds,edges,best,cover=exact_minimum()
    singles={q:len(edges-cover[q]) for q in DIAGNOSTICS}
    return {"worlds":len(worlds),"incompatible_edges":len(edges),"best":best,
            "uncovered_by_single":singles}


def main():
    c=certificate()
    print(f"calibrated_worlds={c['worlds']}")
    print(f"incompatible_edges={c['incompatible_edges']}")
    for q,n in c['uncovered_by_single'].items(): print(f"single_uncovered,{q},{n}")
    print(f"EXACT_CHEAPEST_COST={c['best'][0]:.6g}")
    print(f"EXACT_MINIMUM_DIMENSION={c['best'][1]}")
    print("EXACT_CHEAPEST_EXPERIMENT="+"+".join(c['best'][2]))

if __name__=="__main__": main()
