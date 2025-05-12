import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

random_choice = [rock,paper,scissors]
auto_player = random.choice(random_choice)

user_choice = int(input("what do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors:"))



if(user_choice == 0):
    print("your choice:","\n")
    print(rock,"\n")

    print("auto player choice:","\n")
    print(auto_player)
    if auto_player == rock:
        print("draw")
    elif auto_player == paper:
        print("you loose")
    else:
        print("you win")


elif(user_choice == 1):
    print(paper,"\n")

    print("auto player choice:", "\n")
    print(auto_player)
    if auto_player == rock:
        print("you win")
    elif auto_player == paper:
        print("draw")
    else:
        print("you loose")

else:
    print(scissors,"\n")

    print("auto player choice:", "\n")
    print(auto_player)
    if auto_player == rock:
        print("you loose")
    elif auto_player == paper:
        print("you win")
    else:
        print("draw")

