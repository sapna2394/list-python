# print max
n=[45,432,56,1,34,87]
i=0
c=n[i]
while i<len(n):
    j=n[i]
    if j>c:
        c=j
    i=i+1
print(c,"maximum")        
