# count the number which is greater than 20 and less than 40
a=[50,40,23,70,56,12,32,33,39,5,10,7]
i=0
count=0
while i<len(a):
    if a[i]>=20 and a[i]<=40:
        count=count+1
    i=i+1
print(count)       