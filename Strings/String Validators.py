str1=input("Enter a string: ")

print(any(i.isalpha() for i in str1))
print(any(i.isalnum() for i in str1))
print(any(i.isdigit() for i in str1))
print(any(i.islower() for i in str1))
print(any(i.isupper() for i in str1))
