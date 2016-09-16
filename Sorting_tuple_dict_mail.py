#name = raw_input("Enter file:")
name = "D:\Programming\codes\mbox-short.txt"
handle = open(name, 'r')
my_dic={}
for i in handle:
    i=i.strip()
    if i.startswith("From "):
        i=i.split()

        temp= i[5].split(':')
        #print temp[0]
        my_dic[temp[0]] = my_dic.get(temp[0],0)+1

temp=[]
for i,j in my_dic.items():
    temp.append((i,j))

temp.sort()

print temp
for i,j in temp:
    print i, j
