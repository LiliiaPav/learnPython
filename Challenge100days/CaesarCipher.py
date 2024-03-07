def encode():
    abc=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']

    message=input ("Type your message \n")
    message=message.lower()
    shift=int(input ("Type the shift number \n"))
    list_message=list(message)
    list_work=abc[shift:]+abc[0:shift]
    print(list(message))
    print(list_work)
    res=[]
    for i in list_message:
        if i in abc:
            index = abc.index(i)
            res.append(list_work[index])
        else:
            res.append(i)

    print(''.join(res))

def decode():
    abc=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
    message=input ("Type your message ").lower()
    shift=int(input ("Type the shift number "))
    res=[]
    for i in message:
        if i in abc:
            index = abc.index(i)
            
            res.append(abc[index-shift])
        else:
            res.append(i)

    print(''.join(res))
    print()

task=input();
if task=="encode":
    encode()
elif task=="decode":
    decode()
else:
    print ("I don't know this command")

again= input("Type 'yes' if you want to go again. Otherwise type 'no'")