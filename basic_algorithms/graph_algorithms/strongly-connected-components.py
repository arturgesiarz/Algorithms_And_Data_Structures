#TIME COMPLEXITY O(V+E),  where e is the number of edges in the graph, and v is the number of the vertices.
"""
Algorithm for finding strongly connected components in a DAG.
    In the given algorithm, I return an array whose -1 symbolizes that the 'connected component' begins and the following numbers, respectively.
no longer being -1 means that this number from a given insek is in 'consistency' with the previous one, and when we encounter -1 we will start
another coherent component.
    Scalable connections are vertices for which we can reach any point from x to y.
    You can also add that the number '-1' symbolizes the number of connected components
"""

def DFS(G):
    n=len(G)
    visited=[False for _ in range(n)]
    time_exit=[0 for _ in range(n)]  #array, marking the time in which the vertex was processed
    time=0
    def DFS_start(G):
        for i in range(n):
            if visited[i]==False:
                DFS_visit(G,i)
    def DFS_visit(G,x):
        nonlocal time
        visited[x]=True
        time+=1
        for i in range(len(G[x])):
            if not visited[G[x][i]]:
                DFS_visit(G,G[x][i])
        time+=1
        time_exit[x]=(time,x)
    DFS_start(G)
    return time_exit

def transparate_graph(G): #graph translating function, i.e. we will simply reverse our edges in the DAGU graph
    n=len(G)
    solution=[[] for _ in range(n)] #to avoid references
    for i in range(n):
        for j in range(len(G[i])):
            solution[i].append(G[i][j]) #assigns values ​​so that nothing changes by reference
    for v in range(n):
        for adj in range(len(G[v])): #checking on my neighbor
            temp=G[v][adj] #one by one I visit the vertices in my original graph
            solution[v].pop(0) #I'm deleting the first elements because it would be like adding them the other way around
            solution[temp].append(v)
    return solution

def find_strong_connected_fragments(G):
    n=len(G)
    visited=[False for _ in range(n)]
    parents=[-1 for _ in range(n)]

    transparate_G=transparate_graph(G)
    time_exist_G=DFS(G) #I need this to have time to process the vertex data
    time_exist_G.sort(reverse=True)  #sorting takes place here by the first element

    tab_solution=[[] for _ in range(n)] #I create sets for my specific results

    print(time_exist_G)

    def connected_start(G):
        nonlocal time_exist_G
        for i in range(n):
            if visited[time_exist_G[i][1]]==False:
                connected_visit(G,time_exist_G[i][1],time_exist_G[i][1])
    def connected_visit(G,x,root):
        visited[x]=True
        for i in range(len(G[x])):
            if visited[G[x][i]]==False:
                print(G[x][i])
                tab_solution[root].append(G[x][i])
                parents[G[x][i]]=x
                connected_visit(G,G[x][i],root)
        #tab_solution.append(x)
        print("\n")
    connected_start(transparate_G)
    #return parents
    #return  tab_solution
    return tab_solution


if __name__ == '__main__': #some tests
    Graph = [
        [1],
        [2, 3, 6],
        [3],
        [6, 5],
        [],
        [4, 6],
        []
    ]
    Graph2=[
        [1,3],
        [2],
        [0,3,5],
        [4],
        [3,5,7],
        [6],
        [5,7],
        [7]
    ]
    graph1 = [
        [1, 2],  # 0
        [3],  # 1
        [4],  # 2
        [0],  # 3
        [2, 5],  # 4
        [6],  # 5
        [5, 7],  # 6
        [4, 8],  # 7
        [6, 9],  # 8
        [7]  # 9
    ]
    print(find_strong_connected_fragments(graph1))

