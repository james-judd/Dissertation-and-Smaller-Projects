import networkx as nx
import graph6
import graph7
import graph8
import graph9
import graph10

def bfs(G,a,b):
    G.add_nodes_from(G.nodes(), label = -1)     # initialization of all labels
    G.node[a]['label']=0
    G.nodes[a]['visited']=1
    l=[]
    c=0
    while b not in l:
        c+=1                                    #distance counter
        for x in range(1,len(G.nodes())+1):     #for all visited nodes:
            if G.nodes[x]['visited']==1:        
                l.extend(G.adj[x])              #add adjacent vertices to l
        for y in l:                             #for unvisited adjacent vertices:
            if G.nodes[y]['visited']!=1:        
                G.nodes[y]['visited']=1         #mark as visited and assign distance
                G.nodes[y]['label']=c           
    return(G.nodes[b]['label'])                 #return distance of b
    

G6=graph6.Graph()
a=12
b=40
print('Graph G6:')
print('The distance between vertices', a, 'and', b, 'is:', bfs(G6,a,b))
print()


G7=graph7.Graph()
a=5
b=36
print('Graph G7:')
print('The distance between vertices', a, 'and', b, 'is:', bfs(G7,a,b))
print()


G8=graph8.Graph()
a=15
b=35
print('Graph G8:')
print('The distance between vertices', a, 'and', b, 'is:', bfs(G8,a,b))
print()


G9=graph9.Graph()
a=1
b=19
print('Graph G9:')
print('The distance between vertices', a, 'and', b, 'is:', bfs(G9,a,b))
print()


G10=graph10.Graph()
a=6
b=30
print('Graph G10:')
print('The distance between vertices', a, 'and', b, 'is:', bfs(G10,a,b))
print()
