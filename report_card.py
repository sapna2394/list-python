report card nested list
a=[
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65],
    [95, 45, 78],
    [87,67,49,68,88]
] 
i=0
sum=0
while i<len(a):
    j=0
    s=0
    while j<len(a[i]):
        s=s+a[i][j]
        j=j+1
    sum=sum+s    
    i=i+1
print(sum)    