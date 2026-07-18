from collections import OrderedDict

item_no = int(input("Enter no. of items: "))
items = OrderedDict()

print("Enter item name and its price below: ")
total_price = 0

for _ in range(item_no):
    data = input().split()
    name = " ".join(data[:-1])
    price = int(data[-1])

    if name in items:
        items[name]+=price
   
    else:
        items[name]=price

print("\nFinal items list: ")

for names, total_price in items.items():
    print(names, total_price)