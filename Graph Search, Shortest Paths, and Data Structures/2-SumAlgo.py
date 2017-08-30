
hash = {}
count = 0
input_file = open("S:\\Algorithms\\c2\\algo1-programming_prob-2sum.txt", 'r')
import os

from src.hash_table import two_sum_problem_sort, two_sum_problem_hash
from src.heap import Median


numbers = []
with open("S:\\Algorithms\\c2\\algo1-programming_prob-2sum.txt".format(base=os.getcwd())) as f:
    for line in f:
        numbers.append(int(line))

count = 0

for t in range(-10000, 10000):
    results = two_sum_problem_hash(numbers, t, distinct=True)
    if len(results) > 0:
        count += 1

print '>>>>>>>>', count # should be 427