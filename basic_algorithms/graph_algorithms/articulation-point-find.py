#TIME COMPLEXITY O(N + M),  where n are the vertices and m is the number of edges
"""
    The algorithm that finds all articulation points in a graph using Trijan algorithm.
"""
def check_if_exist(tab,value): #function that checks whether the entered value already exists in the array
    n=len(tab)
    for i in range(n):
        if tab[i]==value: return True
    return False

def find_aticulation_point(G):
    n=len(G)
    visited=[False for _ in range(n)]
    parents=[-1 for _ in range(n)]
    time_visit=[0 for _ in range(n)]
    low=[-1 for _ in range(n)]
    articulation_points=[]
    time=0
    def dfs(G):
        for i in range(n):
            if not visited[i]:
                dfs_visit(G,i,i)
    def dfs_visit(G,x,root):
        nonlocal time
        visited[x]=True
        time+=1
        time_visit[x]=time
        low[x]=time #working, it gives such value
        childrens=0
        for i in range(len(G[x])):
            if not visited[G[x][i]]:
                childrens+=1
                parents[G[x][i]]=x
                dfs_visit(G,G[x][i],root)
                low[x] = min(low[x], low[G[x][i]])
                if parents[x] == -1 and childrens > 1 and not check_if_exist(articulation_points,x): articulation_points.append(x)
                if parents[x] != -1 and low[G[x][i]] >= time_visit[x] and not check_if_exist(articulation_points,x): articulation_points.append(x)
            elif G[x][i]!=parents[x]:
                low[x]=min(low[x],time_visit[G[x][i]])
        #if parents[x] != -1 and low[x] < low[parents[x]]: low[parents[x]] = low[x]
        if x==root and childrens > 1 and not check_if_exist(articulation_points,x): articulation_points.append(x)

    dfs(G)
    return articulation_points


if __name__ == '__main__': #some tests
    G1=[
        [1, 2, 6],
        [0, 5],
        [0, 3],
        [2, 4],
        [3, 5, 6],
        [1, 4, 7],
        [0, 4],
        [5, 8],
        [7, 9],
        [8],
    ]
    G2=[
        [1, 2],
        [0, 3, 4],
        [0, 5],
        [1, 6],
        [1, 5],
        [2, 4, 7],
        [3],
        [5, 8],
        [7, 9],
        [8],
    ]
    G3=[
        [1, 3, 6],
        [5, 0, 4, 2],
        [4, 1, 7],
        [8, 0, 7],
        [9, 2, 1, 7, 5, 8],
        [1, 4],
        [0],
        [4, 3, 2],
        [3, 4],
        [4]
    ]









