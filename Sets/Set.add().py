print("Enter 7 countries name: ")
set_countries=set()

for i in range(7):
    countries=input()
    set_countries.add(countries)
    
print("Count of unique elements:", end=" ")
print(len(set_countries))