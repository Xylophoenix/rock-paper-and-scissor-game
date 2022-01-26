import random

print("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors :- ")
choice = int(input())
random_rock = ["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""", """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""", """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""]
rock = random_rock[0]
paper = random_rock[1]
scissors = random_rock[2]
if choice == 0:
    print(rock)
    random_rock = random.choice(random_rock)
    if random_rock == rock:
        print(rock)
        print("Draw!")
    elif random_rock == paper:
        print(paper)
        print("You lose!")
    elif random_rock == scissors:
        print(scissors)
        print("You win!")
elif choice == 1:
    print(paper)
    random_rock = random.choice(random_rock)
    if random_rock == rock:
        print(rock)
        print("You win!")
    elif random_rock == paper:
        print(paper)
        print("Draw!")
    elif random_rock == scissors:
        print(scissors)
        print("You lose!")
elif choice == 2:
    print(scissors)
    random_rock = random.choice(random_rock)
    if random_rock == rock:
        print(rock)
        print("You lose!")
    elif random_rock == paper:
        print(paper)
        print("You win!")
    elif random_rock == scissors:
        print(scissors)
        print("Draw!")
else:
    print("Invalid input")
    print("Please try again")