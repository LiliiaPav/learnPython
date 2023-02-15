#!python3
def CelsiusToFahrenheit (inp):
    with open("examlpe.txt", 'a') as writefile:
        if inp >= -273.15:
            res=float((inp * 9/5)+32)
            writefile.write (str(res)+'\n')

#temp=float(input ("Enter in Celsius "))

temperatures=[10,-20,-289,100]
for elem in temperatures:
    CelsiusToFahrenheit(elem)
