   
l1 = ["eat", "sleep", "repeat"]
s1 = "geek"
 
# creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)
 
print ("Return type:", type(obj1))
# print (list(enumerate(l1)))
 
# changing start index to 2 from 0
# print (list(enumerate(s1, 2)))

# for ele in enumerate(l1):
#     print (ele)


# for ele in enumerate(s1):
#     print (ele)

thestr = "Ogres are often foolhardy oafs"
newstr = ""
for i, c in enumerate(thestr):
    if c == "o":
        continue
    if i > 20:
        break
    newstr += c
print(newstr)

#Ogres are ften flh
def runtest():
    a= 2+2

print(runtest())