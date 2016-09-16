def construct_dictionary_from_lists(names_list, ages_list, scores_list):
    my_res={}
    def result(score):
        if score>=60:
            return "pass"
        else:
            return "fail"

    for elem in range( len(names_list)):
        my_res[names_list[elem]]=[ages_list[elem], scores_list[elem], result(scores_list[elem])]
    return my_res

def one_to_2D(some_list, r, c):
    res=[]
    while len(some_list)<(r*c):
        some_list.append(None)
    i=0
    for row in range(r):
        n=c
        temp=[]
        while n>0:
            temp.append(some_list[i])
            i+=1
            n-=1
        res.append(temp)
    return res

def multiplication_table(n):
    res=[]
    row=1
    while row<=n:
        #print ('___', row, res)
        my_list=[]
        for i in range (1, n+1):
            my_list.append(row*i)
        row+=1
        res.append(my_list)
    return res



print (construct_dictionary_from_lists(["paul", "saul", "steve", "chimpy"], [28, 59, 22, 5], [59, 85, 55, 60]))
#print (one_to_2D([8, 2, 9, 4, 1, 6, 7, 8, 7, 10], 2, 3) )
#print (multiplication_table(4) )