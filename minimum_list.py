print minimum
n=[34,1,45,79,2,0]
i=0
c=n[i]
while i<len(n):
    j=n[i]
    if j<c:
        c=j
    i=i+1
print(c,"minimum")