#TIME COMPLEXITY O(N^3), where n is the number of vertices.
"""
The algorithm is used to find the shortest paths between each two vertices. Mainly when we will be there
    When using this algorithm, it will be convenient to use a matrix representation of the graph.
    O(V^3)
"""
def print_matrix(tab):
    for i in range(len(tab)): print(tab[i])
    print('\n')

def inicitalize_costs(tab,G): #an auxiliary function for resetting the diagonal costs array and adding the weights of the partial handles
    for i in range(len(G)):
        tab[i][i]=0 #due to the fact that the cost of reaching itself is simply 0, if there is a negative value on the diagonal, it means that there is a negative cycle in the graph
        for j in range(len(G)):
            if G[i][j]!=0: tab[i][j]=G[i][j]
    return tab

def inicitalize_parents(parents,G):
    for i in range(len(G)):
        for j in range(len(G)):
            if G[i][j]!=0: #means that a given edge exists, because there cannot be an edge equal to 0 in our convention
                parents[i][j]=i #because when there is an edge, there can be only one possibility of the father, only the outgoing edge
    return parents

def find_path(x,y,parents): #pathfinding algorithm
    res=[]
    while x!=y:
        if parents[x][y]==-1: return None #because then such a path does not exist
        res.append(y)
        y=parents[x][y]
    res.append(x)
    res.reverse()
    return res

def warschall(G):
    n=len(G)
    costs=[[float('inf') for _ in range(n)] for _ in range(n)] #the table in the matrix version will be used to help me find out how much it will cost me to get from v to u
    parents = [[-1 for _ in range(n)] for _ in range(n)]
    costs=inicitalize_costs(costs,G)
    parents=inicitalize_parents(parents,G)

    for t in range(n): #I have to go through n points that will serve as connectors to find out if I can find a cheaper path.
        for i in range(n):
            for j in range(n):
                if costs[i][j]>costs[i][t]+costs[t][j]: #this is a property of the path, it means that the shortest path will never change
                    costs[i][j]=costs[i][t]+costs[t][j]
                    parents[i][j]=parents[t][j]
    return costs,parents

if __name__ == '__main__': #some tests
    Graph=[
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 0, 2, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, -50, 0, 0, 15, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 10, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 9, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 12, 0]
    ]
    Graph_minus_cycle=[
        [0, 5, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 0, 2, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, -50, 0, 0, -15, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 10, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 9, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 12, 0]
    ]
    cost,parents=warschall(Graph)
    print_matrix(cost)
    print_matrix(parents)
    print(find_path(7,3,parents))

