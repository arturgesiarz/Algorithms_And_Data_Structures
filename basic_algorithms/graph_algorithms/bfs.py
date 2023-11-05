#TIME COMPLEXITY O(N + M),  where n are the vertices and m is the number of edges
"""
Algorithm, BFS - breadth first search. This is a breadth-first search of the graph. We will implement for neighborhood lists.
I.e. it will be a two-dimensional list for which the first dimension will denote a given vertex and the array will denote a given vertex
assigned will mean vertices that are connected directly to this vertex by an edge
"""

from collections import deque

def BFS(Graph,x): #To the graph search function, I add this graph and the starting point - the neighborhood list
    n=len(Graph) #number of vertices
    visited=[False for _ in range(n)]
    q=deque()
    q.append(x) #adds to my queue the vertex from which I should start
    visited[x]=True #because I visited the peak from which I had just started
    print(x)
    while len(q)>0: #as long as there are any items in the queue
        v=q.popleft() #removes and returns the element on the left
        for i in range(len(Graph[v])):
            if visited[Graph[v][i]]==False:
                print(Graph[v][i])
                q.append(Graph[v][i])
                visited[Graph[v][i]]=True #because we just visited him

if __name__ == '__main__':
	Graph=[ [1],[0,2],[1,3,4],[2,4],[3,2] ] #directed graph
    BFS(Graph,1)
