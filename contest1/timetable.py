d, s = list(map(int, input().split()))
m1 = []
m2 = []

for _ in range(d):
    mini, maxi = list(map(int, input().split()))
    m1.append(mini)
    m2.append(maxi)
mini_sum = sum(m1)
maxi_sum = sum(m2)

if sum(m1) <= s and sum(m2)>=s:
    print("YES")
    final = []
    next_sum = s
    m1=m1[:-1]
    m2 = m2[:-1]
    for m,n in zip(m1, m2):
        if next_sum - n >= mini_sum-n and next_sum - m <= maxi_sum-n:
            final.append(n)
            next_sum -= n
            mini_sum -=m
            maxi_sum-=n
        else:
            final.append(m)
            next_sum -= m
            mini_sum-=m
            maxi_sum-=n
    # print("next_sum", next_sum)
    final.append(next_sum)
    for i in final[:-1]:
        print(i, end=" ")
    print(final[-1], end="")

else:
    print("NO")