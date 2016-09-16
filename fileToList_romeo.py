myhand = open('D:\Programming\codes\Romeo.txt')
res=[]
lst = []
for line in myhand:
    lst = line.split()
    for i in lst:
        if i not in res:
            res.append(i)
res.sort()
print res