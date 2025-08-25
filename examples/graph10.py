edges = [
    ('s','a',2), ('s','b',7), ('s','c',9), 
    ('a','d',2), ('a','e',4), 
    ('b','e',1), ('b','f',3), 
    ('c','f',2), 
    ('d','g',3), ('e','g',2), 
    ('e','h',4), ('f','h',1), 
    ('g','i',3), ('h','i',2) 
] 

def build_graph(): 
    from collections import defaultdict 
    G = defaultdict(list) 
    for u,v,w in edges: 
        G[u].append((v,w)) 
    return G 
