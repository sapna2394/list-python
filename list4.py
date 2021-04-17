# take 10 user input print the same no. on line and reverse it.
i=0
a=[]
while i<10:
    n=int(input("enter the number"))
    i=i+1
    a.append(n)
print(a)
b=len(a)-1
c=[]
while b>=0:
    c.append(a[b])
    b=b-1
print(c)        