from itertools import combinations

st, k = input("Enter string with size of combinations: ").split()
k = int(k)

st = sorted(st)

for i in range(1, k+1):
    for j in combinations(st, i):
        print("".join(j))

