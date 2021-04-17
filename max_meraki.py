# max meraki
n=[50,40,23,70,56,12,5,10,7]
i=0
c=n[i]
while i<len(n):
    j=n[i]
    if j>c:
        c=j
    i=i+1
print(c,"maximum")    