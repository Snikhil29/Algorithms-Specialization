import sys

f = open("S://Algorithms//c3//knapsack_big.txt", 'r')
lines = f.readlines()
f.close()

W, N = map(lambda x: int(x), lines[0].split(" "))
w = [10000000]
v = [10000000]
for line in lines[1:]:
    v.append(int(line.split(" ")[0]))
    w.append(int(line.split(" ")[1]))

K = {}
sys.setrecursionlimit(2100)
def knapsack(W, N):
    global K
    if N == 0: return 0
    if (W,N) in K:
        return K[(W, N)]
    one = knapsack(W, N - 1)
    two = knapsack(W - w[N], N - 1) + v[N] if (w[N] <= W) else -1
    K[(W,N)] = max(one, two)
    return K[(W,N)]

print knapsack(W, N)