from itertools import permutations
from itertools import combinations
# Get all permutations of [1, 2, 3]
perm = permutations([1, 2, 3])
comb = combinations([1, 2, 3], 2)
# Print the obtained permutations
for i in list(perm):
    print (i)
for i in list(comb):
    print (i)
