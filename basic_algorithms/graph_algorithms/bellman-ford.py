#TIME COMPLEXITY O(V*E),   where v are the number of vertices and m is the number of edges
"""
	Bellman-Ford -> list representation.
    This is an algorithm that allows finding the lowest cost from the source to every possible vertex, if
    but such a path does not exist, 'inf' is left, or if we are dealing with negative weights,
    our algorithm finds the lowest weight as long as it is not a negative cycle.

    ->bellman_check has the task of checking whether it is possible to perform more relaxation than |V-1|, and if the graph does not have negative cycles, it will not be
    it is possible to induce additional relaxation after so many surgeries, but if it is possible, we are dealing with a negative cycle

    Time complexity O(V*E).
    For the DAG, it is worth sorting topologically and then going through a single Bellmanford iteration, then the complexity will change to O(V + E)
"""

def bellman_ford(G,s):
    n=len(G)
    costs=[float('inf') for _ in range(n)] #array, the cost I have to pay when going from the source to a given vertex
    costs[s]=0  #because we start from this vertex
    def bellman_start(G): #I want to visit every edge in the graph
        for _ in range(n-1): #we want to examine all |V-1| vertices
            for i in range(n):
                for j in range(len(G[i])): #I look through all the neighbors of each vertex and perform relaxation on them
                    relax(G,i,G[i][j][0],j)
    def relax(G,v,u,id_u):
        if costs[u]>costs[v]+G[v][id_u][1]:
            costs[u]=costs[v]+G[v][id_u][1]
    def bellman_check(G): #the function checks whether there is a cycle with a negative weight obtained from the source, if so, we will return infinity for such cases
        for i in range(n):
            for j in range(len(G[i])):
                if costs[G[i][j][0]]>costs[i]+G[i][j][1]:
                    costs[G[i][j][0]]=float('-inf')
    bellman_start(G)
    bellman_check(G) #final check
    return costs

if __name__ == '__main__': #some tests
    Graph=[
        [(1,1)],
        [(0,1),(2,8),(6,2)],
        [(1,8),(3,7)],
        [(2,7),(6,1),(4,20)],
        [(3,20),(5,9)],
        [(4,9),(6,5)],
        [(1,2),(3,1),(5,5)]
    ]
    GraphDAG=[
        [(2,20)],
        [(0,-7),(3,-17),(4,10)],
        [],
        [(2,-5)],
        [],
        [(1,8)],
        [(0,-1)]
    ]
    print(bellman_ford(GraphDAG,5))
