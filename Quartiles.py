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
X.sort()

m=int(N/2)
if N%2==0:
    L=X[0:m]
    U=X[m:]
else:
    L=X[0:m]
    U=X[m+1:]

medianX=med(N, X)
medianL=med(m, L)
medianU=med(m, U)
print(int(medianL))
print (int(medianX))
print (int(medianU))
