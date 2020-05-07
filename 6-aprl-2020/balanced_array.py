t = int(input())
for _ in range(t):
    n = int(input())
    if (n//2)%2==0:
        print("YES")
        round = n//2
        for i in range(1, round+1):
            print(i*2, end = " ")
        for i in range(1, round):
            print(i*2-1, end = " ")
        print(round*2-1 +(round))
    else:
        print("NO")