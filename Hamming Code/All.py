import math
import numpy
import copy

def hammingGeneratorMatrix(r):
    n = 2**r-1
    pi = []
    for i in range(r):
        pi.append(2**(r-i-1))
    for j in range(1,r):
        for k in range(2**j+1,2**(j+1)):
            pi.append(k)
    rho = []
    for i in range(n):
        rho.append(pi.index(i+1))
    H = []
    for i in range(r,n):
        H.append(decimalToVector(pi[i],r))
    GG = [list(i) for i in zip(*H)]
    for i in range(n-r):
        GG.append(decimalToVector(2**(n-r-i-1),n-r))
    G = []
    for i in range(n):
        G.append(GG[rho[i]])
    G = [list(i) for i in zip(*G)]
    return G

def decimalToVector(n,r): 
    v = []
    for s in range(r):
        v.insert(0,n%2)
        n //= 2
    return v

def message(a):
    l=len(a)
    r=2
    while 2**r-2*r-1<l:
    	r+=1
    k=2**r-r-1
    b=[]
    for item in bin(l)[2:]:
        b.append(int(item))
    M=(r-len(b))*[0]+b+a+(k-r-l)*[0]
    return M

def hammingEncoder(m):
    import numpy
    r=2
    k=len(m)
    while 2**r-r-1<k:
        r+=1
    if 2**r-r-1!=k:
        return list()
    return(list(numpy.dot(m,hammingGeneratorMatrix(r))%2))

def hammingDecoder(v):
    import math
    import numpy
    import copy
    r=(math.log2(len(v)+1))
    if r%1!=0:
        return([])
    l=[]
    c=0
    while c<len(v):
        x=[]
        for i in bin(c+1)[2:]:
            x.append(int(i))
        l.append(x)
        c+=1
    for i in l:
        while len(i)<r:
            i.insert(0,0)
    e=numpy.dot(v,numpy.array(l))%2
    p=0
    for i in range(0,len(e)):
        p+=(e[i]*2**(len(e)-i-1))
    D=copy.copy(v)
    if p!=0:
        D[p-1]=(D[p-1]+1)%2
    return(D)

def messageFromCodeword(c):
    import copy
    M=[]
    r=2
    while 2**r-1<len(c):
        r+=1
    if 2**r-1!=len(c):
        return(M)
    M=copy.copy(c)
    x=0
    for i in range(0,r):
        del M[2**i-1-x]
        x+=1
    return(M)

def dataFromMessage(m):
    D=[]
    r=2
    while 2**r-r-1<len(m):
        r+=1
    if 2**r-r-1!=len(m):
        return(D)
    L=[]
    for i in range(0,r):
        L.append(m[i])
    l=0
    for i in range(0,r):
        l+=L[i]*2**(r-i-1)
    if r+l>len(m):
        return(D)
    D=m[r:r+l]
    return(D)

def repetitionEncoder(m,n):
    R=[]
    for i in (m):
        c=0
        while c<n:
            c+=1
            R.append(i)
    return(R)

def repetitionDecoder(v):
    C=[]
    if v.count(1)>v.count(0):
        C.append(1)
    elif v.count(1)<v.count(0):
        C.append(0)
    return(C)
