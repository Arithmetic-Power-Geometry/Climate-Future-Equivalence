"""Calibrated incompatible-world search for Climate Future Equivalence.

Copyright (C) 2026 Mohammad Amir Khusru Akhtar
Licensed under the Apache License, Version 2.0.

Purpose
-------
Move beyond two hand-picked worlds. Generate an ensemble of two-layer climate
worlds, retain only those consistent with the same coarse historical knowledge,
and ask which *single additional scalar diagnostic* most strongly separates
remaining mutually incompatible futures.

This is a methodological benchmark, not a claim about real-world monetary cost.
'Cost' below is measurement dimensionality: one scalar diagnostic = unit cost 1.
"""
from __future__ import annotations
from dataclasses import dataclass
import math

@dataclass(frozen=True)
class World:
    ecs: float
    gamma: float
    aerosol: float

CS, CD, F2X = 8.0, 100.0, 3.7
DT = 0.1
HIST_YEARS = 170.0


def forcing(t: float, aerosol: float) -> float:
    # Idealized GHG ramp to 3.2 W/m2 plus aerosol cooling that emerges after 1950.
    ghg = 3.2 * t / HIST_YEARS
    aerosol_on = max(0.0, (t - 100.0) / (HIST_YEARS - 100.0))
    return ghg + aerosol * aerosol_on


def simulate(w: World, future_years: float = 100.0):
    lam = F2X / w.ecs
    s = d = 0.0
    hist=[]
    n=int(HIST_YEARS/DT)
    for i in range(n+1):
        t=i*DT
        f=forcing(t,w.aerosol)
        nflux=f-lam*s
        hist.append((t,s,d,nflux))
        ds=(f-lam*s-w.gamma*(s-d))/CS
        dd=w.gamma*(s-d)/CD
        s += DT*ds; d += DT*dd
    # Common future forcing: aerosol removed and forcing held at 3.2 W/m2.
    fut=[]
    for i in range(int(future_years/DT)+1):
        t=i*DT
        f=3.2
        nflux=f-lam*s
        fut.append((t,s,d,nflux))
        ds=(f-lam*s-w.gamma*(s-d))/CS
        dd=w.gamma*(s-d)/CD
        s += DT*ds; d += DT*dd
    return hist,fut


def interp(rows, year, col):
    return min(rows,key=lambda r:abs(r[0]-year))[col]


def ensemble():
    out=[]
    for ecs_i in range(20,51):
        ecs=ecs_i/10
        for g_i in range(4,25):
            gamma=g_i/20
            for a_i in range(-18,-3,2):
                aerosol=a_i/10
                w=World(ecs,gamma,aerosol)
                h,f=simulate(w)
                # Shared coarse historical knowledge: present warming and TOA imbalance.
                gmst=h[-1][1]; toa=h[-1][3]
                if abs(gmst-1.20)<=0.08 and abs(toa-0.70)<=0.20:
                    out.append((w,h,f))
    return out


def main():
    worlds=ensemble()
    if len(worlds)<2:
        raise SystemExit('Calibration left too few worlds')

    # Candidate one-scalar diagnostics. All have equal dimensional cost=1.
    diagnostics={
        'historical_surface_120y': lambda h,w: interp(h,120,1),
        'historical_surface_150y': lambda h,w: interp(h,150,1),
        'historical_TOA_150y': lambda h,w: interp(h,150,3),
        'deep_temperature_now': lambda h,w: h[-1][2],
        'aerosol_ERF_now': lambda h,w: w.aerosol,
    }
    # Normalize by illustrative observational scales; higher range/scale separates more.
    scales={
        'historical_surface_120y':0.05,
        'historical_surface_150y':0.05,
        'historical_TOA_150y':0.15,
        'deep_temperature_now':0.02,
        'aerosol_ERF_now':0.20,
    }
    ranked=[]
    for name,fn in diagnostics.items():
        vals=[fn(h,w) for w,h,f in worlds]
        span=max(vals)-min(vals)
        ranked.append((span/scales[name],name,span))
    ranked.sort(reverse=True)

    # Demonstrate incompatible futures under identical future forcing.
    future50=[interp(f,50,1) for w,h,f in worlds]
    future100=[interp(f,100,1) for w,h,f in worlds]
    print(f'calibrated_worlds={len(worlds)}')
    print(f'ECS_range={min(w.ecs for w,_,__ in worlds):.2f},{max(w.ecs for w,_,__ in worlds):.2f}')
    print(f'aerosol_range={min(w.aerosol for w,_,__ in worlds):.2f},{max(w.aerosol for w,_,__ in worlds):.2f}')
    print(f'future50_surface_range={min(future50):.4f},{max(future50):.4f}')
    print(f'future100_surface_range={min(future100):.4f},{max(future100):.4f}')
    print('diagnostic,normalized_separation,raw_span,scalar_cost')
    for score,name,span in ranked:
        print(f'{name},{score:.6f},{span:.6f},1')
    print(f'CHEAPEST_MAX_SEPARATION={ranked[0][1]}')

if __name__=='__main__':
    main()
