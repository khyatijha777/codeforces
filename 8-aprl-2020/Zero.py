from fractions import Fraction
from math import gcd
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
d = {"0":0}
c= 0
m = 0
for i in range(n):
    # print("a:, b", a[i], b[i])
    if  b[i]==0 and a[i] ==0:
        c+=1
        continue
    
    if a[i]==0:
        continue
    # print("inside")
    p = gcd(b[i],a[i])
    z = [b[i]/p,a[i]/p] 
    if z[0] >0 and z[1]>0:
        z[0] *=(-1)
    elif z[0] <0 and z[1]<0:
        z[1] *=(-1)
    elif z[0] >0 and z[1]<0:
        z[1] *=(-1)
    elif z[0] <0 and z[1]>0:
        z[0] *=(-1)
    else:
        pass
    z =  tuple(z)
    try:
        d[z] +=1
    except:
        d[z] = 1
    m = max(m, d[z])


# print(d)
print(m+c)
