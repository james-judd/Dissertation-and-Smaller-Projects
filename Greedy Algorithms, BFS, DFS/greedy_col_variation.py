import networkx as nx
import graph1
import graph2
import graph3
import graph4
import graph5


def find_next_vertex(G):
    n=len(G.nodes())                        #number of nodes
    if G.nodes[1]['visited']!=1:            #for first iteration:
        G.nodes[1]['color']=1               #vertex assigned smallest color and marked visited
        G.nodes[1]['visited']=1                 
    else:
        L=[]
        for a in range(1,n+1):              #for all visited nodes:
            if G.nodes[a]['visited']==1:        
                L.extend(list(G.adj[a]))    #add adjacent nodes to L
        L.sort()                            #put nodes in ascending order
        for b in L:                         #starting with smallest node:
            if G.nodes[b]['visited']!=1:    #if node hasn't been visited
                find_smallest_color(G,b)    #assign smallest viable color
                break                       #next iteration


def find_smallest_color(G,i):
    n=len(G.nodes())                        #number of nodes
    l=list(G.adj[i])                        #list of adjacent nodes
    c=[]
    for int in l:
        c.append(G.nodes[int]['color'])     #adding colors of adjacent nodes to c
    t=1
    while t in c:
        t+=1
    G.nodes[i]['color']=t                   #vertex assigned smallest colour not in c and marked visited
    G.nodes[i]['visited']=1                 #vertex marked visited


def greedy(G):
    n = len(G.nodes())                      #number of nodes
    global kmax
    global visited_counter                  
    for i in range(1,n+1):                  #for all nodes in graph:
        find_next_vertex(G)                 #assign smallest viable color
    L=list(G.nodes())                       #list of all nodes
    C=[]
    for int in L: 
        C.append(G.nodes[int]['color'])     #adding colors of all nodes to C
    kmax=max(C)                             #kmax is the largest color in C
    print()                                 #the following code was provided
    for i in G.nodes():
        print('vertex', i, ': color', G.node[i]['color'])
    print()
    print('The number of colors that Greedy computed is:', kmax)
    print()


print('Graph G1:')
G=graph1.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)


print('Graph G2:')
G=graph2.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)


print('Graph G3:')
G=graph3.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)


print('Graph G4:')
G=graph4.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)


print('Graph G5:')
G=graph5.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)
