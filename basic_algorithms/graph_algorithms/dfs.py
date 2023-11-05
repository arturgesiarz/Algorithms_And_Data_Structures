#TIME COMPLEXITY O(N + M),  where n are the vertices and m is the number of edges
"""
The DFS algorithm, together with the visiting subfunction and recursion, is used for this.
In the DFS function, we normally need two additional variables, one of them is
    the time at which a given vertex was visited, and another time is the time at which it was processed.
    ->A processed vertex is one that either has no neighbors or all of its neighbors have already been visited.
"""

def DFS(G):
    n = len(G)
    visited = [False for _ in range(n)]
    parents = [None for _ in range(n)]
    time_visit=[0 for _ in range(n)]
    time_convert=[0 for _ in range(n)]
    time = 0
    def DFS_start(G):
        for i in range(n): #traversing all vertices
            if visited[i]==False:
                DFS_visit(G,i)
    def DFS_visit(G,x):
        nonlocal time
        time+=1
        time_visit[x]=time
        visited[x]=True
        for i in range(len(G[x])): #I want to search all my neighbors
            if visited[G[x][i]]==False:
                parents[G[x][i]]=x
                DFS_visit(G,G[x][i])
        time+=1
        time_convert[x]=time
    DFS_start(G)
    return parents

if __name__ == '__main__': #some tests
    Graph=[ [1,2], [0,3,4], [0,3], [4,1,2], [1,3,5], [4], [7],[6,8],[7,9,10],[8],[8] ]
    print(DFS(Graph))



