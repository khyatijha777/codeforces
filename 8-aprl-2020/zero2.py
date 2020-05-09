from fractions import gcd
n=input()
a=list(map(float,input().split()))
b=list(map(float,input().split()))
d={}
m=0
c=0
for i in range(n):
    if a[i]!=0:
        g=gcd(a[i],b[i])
        z=(b[i]/g,a[i]/g)
        try:
            d[z]+=1
        except:
            d[z]=1
        m=max(m,d[z])
    if a[i]==0 and b[i]==0:
        c+=1
print(m+c)