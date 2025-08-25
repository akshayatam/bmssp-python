import heapq 
from math import inf 

def bounded_ms_dijkstra(G, dist, S, B): 
    """
    Bounded multi-source Dijkstra: 
    Settles all nodes with final distance < B from frontier S. 
    Returns (completed_set, pred)
    """ 

    pq = [] 
    pred = {} 
    completed = set() 

    for s in S: 
        if dist.get(s, inf) < B: 
            heapq.heappush(pq, (dist[s], s)) 

    while pq: 
        d_u, u = heapq.heappop(pq) 
        if d_u != dist.get(u, inf): 
            continue 
        if d_u >= B: 
            break 

        completed.add(u) 
        for v, w in G.get(u, []): 
            nd = d_u + w 
            if nd < B and nd < dist.get(v, inf): 
                dist[v] = nd 
                pred[v] = u 
                heapq.heappush(pq, (nd, v)) 

    return completed, pred 
