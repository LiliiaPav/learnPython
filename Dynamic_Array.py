# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
temp=raw_input()
temp= map (int, temp.strip().split())
N=temp[0]
Q=temp[1]
LastAns=0
S={}
for i in xrange(N):
    S[i]=[]

for line in sys.stdin:
    line = map (int, line.strip().split())
    ind=((line[1] ^ LastAns) % N)
    if line[0]==1:
        S[ind] = S[ind]+[line[2]]
        #print ind, S[ind], line[2]
    elif line[0]==2:
        #print ind, len(S[ind])
        value= line[2]%len(S[ind])
        LastAns=S[ind][value]
        print LastAns

'''
Sample Input

2 5
1 0 5
1 1 7
1 0 3
2 1 0
2 1 1

n = number of sequence lastAns=0 q = number of query sequences S0={} S1={} S2={} . . . Sn={}
for queries type (1) 1 x y index of sequence id = (x^lastAns)%n append y in Si-th sequence
(2) 2 x y index of sequence id = (x^lastAns)%n lastAns = valueAt(y%(size of Si-th sequence)) and pint lastAns
'''