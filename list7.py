# even or odd in list
n=[23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
i=0
a=[]
b=[]
while i<len(n):
    if n[i]%2==0:
        a.append(n[i])
    else:
        b.append(n[i])
    i=i+1
print(a,"even")
print(b,"odd")
