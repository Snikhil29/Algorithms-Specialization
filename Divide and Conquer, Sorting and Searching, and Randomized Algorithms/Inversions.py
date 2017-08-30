NUMLIST_FILENAME = 'S:\\Algorithms\\c1\\IntegerArray.txt'
inFile = open(NUMLIST_FILENAME, 'r')

with inFile as f:
    numList = [int(integers.strip()) for integers in f.readlines()]

count = 0


def inversionsCount(x):
    global count
    midsection = len(x) / 2
    leftArray = x[:midsection]
    rightArray = x[midsection:]
    if len(x) > 1:
        inversionsCount(leftArray)
        inversionsCount(rightArray)
        i, j = 0, 0
        a = leftArray;
        b = rightArray
        for k in range(len(a) + len(b) + 1):
            if a[i] <= b[j]:
                x[k] = a[i]
                i += 1
                if i == len(a) and j != len(b):
                    while j != len(b):
                        k += 1
                        x[k] = b[j]
                        j += 1
                    break
            elif a[i] > b[j]:
                x[k] = b[j]
                count += (len(a) - i)
                j += 1
                if j == len(b) and i != len(a):
                    while i != len(a):
                        k += 1
                        x[k] = a[i]
                        i += 1
                    break
    return x

inversionsCount(numList)
print count