print ('Please think of a number between 0 and 100!')
low = 0
high = 100
ans = int(high + low)/2
ind = 'a'
while ind!='c':
    
    print('Is your secret number ' + str(ans) + '?')
    ind = raw_input ("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
   
    if ind == 'h':
        high = ans
        
    elif ind == 'l':
        low = ans
        
    elif ind=='c':
        break
        
    else:
        print('Sorry, I did not understand your input.')
        
    #print high
   # print lowh
    
    ans = int((high + low)/2)
    if high == 1 or low==99:
        break
    
    if int(high-low)==2:
        ans = int((high + low)/2)
        break

print(' Game over. Your secret number was: ' + str(ans) )  