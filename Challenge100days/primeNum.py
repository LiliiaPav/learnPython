#Write your code below this line 👇
def prime_checker(number):
    work=res = [int(x) for x in str(number)]
    work_len=len(work)
    #print(work)
    #print(work_len)
    #print(sum(work)%3)
    if work[work_len-1] in (0, 2, 4, 6, 8):
        print("It's not a prime number.")
    elif sum(work)%3==0:
        #print ("By 3", sum(work)%3)
        print("It's not a prime number.")
    #print (work_len)
    else:
        print("It's a prime number.")
    




#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
