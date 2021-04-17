a=["s","a","p","n","a"]
b=[]
i=0
c=0
while i<len(a):
    if a[i] not in b:
        c=c+1
        b.append(a[i])
    i=i+1
 print(b)        
while i<len(b):
    if a in b:
b.append(b[i])