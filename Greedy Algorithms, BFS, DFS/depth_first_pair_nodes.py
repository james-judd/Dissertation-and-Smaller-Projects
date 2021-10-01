import networkx as nx
import graph6
import graph7
import graph8
import graph9
import graph10

### count the length of the path between two pre-specified vertices a and b, using Depth-First-Search

def dfs(G,a,b,u):
    n=len(G.nodes())                            #number of nodes
    u=a                                         #u is current vertex
    G.nodes[a]['label']=0
    G.nodes[a]['visited']=1
    G.nodes[b]['label']=0
    L=[a]                                       #list of visited vertices
    while G.nodes[b]['label']==0:               #while b is unvisited:
        l=[]
        l.extend(G.adj[u])                      #create ordered list of vertices adjacent to u
        l.sort()
        d=G.nodes[u]['label']                   #distance
        c=0
        for x in l:                             #for adjacent vertices:
            c+=1                                #'position in list' counter
            if G.nodes[x]['visited']!=1:        #if vertex is unvisited:
                G.nodes[x]['visited']=1         #mark as visited, assign distance, label previous vertex in path
                G.nodes[x]['label']=d+1
                G.nodes[x]['previous']=u
                u=x                             #becomes new current vertex   
                L.append(u)                     #add vertex to visited list
                break                           #exit back to while loop
            else:                               
                if c==len(l):                   #if all adjacent vertices visited:
                    u=G.nodes[u]['previous']    #go back 1 step
    print(L)                                    #print order of visited vertices
                

print()
G6=graph6.Graph()
a=12
b=40
print('Depth-First-Search visited the following nodes of G6 in this order:')
dfs(G6,a,b,a)  ### count the DFS-path from a to b, starting at a
print('Depth-First Search found a path in G6 between vertices', a, 'and', b, 'of length', G6.node[b]['label'])
print()


G7=graph7.Graph()
a=5
b=36
print('Depth-First-Search visited the following nodes of G7 in this order:')
dfs(G7,a,b,a)  ### count the DFS-path from a to b, starting at a
print('Depth-First Search found a path in G7 between vertices', a, 'and', b, 'of length', G7.node[b]['label'])
print()


G8=graph8.Graph()
a=15
b=40
print('Depth-First-Search visited the following nodes of G8 in this order:')
dfs(G8,a,b,a)  ### count the DFS-path from a to b, starting at a
print('Depth-First Search found a path in G8 between vertices', a, 'and', b, 'of length', G8.node[b]['label'])
print()


G9=graph9.Graph()
a=1
b=19
print('Depth-First-Search visited the following nodes of G9 in this order:')
dfs(G9,a,b,a)  ### count the DFS-path from a to b, starting at a
print('Depth-First Search found a path in G9 between vertices', a, 'and', b, 'of length', G9.node[b]['label'])
print()


G10=graph10.Graph()
a=6
b=30
print('Depth-First-Search visited the following nodes of G10 in this order:')
dfs(G10,a,b,a)  ### count the DFS-path from a to b, starting at a
print('Depth-First Search found a path in G10 between vertices', a, 'and', b, 'of length', G10.node[b]['label'])
print()
