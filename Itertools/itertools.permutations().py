from itertools import permutations

st, k = input("Enter string with size of permutations: ").split()
k = int(k)

res = list(sorted(permutations(st, k)))

for ele in res:
    print("".join(ele))
