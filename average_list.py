# find average
p=[2,3,6,8,9]
l=len(p)
i=0
s=0
a=0
while i<l:
    s=s+p[i]
    a=s/l
    i=i+1
print("sum",s)
print("average",a)