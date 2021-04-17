# total sum of even and odd
n=[23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
i=0
a=[]
b=[]
s=0
s1=0
while i<len(n):
    if n[i]%2==0:
        a.append(n[i])
        s=s+(n[i])
    else:
        b.append(n[i])
        s1=s+(n[i])
    i=i+1
print(s,"even")
print(s1,"odd")        