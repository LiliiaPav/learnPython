def find(str, ch, start=0, end=0):
    if end==0:
        end=len(str)
    index=start
    while index<end:
        if str[index]==ch:
            return index
        index+=1
    return -1


print find('apple', 'e',0,3)