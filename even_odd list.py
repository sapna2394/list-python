# check weather number is even,odd,positive,negative,zero.
a=[]
i=0
while i<5:
    n=int(input("enter the number"))
    a.append(n)
    i=i+1
    if n%2==0:
        print("it is even")
    else:
        print("it is odd")    
    if n>0:
        print("it is positive")
    elif n<0:
        print("it is negative")
    else:
        print("number is zero") 