#!/usr/bin/python3

from __future__ import division
import sys
import math
import random
import numpy
import itertools
import functools

def norm(p):
    return math.sqrt(sum([x**2 for x in p]))

def sphere_point(d=3):
    p = tuple(random.normalvariate(0, 1) for i in range(d))
    denom = norm(p)
    return tuple(x/denom for x in p)

def orientation(points):
    assert(len(points)==4)
    return numpy.linalg.det(tuple(p+(1,) for p in points))

def facets(points):
    facets = list()
    for a,b,c in itertools.combinations(points, 3):
        o = [orientation([a, b, c, d]) for d in points if d not in [a, b, c]]
        if functools.reduce(lambda a,b: a and b,  [x <= 0 for x in o]):
            facets.append((a,b,c))
        elif functools.reduce(lambda a,b: a and b,  [x >= 0 for x in o]):
            facets.append((c,b,a))
    return facets

if __name__ == "__main__":
    n = 200
    points = [sphere_point() for i in range(n)]
    for p in points:
        print(p, norm(p))
    for i in range(10):
        pts = random.sample(points, 4)
        print(orientation(pts))

    print (orientation([ (0,0,0), (1,0,0), (0,1,0), (0,0,-1) ]))

    for i in range(1000):
        pts = random.sample(points, 5)
        fcts = facets(pts)
        outside = [len([1 for p in points if not p in f and orientation(f+(p,))>0])/n \
                   for f in fcts]
        if max(outside) <= .25:
             print("*", end='')
        else:
            print("-", end='')
        sys.stdout.flush()
        #print(len(fcts), max(outside), sum(outside))
