# take 10 input from user find weather number is present in list or not.
a=[]
i=0
while i<10:
    n=int(input("enter the number"))
    a.append(n)
    i=i+1
n1=int(input("ENTER THE NUMBER"))
if n1 in a:
    print("it is present in list")
else:
    print("it is not present in list")