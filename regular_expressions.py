import re
name = "D:\Programming\codes\ActualData.txt"
handle = open(name, 'r')
my_list=[]
res=0
for i in handle:
    i=i.strip()
    y=re.findall('[0-9]+', i)
    if len(y)>0:
        my_list+=y
for i in my_list:
    num=int(i)
    res+=num

print res