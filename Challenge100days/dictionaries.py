data={}
while True:
    name= input ("What's your name?: ")
    bit = input ("What's your bit?: ")
    data[name] = bit
    cont= input ("Do you want to continue?( 'yes' or 'no'): ").lower()
    if cont =='no':
        break
    else:
        print('\n'*50)

list_d=list(data.values())
maxVal=max(list_d)
for x, y in data.items():
    if y==maxVal:
        print (x ,y)

#print(max(data, key=data.get))