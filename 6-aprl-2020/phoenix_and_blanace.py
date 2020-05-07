t = int(input())
for _ in range(t):
    n = int(input())
    s1 = 0
    half = n//2
    for i in range(1, half):
        s1 += 2**i
    s1 += 2**n
    s2 = 0
    for i in range(half, n):
        s2+=2**i
        
    print(abs(s1-s2))

