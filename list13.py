c=[19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
i=0
a=[]
b=[]
y=[]
while i<len(c):
    c1=0
    j=0
    while j<len(c):
        if c[i]==c[j]:
            b.append(c[j])
            c1=c1+1
        j=j+1
    k=0
    while k<len(c):
        if c[i] not in a:
            a.append(c[i])
            # print((c[i]),"times",c1)
            y.append([c[i],c1])
        k=k+1
    i=i+1
print(y)        