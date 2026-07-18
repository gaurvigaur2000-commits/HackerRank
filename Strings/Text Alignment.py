print("="*40)
print("REPORT CARD".center(40))
print("="*40)
print("Name".ljust(20)+"Marks".center(7)+"Grade".rjust(12))
print("-"*40)

data = [("Aarav", 92, "A"),
    ("Diya", 85, "B"),
    ("Krish", 78, "C"),
    ("Meera", 96, "A"),
    ("Rohan", 88, "B")]
    
for name, marks, grade in data:
    print(name.ljust(20)+ str(marks).center(8)+grade.rjust(9))

print("="*40)