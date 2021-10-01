import time
import numpy
import networkx as nx
import matplotlib.pyplot as plt

def WPGMA(textfile):
        start=time.time()
        mTxt=open(textfile, 'r')
        mStr=mTxt.read()
        mTxt.close()
        print(mStr)
        print()
        mLst=mStr.split()
        dim=int(numpy.sqrt(len(mLst)))
        matrix=[[0]*(dim) for i in range(0,dim)]
        G=nx.Graph()
        labels={}
        for a in range(0,dim):
                for b in range(0,dim):
                    matrix[a][b]=mLst[a+dim*b]
                    if a!=0 and b!=0:
                        matrix[a][b]=float(matrix[a][b])
        for a in range(1,dim):
                G.add_node(matrix[a][0],labels=matrix[a][0])
        for a in G.nodes():
                labels[a]=a
        while len(matrix)>2:
            small=matrix[1][2]
            x=1
            y=2
            for a in range(1,dim):
                    for b in range(1,dim):
                        if matrix[a][b]!=0 and matrix[a][b]<small:
                            small=matrix[a][b]
                            x=a
                            y=b
            matrix.extend([[0]*(dim+1)])
            for a in range(0,dim):
                matrix[a].append(0)
            matrix[0][-1]=matrix[0][x]+matrix[0][y]
            matrix[-1][0]=matrix[0][-1]
            for a in range(1,dim+1):
                matrix[a][-1]=((matrix[a][x]+matrix[a][y])/2)
                matrix[-1][a]=matrix[a][-1]
            matrix[-1][-1]=0.0
            G.add_node(matrix[-1][0])
            G.add_edge(matrix[x][0],matrix[-1][0])
            G.add_edge(matrix[y][0],matrix[-1][0])                  
            for a in range(0,dim+1):
                del matrix[a][max(x,y)]
                del matrix[a][min(x,y)]
            del matrix[max(x,y)]
            del matrix[min(x,y)]
            dim-=1
            for a in matrix:
                print(a)
            print()
        nx.draw(G,labels=labels,with_labels=True)
        plt.savefig(textfile[:-4]+'.png')
        plt.clf()
        stop=time.time()
        time_taken=stop-start
        print('Time taken: '+str(time_taken))
