from collections import Counter 

shoe_list = list(map(int, input("Enter sizes of shoes: ").split()))
counter = Counter(shoe_list)
print(counter)

customers = int(input("Enter no. of customers: "))
print("Enter size of the shoe and its prize below: ")

total_price=0

for _ in range(customers):
    size, price = map(int, input().split())
    
    if counter[size]>0:
        total_price+=price
        counter[size]-=1

print("Profit: ", total_price)
print("Stock: ", counter)