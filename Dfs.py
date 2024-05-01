def DFSTraversal(adj,n):
    visited=[False]*(n+1)
    result=[]
    for i in range(1,n+1):
        if visited[i]==False:
            initiateDFS(i,visited,adj,result)
    print(*result)

def initiateDFS(node,visited,adj,result):
    result.append(node)
    visited[node]=True
    for n in adj[node]:
        if visited[n]==False:
            initiateDFS(n,visited,adj,result)

n, m = map(int, input().split())
adj = []
for i in range(n+1):
    adj.append([])
 
for i in range(m):
    u,v = map(int,input().split())
    adj[u].append(v)
    adj[v].append(u)

    
DFSTraversal(adj,n)
