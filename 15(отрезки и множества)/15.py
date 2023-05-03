p = {1, 2, 7}
q = {1, 2, 4, 5, 6}


def f(x, a):
    return ((x not in a) <= (x not in p)) or (x not in q)


a = set() #set(range(1, 1000)

for x in range(1, 1000):
    if not f(x, a):
        a.add(x) #a.remove(x)

print(sorted(a))