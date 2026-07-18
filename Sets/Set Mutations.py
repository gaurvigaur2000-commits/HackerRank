set_A=set(map(int, input("Enter elements of set A: ").split()))
operation_no=int(input("Enter no. of operations to perform: "))

for _ in range(operation_no):
    cmd=input().split()
    other_set=set(map(int,input("Enter elements: ").split()))

    if cmd[0]=="intersection_update":
        set_A.intersection_update(other_set)
        print(set_A)
    
    elif cmd[0]=='update':
        set_A.update(other_set)
        print(set_A)
    
    elif cmd[0]=="symmetric_difference_update":
        set_A.symmetric_difference_update(other_set)
        print(set_A)
    
    elif cmd[0]=="difference_update":
        set_A.difference_update(other_set)
        print(set_A)

print(sum(set_A))
