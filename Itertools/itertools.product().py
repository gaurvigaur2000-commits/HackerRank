from itertools import product

list_A = list(map(int, input("Enter elements of list A: ").split()))
list_B = list(map(int, input("Enter elelments of list B: ").split()))

prod = list(product(list_A, list_B))

print(*prod)