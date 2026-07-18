set_A=set(map(int, input("Enter elements of set A: ").split()))

set_B=set(map(int, input("Enter elements of set B: ").split()))

arr=map(int, input("Enter elements of array: ").split())

happiness=0

for i in arr:
    
    if i in set_A:
        happiness+=1
    
    elif i in set_B:
        happiness+=1

print("Happiness: ", happiness)

