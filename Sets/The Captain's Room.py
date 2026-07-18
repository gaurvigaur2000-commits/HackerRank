# k = int(input("No. of members in each family: "))
# rooms = list(map(int, input("Room nos.: ").split()))
# dict1={}
# 
# for i in rooms:
#     if i not in dict1:
#         dict1[i]=1
#     else:
#         dict1[i]+=1

# print("Captain's Room is", end=" ")

# for rooms, count in dict1.items():
#     if count==1:
#         print(rooms)

k = int(input("No. of members in each family: "))
rooms = list(map(int, input("Room nos.: ").split()))
unique_rooms = set()
duplicate_rooms = set()
for i in rooms:
    if i not in unique_rooms:
        unique_rooms.add(i)
    else:
        duplicate_rooms.add(i)

captain_room = unique_rooms.difference(duplicate_rooms)

print("Captain's Room is", end=" ")
print(*captain_room)