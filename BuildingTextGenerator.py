import random
import string

def enter(x):
    temp=[]
    i=1
    while x>0:
        x-=1
        elem=input ('What %1d letter do you want? Enter "v" for vowels, "c" for consonants, "l" for any letter: '%(i))
        i+=1
        temp.append(elem)
    return temp

full=string.ascii_lowercase
vowels = 'aeiouy'
consonants='bcdfghjklmnpqrstvwxz'
try:
    N=int(input ('Enter a lenght of name '))
    L=int(input ('How many names do you want '))
except:
    print("Error!")

if N>0:
    listLet=enter(N)
    while L>0:
        res=''
        for elem in listLet:
            if elem=='v':
                res+=random.choice(vowels)
            elif elem=='l':
                res+=random.choice(full)
            elif elem=='c':
                res+=random.choice(consonants)
            else:
                res+=elem
        print(res)
        L-=1
