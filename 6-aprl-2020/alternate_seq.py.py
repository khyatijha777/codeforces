t = int(input())
for _ in range(t):
    l = int(input())
    n = list(map(int, input().split()))
    n.append("?")
    i = 0
    if n[0]>0:
        cur = 1
    else:
        cur =0
    s = 0
    while i<l:
        print("ok")
        if cur == 1:
            print("counting positive")
            temp = 0
            while n[i] != "?" and n[i]>0:
                if n[i] >temp:
                    temp = n[i]
                i+=1
            print("temp: ", temp)
            s+=temp
            print("s: ", s)
            cur = 0
        if cur == 0:
            print("counting negative")

            temp = n[i]
            while n[i] != "?" and n[i]<0:
                if n[i] >temp:
                    temp = n[i]
                    print("temp: ", temp)
                i+=1
            s+=temp
            print("s: ", s)

            cur = 1
        i+=1

    print(s)

