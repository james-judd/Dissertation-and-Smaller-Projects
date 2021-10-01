#!/usr/bin/python
import time
import sys
import numpy

def fill(seq1,seq2):
    t=-2
    u=-2
    for i in range(2,L1+2):
        backtrack[i][0]=seq1[i-2]
        backtrack[i][1]='U'
        scorematrix[i][1]=t
        t-=2
    for i in range(2,L2+2):
        backtrack[0][i]=seq2[i-2]
        backtrack[1][i]='L'
        scorematrix[1][i]=u
        u-=2
    backtrack[1][1]='x'
    for x in range(2,L1+2):
        for y in range(2,L2+2):
            score(x,y)  

def score(x,y):
    a=match(x,y)+scorematrix[x-1][y-1]
    b=scorematrix[x-1][y]-2
    c=scorematrix[x][y-1]-2
    if max(a,b,c)==a:
        backtrack[x][y]='D'
        scorematrix[x][y]=a
    if max(a,b,c)==b:
        backtrack[x][y]='U'
        scorematrix[x][y]=b
    if max(a,b,c)==c:
        backtrack[x][y]='L'
        scorematrix[x][y]=c

def match(x,y):                                                                 
    if seq1[x-2]==seq2[y-2]:                                                
        if seq1[x-2]=='A':
            return(4)                                                       
        elif seq1[x-2]=='C':
            return(3)
        elif seq1[x-2]=='G':
            return(2)
        elif seq1[x-2]=='T':
            return(1)
    else:
        return(-3)

def align(seq1,seq2):
    x=L1+1
    y=L2+1
    global string1
    global string2
    while x!=1 or y!=1:
        if backtrack[x][y]=='D':
            string1=seq1[x-2]+string1
            string2=seq2[y-2]+string2
            x-=1
            y-=1
        elif backtrack[x][y]=='U':
            string1=seq1[x-2]+string1
            string2='_'+string2
            x-=1
        elif backtrack[x][y]=='L':
            string1='_'+string1
            string2=seq2[y-2]+string2
            y-=1
            
# DO NOT EDIT ------------------------------------------------
# Given an alignment, which is two strings, display it

def displayAlignment(alignment):
    string1 = alignment[0]
    string2 = alignment[1]
    string3 = ''
    for i in range(min(len(string1),len(string2))):
        if string1[i]==string2[i]:
            string3=string3+"|"
        else:
            string3=string3+" "
    print('Alignment ')
    print('String1: '+string1)
    print('         '+string3)
    print('String2: '+string2+'\n\n')

# ------------------------------------------------------------


# DO NOT EDIT ------------------------------------------------
# This opens the files, loads the sequences and starts the timer
file1 = open(sys.argv[1], 'r')
seq1=file1.read()
file1.close()
file2 = open(sys.argv[2], 'r')
seq2=file2.read()
file2.close()
start = time.time()

#-------------------------------------------------------------

string1=''
string2=''
L1=len(seq1)
L2=len(seq2)
backtrack=[[' ']*(L2+2) for i in range(L1+2)]            
scorematrix=[[0]*(L2+2) for i in range(L1+2)]
fill(seq1,seq2)
align(seq1,seq2)
best_score=scorematrix[-1][-1]
best_alignment=string1,string2

#-------------------------------------------------------------


# DO NOT EDIT (unless you want to turn off displaying alignments for large sequences)------------------
# This calculates the time taken and will print out useful information 
stop = time.time()
time_taken=stop-start

# Print out the best
print('Time taken: '+str(time_taken))
print('Best (score '+str(best_score)+'):')
displayAlignment(best_alignment)

#-------------------------------------------------------------

