n = int(input())
db = {}
names = []
for _ in range(n):
    names.append(input())
for name in names:
    if db.get(name, 0):
        print(name+"{}".format(db[name]))
        db[name]+=1
    else:
        print("OK")
        db[name] = 1
        