#Command + /

#with open('fileToTest.txt', 'w') as myfile:
#    myfile.write('Sally Smith\n')

#append to the file
#with open ('fileToTest.txt', 'a') as myfile:
#    myfile.write('Mark Jacobson\n')


#with open ('file.txt', 'r') as myfile:
#    test=myfile.readlines()
#    print(len(test))

# with open ('file.txt', 'r') as myfile:
#     for line in myfile:
#         print(line, end='')
#     print()

# employees=['Sally Smith', 'Mark Jacobson']
# with open ('fileToTest.txt', 'w') as myfile:
#     for emp in employees:
#         myfile.write(emp+'\n')
    

# with open ('file.txt', 'r') as myfile:
#     result=[]
#     text=myfile.read()
#     text=text.split()
#     for i in text:
#         if len(i)==5:
#             result.append(i)

#     print(len(result))


import os

# # get the current working directory
# currentDir = os.getcwd()
# print(f"Files in the directory: {currentDir}")
# for file in  os.listdir(currentDir):
#     print(file)

 
currentDir = os.getcwd()
fileToWork = input(r"Enter file name: ")
fileToWork=os.path.join(currentDir, fileToWork)
if os.path.isfile(fileToWork):
    with open (fileToWork, 'r') as myfile:
        for line in myfile:
            print(line, end='')
else:
    print(f"File {fileToWork} doesn't exist")


# accounts=[[100, 'Mary', 34.58], 
#           [200, 'Alison', 345.67], 
#           [300, 'Marc', 3.00], 
#           [400, 'Zoltar', -32.16], 
#           [500, 'Kathleen', 24.32]]

# with open ('accounts.txt', 'w') as myfile:
#     for acc in accounts:
#         text = str(acc[0]) +' '+acc[1]+' '+ str(acc[2])
#         myfile.write(text+'\n')
# with open ('accounts.txt', 'r') as myfile:
#      for line in myfile:
#         print(line, end='')

# result=[]
# with open ('accounts.txt', 'r') as myfile:
#     for line in myfile:
#         temp = line.split(' ')
#         if 'Zoltar' in temp:
#             i=0
#             while i < len(temp):
#                 if temp[i]=='Zoltar':
#                     temp[i]='Robert' 
#                 i += 1
    
#         result.append(' '.join(temp))
#     result=''.join(result)
#     print(result)

# with open('tempfile.txt', 'w') as myfile:
#     myfile.write(result)

# os.remove("accounts.txt")
# os.rename('tempfile.txt', "accounts.txt")




# path=os.path.join(currentDir, fileToWork)

# line.replace












    



