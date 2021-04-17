# second max. meraki
n=[50,40,23,70,56,12,5,10,7]
i=0
mix=n[i]
while i<len(n):
    if mix<n[i]:
        mix=n[i]
    i=i+1
n.remove(mix)
j=0
mix=n[j]
while j<len(n):
    if mix<n[j]:
        mix=n[j]
    j=j+1
print(mix)
