set1=set(map(int, input("Enter set elements: ").split()))
print(set1)

cmd_no=int(input("Enter no. of operations to perform on the given set: "))
print("Enter operations below: ")

for _ in range(cmd_no):
    cmd=input().split()

    if cmd[0]=="discard":
        set1.discard(int(cmd[1]))
        print(set1)
    
    elif cmd[0]=="remove":
        set1.remove(int(cmd[1]))
        print(set1)
    
    elif cmd[0]=="pop":
        set1.pop()
        print(set1)


