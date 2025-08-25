# examples/run_examples.py
from collections import defaultdict
from math import inf
from src.utils import bounded_ms_dijkstra

edges = [
    ('s','a',2), ('s','b',7), ('s','c',9),
    ('a','d',2), ('a','e',4),
    ('b','e',1), ('b','f',3),
    ('c','f',2),
    ('d','g',3), ('e','g',2),
    ('e','h',4), ('f','h',1),
    ('g','i',3), ('h','i',2),
]

def build_graph(edges):
    G = defaultdict(list)
    for u, v, w in edges:
        G[u].append((v, w))
    return G

def vertex_set(edges):
    V = set()
    for u, v, _ in edges:
        V.add(u); V.add(v)
    return V

def demo():
    G = build_graph(edges)
    V = vertex_set(edges)

    dist = {v: inf for v in V}
    dist['s'] = 0.0

    S = {'s'}
    completed, pred = bounded_ms_dijkstra(G, dist, S, B=float('inf'))
    print("Completed vertices (phase 1):", sorted(completed))
    print("Distances after phase 1:", {k: v for k, v in dist.items() if v < inf})

if __name__ == "__main__":
    demo()
