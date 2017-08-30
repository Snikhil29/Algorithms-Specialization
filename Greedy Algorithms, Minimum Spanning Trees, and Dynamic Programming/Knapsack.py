lines = [map(int, x.split(' ')) for x in open("S://Algorithms//c3//knapsack1.txt", 'r').read().split('\n')[:-1]]

capacity = lines[0][0]
items = lines[1:]

subproblems = []
subproblems.append([0 for cap in range(capacity + 1)])

for i, item in enumerate(items):
    subproblem = []
    for cap in range(capacity + 1):
        subproblem.append(max(subproblems[i][cap], subproblems[i][cap - item[1]] + item[0] if cap - item[1] >= 0 else 0))
    subproblems.append(subproblem)

print subproblems[-1][-1]