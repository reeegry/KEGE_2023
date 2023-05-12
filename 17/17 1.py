# a = [1, 2, 3, 4]
# b = ['a', 'b', 'c']
# print(list(zip(a, b)))

with open('17_2400.txt') as file:
    a = list(map(int, file.readlines()))
    b = list(zip(a, a[1:]))
    c = []
    count = 0
    max_pr = -100000000
    for i, j in b:
        if i + j >= 100 and i * j < 0:
            count += 1
            max_pr = max(max_pr, i * j)

print(count, max_pr)