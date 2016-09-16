name = "D:\Programming\codes\mbox-short.txt"
handle = open(name, 'r')
mails=[]
my_dic={}
for i in handle:
    i=i.strip()
    if i.startswith("From:"):
        i=i.split()
        my_dic[i[1]]=my_dic.get(i[1],0)+1

for i in my_dic:
    if my_dic[i]==max(my_dic.values()):
        print i, max(my_dic.values())