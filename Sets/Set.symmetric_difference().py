English={23, 67, 33, 78, 89, 90, 1, 20, 22}
French={10, 1, 67, 31, 89, 2, 22, 45, 66, 77}

final_set=English.symmetric_difference(French)

print("No. of students not in both: ", len(final_set))


