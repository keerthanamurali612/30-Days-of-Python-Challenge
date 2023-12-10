print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("Who  developed Python? ")
if answer.lower() == "guido van rossum":
    print(f"Correct! Let's move on next questions")
    score += 1
else:
    print("Incorrect!")

answer = input("Who  developed C? ")
if answer.lower() == "denish ritchie":
    print(f"Good Job! Let's move on next questions")
    score += 1
else:
    print("Incorrect!")

answer = input("Who  developed JAVA? ")
if answer.lower() == "james gosling":
    print(f"Excellent! Let's move on next questions")
    score += 1
else:
    print("Incorrect!")

answer = input("What is 3*2-1 ? ")
if answer.lower() == "5":
    print(f"Correct! Let's move on next questions")
    score += 1
else:
    print("Incorrect!")

answer = input("Who  developed Javascript? ? ")
if answer.lower() == "brendan eich":
    print(f"Correct! one more questions")
    score += 1
else:
    print("Incorrect!")

answer = input("Who  developed HTML? ? ")
if answer.lower() == "tim berners lee":
    print(f"Congrats! finally finished")
    score += 1
else:
    print("Incorrect!")

print(f" You got {score} questions correct!")
print(f"You got {(score/6) *100} %")