n = int(input())
p = [0] * (n + 1)
for i in range(1, n + 1):
    p[i] = int(input())


def get_depth(i, acc):
    while True:
        if p[i] == -1:
            return acc
        
        i = p[i]
        acc += 1

max_depth = 0
for i in range(1, n + 1):

    max_depth = max(max_depth, get_depth(i, 0))

print(max_depth + 1)