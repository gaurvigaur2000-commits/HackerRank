count=0

str1=input("Enter a string: ")
sstr=input("Enter a substring: ")

for i in range(len(str1)):

    if str1[i:i+len(sstr)]==sstr:
        count+=1

print(count)

