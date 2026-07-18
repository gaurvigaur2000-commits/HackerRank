Set1=set(map(int, input("Enter elements of set 1: ").split()))

Set2=set(map(int, input("Enter elements of set 2: ").split()))

if Set1.issubset(Set2):
    print("True")

else:
    print("False")