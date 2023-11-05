#TIME COMPLEXITY O(V+E),  where e is the number of edges in the graph, and v is the number of the vertices.
"""
Topological sorting algorithm. It only works for directed graphs, acyclic DAGs, by definition
"""

def topological_sort(G):
    n=len(G)
    topological_solution=[]
    visited=[False for _ in range(n)]
    time=0
    time_visited=[0 for _ in range(n)] #times to visit each specific peak
    time_end=[0 for _ in range(n)] #processing times
    def DFS_start(G):
        for i in range(n):
            if visited[i]==False:
                DFS_visit(G,i)
    def DFS_visit(G,x):
        nonlocal time
        visited[x]=True
        time+=1
        time_visited[x]=time
        for i in range(len(G[x])):
            if visited[G[x][i]]==False:
                DFS_visit(G,G[x][i])
        time+=1
        time_end[x]=time
        topological_solution.append(x)
    DFS_start(G)
    topological_solution.reverse()
    return topological_solution,time_end,time_visited

if __name__ == '__main__': #some tests
    Graph = [
        [1],
        [2,3,6],
        [3],
        [6,5],
        [],
        [4,6],
        []
        ]
    print(topological_sort(Graph))
    tab=[2,3,4,1,2]
    tab.sort(reverse=True)
    print(tab)
