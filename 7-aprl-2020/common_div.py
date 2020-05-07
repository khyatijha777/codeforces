a = input()
b = input()
i =1
count = 0
while i<=len(a):
    l = len(a)/len(a[:i])
    if int(l) == l:
        if a[:i]*int(l) ==a:
            l = len(b)/len(a[:i])
            # print("l : ", l)
            if int(l) == l:
                if a[:i]*int(l)==b:
                    count+=1
    i+=1
    
print(count)