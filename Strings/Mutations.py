st=input("Enter sring: ")

position, character = input("Enter position and character: ").split()
position = int(position)
new_st = st[:position] + character + st[position:len(st)]

print(new_st)