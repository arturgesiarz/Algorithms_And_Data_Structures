#TIME COMPLEXITY O(ELogE), where e is the number of edges in the graph.
"""
	Implementation of Kruskal's algorithm.
    Kruskal's algorithm is that I sort the edges ascending, and I process every edge in my graph
    exactly in this order. Then I create disconnected sets for each vertex.
    When I next walk up the smallest edges, I will check whether I have already connected them.
    given edges to my minimal spanning tree. Before connecting two vertices, I check their representatives,
    in a disjoint set - if they happen to have the same person, it means that they belong to the same group, so I cannot connect them
    , but if they are not necessary, I combine them in such a way that I enlarge my set of edges by a given vertex and change the represented ones.
"""

class Node: #this data structure is used to use disjoint sets
    def __init__(self): #create a structure of disjoint trees
        self.parent=self #this is intended to break up the parent in some kind of loop that will allow us to continue searching
        self.rank=0 #estimation of tree height

def find_set(x): #function that finds the parent, and also immediately connects to it via recursion
    if x!=x.parent:
        x.parent=find_set(x.parent)
    return x.parent

def union(x,y):  #function, joining, both vertices that are as if on an edge together into one set
    x=find_set(x)
    y=find_set(y) #makes it possible to find the root of given nodes and immediately connect them to their parents to make it faster
    if x.rank>y.rank: #we will combine, smaller with larger
        y.parent=x #connecting all my remaining nodes to x
    else:
        x.parent=y
        if x.rank==y.rank:
            y.rank+=1 #because I'm now increasing the estimate to the height of my node
def convert_to_edges_sorted(G): #sorting function, edges by weights -> O(E)
    n=len(G)
    edges=[]
    for v in range(n):
        for neightboors in range(len(G[v])):
            edges.append((v,G[v][neightboors][0],G[v][neightboors][1]))
    return sorted(edges,key=lambda edges:edges[2])

def krusal(G): # O(ElogV)
    n=len(G)
    edges=convert_to_edges_sorted(G) # O(E)
    sets=[Node() for _ in range(n)] # O(V)
    edges_sol=[]
    for edge in edges: #we will look at the tops one by one in order of increasing weight
        if find_set(sets[edge[0]])!=find_set(sets[edge[1]]): #this means that the parents are different, so I will be able to join the disjoint sets together
            union(sets[edge[0]],sets[edge[1]])
            edges_sol.append((edge[0],edge[1]))
    return edges_sol

if __name__ == '__main__': #some tests
    Graph=[
        [(1,4)],
        [(2,8),(4,10)],
        [(1,8),(3,7),(4,2),(5,3)],
        [(2,7)],
        [(1,10),(2,2),(5,1),(6,5)],
        [(2,3),(4,1),(6,2)],
        [(4,5),(5,2)]
    ]
    print(krusal(Graph))
