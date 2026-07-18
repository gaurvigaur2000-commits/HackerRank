set_A=set(map(int, input("Enter set A: ").split()))

superset=False

set_B=set(map(int, input("Enter set B: ").split()))

if set_A > set_B:
    superset=True
    
print("Superset" if superset else "Not superset")