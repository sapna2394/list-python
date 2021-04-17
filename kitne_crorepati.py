# kitne crorepati
n=[3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100] 
i=0
c=0
d=0
e=0
while i<len(n):
    if n[i]>=10000000:
        c=c+1
    elif n[i]>=100000:
        d=d+1
    elif n[i]<=100000:
        e=e+1
    i=i+1
print(c,"crorepati")
print(d,"lakhpati")
print(e,"dilwale")            
