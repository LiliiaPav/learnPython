'''
Given an array, X, of N integers and an array, W, representing the respective weights of 's elements,
calculate and print the weighted mean of X's elements.
Your answer should be rounded to a scale of 1 decimal place (i.e., 12.3 format).
'''
N=int(input())
X=input()
W=input()
X=X.split()
X=list(map(int, X))
W=W.split()
W=list(map(int, W))

res=0
for i in range(N):
    res+=X[i]*W[i]

mw=res/sum(W)
print (round(mw, 1))
