#
score = int(input("Enter your score out of 100:"))
if (score < 35):
     print("He/She is poor student")

elif(score > 35 and score < 70):
    print("He/She is Average student")

elif(score > 70 and score <100):
    print("He/She is Good student")

else:
    print("Invalid score")
