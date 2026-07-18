import textwrap

st, k = input("Enter string and length of substring: ").split()
k = int(k)
st=textwrap.wrap(st, k)

for ele in st:
    temp_str=""

    for char in ele:

        if char not in temp_str:
            temp_str+=char

    print(temp_str)

