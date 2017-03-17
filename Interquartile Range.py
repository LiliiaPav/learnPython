'''
The interquartile range of an array is the difference between its first (Q1) and third (Q3) quartiles.

Given an array, X, of N integers and an array, F, representing the respective frequencies of X's elements,
construct a data set, S, where each Xi occurs at frequency Fi.
Then calculate and print 's interquartile range, rounded to a scale of 1 decimal place (i.e., 12.3 format).
'''

def med(N, X):

    if N%2==0:
        temp=int(N/2)
        median=(X[temp-1]+X[temp])/2
    else:
        temp=int(N/2)
        median=X[temp]
    return median


N=int(input())
X=input()
X=X.split()
X=list(map(int, X))

F=input()
F=F.split()
F=list(map(int, F))
temp=[]
for i in range(N):
    rep=F[i]
    while rep>0:
        temp.append(X[i])
        rep-=1
X=temp

X.sort()
N=len(X)
m=int(N/2)
if N%2==0:
    L=X[0:m+1]
    U=X[m+1:]
else:
    L=X[0:m]
    U=X[m+1:]

medianX=float(med(N, X))
medianL=float(med(m, L))
medianU=float(med(m, U))

print (round(medianU, 1)-round(medianL, 1))

'''

N=5
X= [6, 12, 8, 10, 20]
F=[5, 4, 3, 2, 1]'''
