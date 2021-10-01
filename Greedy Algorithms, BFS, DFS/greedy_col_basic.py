import networkx as nx
import graph1
import graph2
import graph3
import graph4
import graph5


def find_smallest_color(G,i):
    n=len(G.nodes())                        #number of nodes
    l=list(G.adj[i])                        #list of adjacent nodes
    c=[]
    for int in l:
        c.append(G.nodes[int]['color'])     #adding colors of adjacent nodes to c
    t=1
    while t in c:
        t+=1
    G.nodes[i]['color']=t                   #vertex assigned smallest colour not in c


def greedy(G):
    global kmax
    n=len(G.nodes())                        #number of nodes
    for i in range(1,n+1):                  #for all nodes in graph:
        find_smallest_color(G,i)            #assign smallest color
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


print('Graph G1:')
G=graph1.Graph()
greedy(G)


print('Graph G2:')
G=graph2.Graph()
greedy(G)


print('Graph G3:')
G=graph3.Graph()
greedy(G)


print('Graph G4:')
G=graph4.Graph()
greedy(G)


print('Graph G5:')
G=graph5.Graph()
greedy(G)
