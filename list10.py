# find the even odd and count
n=[23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
i=0
s=0
s1=0
c=0
c1=0
while i<len(n):
    if n[i]%2==0:
        s=s+(n[i])
        c=c+1
    else:
        s1=s1+(n[i])
        c1=c1+1
    i=i+1
sum=s+s1
count=c+c1        
print(s,c,"even")
print(s1,c1,"odd")  
print(sum,count)