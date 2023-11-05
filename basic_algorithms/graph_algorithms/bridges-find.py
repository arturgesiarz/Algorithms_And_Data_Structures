#TIME COMPLEXITY O(N + M),  where n are the vertices and m is the number of edges
"""
	The algorithm is to determine all bridges in graf.
"""

def find_bridge(G):
    n=len(G)
    visited=[False for _ in range(n)]
    parents=[-1 for _ in range(n)]
    time_visit=[0 for _ in range(n)]
    low=[-1 for _ in range(n)]
    bridges=[]
    time=0
    def dfs(G):
        for i in range(n):
            if not visited[i]:
                dfs_visit(G,i)
    def dfs_visit(G,x):
        nonlocal time
        visited[x]=True
        time+=1
        time_visit[x]=time
        low[x]=time #roboczo, nadaje taka wartosc
        for i in range(len(G[x])):
            if not visited[G[x][i]]:
                parents[G[x][i]]=x
                dfs_visit(G,G[x][i])
            elif G[x][i]!=parents[x]:  #if this is not the parent and the vertex was visited, it means that I hit a backward/secondary edge
                low[x]=min(time_visit[x],low[G[x][i]])
        if parents[x] != -1 and low[x] < low[parents[x]]: low[parents[x]] = low[x]#we check whether the value of our low is lower than the parent's, if so, we replace it
        if time_visit[x]==low[x] and x!=0: #means we found the bridge
            bridges.append((x,parents[x]))
    dfs(G)
    return bridges

if __name__ == '__main__': #some tests
    Graph=[
        [1,6],
        [0,2],
        [1,3,6],
        [2,4,5],
        [3,5],
        [3,4],
        [0,2,7],
        [6]
    ]
    print(find_bridge(Graph))
