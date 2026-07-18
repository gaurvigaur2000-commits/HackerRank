st="BANANA"
vowels="AEIOU"
Kevin_score=0
Stuart_score=0

for i in range(len(st)):
    
    if st[i] in vowels:
        Kevin_score+=len(st)-i
    else:
        Stuart_score+=len(st)-i

print("Kevin score: ", Kevin_score, "\nStuart score: ", Stuart_score)

if Kevin_score>Stuart_score:
    print("Kevin is Winner!!")

elif Kevin_score<Stuart_score:
    print("Stuart is Winner!!")

else:
    print("Draw Game")

