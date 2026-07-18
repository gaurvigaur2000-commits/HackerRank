lst = list(map(int, input("Enter elments: ").split()))
op = int(input("No. of operations: "))

print("Enter operation to perform on the list: ")

for _ in range(op):
    cmd = input().split()
    
    if cmd[0] == "insert":
        i = int(input("Enter index: "))
        lst.insert(i, int(cmd[1]))
        print(lst)    
    
    elif cmd[0] == "append":
        lst.append(int(cmd[1]))
        print(lst)
    
    elif cmd[0] == "remove":
        lst.remove(int(cmd[1]))
        print(lst)
    
    elif cmd[0] == "pop":
        lst.pop()
        print(lst)
    
    elif cmd[0] == "sort":
        lst.sort()
        print(lst)
    
    elif cmd[0] == "reverse":
        lst.reverse()
        print(lst)
    
    else:
        print("Wrong input!!")