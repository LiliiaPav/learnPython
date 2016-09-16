def file_to_dic(file_name):
    # Make a connection to the file
    file_pointer = open(file_name, 'r')
    # You can use either .read() or .readline() or .readlines()
    data = file_pointer.readlines()
    result={}
    for i in range(len(data)):
        line=data[i]
        if line[-1]=='\n':
            line=line[:-1]
        temp=line.split(',')
        k=temp[0]
        v=temp[1:]
        for j in range(len(v)):
            v[j]=float(v[j])
         
        result[k]=v
       
    file_pointer.close()
    return result



print (file_to_dic("D:\Programming\codes\IOtest.txt"))

'''
Mark,90,93,60,90
Abigail,84,50,72,75
Frank,46,83,53,79
Yohaan,47,77,74,96
'''
