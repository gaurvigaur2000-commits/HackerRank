participants = int(input("Enter no. of participants: "))

score = list(map(int, input("Enter their score: ").split()))

highest_score = float('-inf')
sec_highest = float('-inf')

for i in score:
    if highest_score < i:
        sec_highest = highest_score
        highest_score = i

    elif i > sec_highest and i != highest_score:
        sec_highest = i 

print("Runner-up score: ", sec_highest)