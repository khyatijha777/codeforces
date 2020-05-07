n, w, h = list(map(int, input().split()))
height = []
width = []
mini = 100000
for _ in range(n):
    p,q = list(map(int, input().split()))
    height.append(p)
    if p<mini:
        mini = p
    width.append(q)
chain = []
sorted_chain = []
for i in range(n):
    print("i: ", i)
    if len(sorted_chain)==0:
        sorted_chain.append([height[0], width[0]])
    else:
        for ind in range(0,len(sorted_chain)):
            print("height[ind]: ", height[ind])
            print("width[ind]: ", width[ind])
            if ind > len(sorted_chain)-1:
                sorted_chain.append( [height[ind], width[ind]])
            else:
                if height[ind]>sorted_chain[ind][0] and width[ind] >sorted_chain[ind][1]:
                    sorted_chain.insert(ind, [height[ind], width[ind]])
                    print("sorted: ", sorted_chain)
                if height[ind]==sorted_chain[ind][0] and width[ind] ==sorted_chain[ind][1]:
                    break
print(sorted_chain)