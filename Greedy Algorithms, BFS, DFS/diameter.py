import networkx as nx
import random as rd
import graph6
import graph7
import graph8
import graph9
import graph10


def max_distance(G):
    n=len(G.nodes())                                #number of nodes
    L=[]
    for a in range(1,n+1):                          #for all starting nodes
        for b in range(a+1,n+1):                    #for all ending nodes(except previous starting nodes)
            for c in range(1,n+1):                  #reset all nodes
                G.nodes[c]['visited']=0             
                G.nodes[c]['label']=0 
            G.nodes[a]['visited']=1                 #BFS
            l=[]
            t=0
            while b not in l:
                t+=1                                    
                for x in range(1,n+1):     
                    if G.nodes[x]['visited']==1:        
                        l.extend(G.adj[x])              
                for y in l:                             
                    if G.nodes[y]['visited']!=1:        
                        G.nodes[y]['visited']=1         
                        G.nodes[y]['label']=t           
            L.append(G.nodes[b]['label'])           #add output to list
    return(max(L))                                  #returns largest output


print()
G6=graph6.Graph()
print('The diameter of G6 (i.e. the maximum distance between two vertices) is:', max_distance(G6))
print()


G7=graph7.Graph()
print('The diameter of G7 (i.e. the maximum distance between two vertices) is:', max_distance(G7))
print()


G8=graph8.Graph()
print('The diameter of G8 (i.e. the maximum distance between two vertices) is:', max_distance(G8))
print()


G9=graph9.Graph()
print('The diameter of G9 (i.e. the maximum distance between two vertices) is:', max_distance(G9))
print()


G10=graph10.Graph()
print('The diameter of G10 (i.e. the maximum distance between two vertices) is:', max_distance(G10))
print()
