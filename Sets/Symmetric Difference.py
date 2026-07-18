Set1=set(map(int, input("Enter elements of set 1: ").split()))
Set2=set(map(int, input("Enter elements of set 2: ").split()))

sym_diff=Set1.symmetric_difference(Set2)

for i in sym_diff:
    print(i)