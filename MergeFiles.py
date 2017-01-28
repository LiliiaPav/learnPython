import os
import datetime
path="D:\Programming\codes_python\Sample-Files"
pack=os.listdir(path)
print (pack)

def readFile (filename):
    with open(path+'\\'+ filename, 'r') as temp:
        content=temp.read()
        return content

def appendToFile (filename, cont):
    with open(filename, 'a') as tempFile:
        tempFile.write(cont+'\n')

resFile=datetime.datetime.now()
resFile=resFile.strftime("%Y-%m-%d-%H-%M-%S-%f")+'.txt'

for elem in pack:
    i=readFile (elem)
    appendToFile (resFile,i)
