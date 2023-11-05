#TIME COMPLEXITY O(ElogV),where e is the number of edges in the graph, and v is the number of the vertices.
"""
	The Prim's algorithm consists in moving from a selected vertex and checking individual neighbors in relation to
    the smallest weight. I use the priority queue and check all the time at the lowest possible weight.
    I almost do relaxation -> only, I don't add the total cost of getting there, I just add the weight and change the parent.
    An additional feature of the Prim's algorithm is that the parent array is the structure of the resulting spanning tree.
    And in the Kruskal's algorithm we only have the edges that belong and nothing else.
"""

from queue import PriorityQueue

def prim(G,root): #we have to add a root in this algorithm because we have to start from some point
    n=len(G)
    keys=[float('inf') for _ in range(n)] #stores the current best value
    parents=[-1 for _ in range(n)] #I will need this table to open the graph
    v_in_quene=[True for _ in range(n)] #if we take it out of the queue, it means that this vertex no longer exists
    keys[root]=0
    q=PriorityQueue()
    q.put((keys[root],root))

    while q.qsize()>0:
        v=q.get()[1]
        v_in_quene[v]=False #when I remove a certain vertex from the queue, I have to take it into account when checking other vertices so as not to get an incorrect result
        for neightbour in range(len(G[v])):
            if keys[G[v][neightbour][0]]>G[v][neightbour][1] and v_in_quene[G[v][neightbour][0]]:
                parents[G[v][neightbour][0]]=v
                keys[G[v][neightbour][0]]=G[v][neightbour][1]
                q.put((keys[G[v][neightbour][0]],G[v][neightbour][0]))
    return parents

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
    print(prim(Graph,0))




