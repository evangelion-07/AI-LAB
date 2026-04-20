#uniform
import heapq

g={}
e=int(input("Enter number of edges: "))
for _ in range(e):
    u=input("From: ")
    v=input("To: ")
    w=int(input("Cost: "))
    g.setdefault(u,[]).append((v,w))

start=input("Start: ")
goal=input("Goal: ")

pq=[(0,start,[start])]   # added path
vis=set()

while pq:
    cost,node,path = heapq.heappop(pq)

    if node==goal:
        print("Optimal Cost:",cost)
        print("Path:",path)
        break

    if node not in vis:
        vis.add(node)
        for i,w in g.get(node,[]):
            heapq.heappush(pq,(cost+w,i,path+[i]))  # update pat