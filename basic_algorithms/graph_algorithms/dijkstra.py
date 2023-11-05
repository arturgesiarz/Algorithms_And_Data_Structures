#TIME COMPLEXITY O ( V + E LogV ),  where v  is the number of vertices and e is the number of edges,
"""
	Dijkstra's algorithm, in list representation.
"""

from queue import PriorityQueue

def dijkstra(G,s): #We send the graph to the function along with the weight function and our starting point
    n=len(G)
    parents=[-1 for _ in range(n)]
    costs=[float('inf') for _ in range(n)]
    costs[s]=0
    q=PriorityQueue()
    q.put((0,s)) #because the distance to the start is 0
    def dijkstra_start(G,s):
        while q.qsize()>0:
            u=q.get()[1] #the smallest vertex will always be charged at cost, this results from the definition of the priority queue
            for i in range(len(G[u])):
                relax(G,u,G[u][i][0],i) #I pass on my neighbor's ID so that I can easily move to his place
    def relax(G,u,v,id_v):
        if costs[v]>costs[u]+G[u][id_v][1]:
            costs[v]=costs[u] + G[u][id_v][1]
            parents[v]=u
            q.put((costs[v],v))
    dijkstra_start(G,s)
    return costs

if __name__ == '__main__': #some tests

    #[0, 1, 9, 4, 17, 8, 3]
    Graph=[
        [(1,1)],
        [(2,8),(6,2)],
        [(1,8),(3,7)],
        [(2,7),(6,1),(4,20)],
        [(3,20),(5,9)],
        [(4,9),(6,5)],
        [(1,2),(3,1),(5,5)]
    ]
    print(dijkstra(Graph,0))











