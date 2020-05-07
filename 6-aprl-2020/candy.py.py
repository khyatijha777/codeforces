t = int(input())
for _ in range(t):
    n = int(input())
    for k in range(2, n):
        # print("k: ", k)
        if n/(2**k-1) >0 and (n/(2**k-1))==n//(2**k-1):
            # print("kls: ",n/(2**k-1)  )
            print(n//(2**k-1))
            break