from queue import Queue

graph={
    'A':['B','C'],
    'B':['G'],
     'C':['D','E'],
     'D':['G','F'],
     'E':['F'],
      'G':[],
    'F':[]

}

visited={}
level={}
perent={}
bfs_triversal=[]
queue=Queue()
for v in graph.keys():
    visited[v] =False
    perent[v]=None
    level[v]=-1

s='A'
visited[s]=True
level[s]=0
queue.put(s)
while not queue.empty():
    u=queue.get()
    bfs_triversal.append(u)
    for i in graph[u]:
        if not visited[i]:
            visited[i]=True
            perent[i]=u
            level[i]=level[u]+1
            queue.put(i)


print(bfs_triversal)
print(visited)



