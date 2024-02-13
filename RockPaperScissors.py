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

#Write your code below this line 👇
game_tools = [rock, paper, scissors]
user_choice = int(input("what do you choose [type 0 for rock, 1 for paper, 2 for scissors] :- \n"))
if user_choice < 0 or user_choice > 2:
    print("Type a valid number you foool!!!!")
else:
  print(game_tools[user_choice])
  
  print("The computer choose:")
  computer_choice = random.randint(0, 2)
  print(game_tools[computer_choice])
  
  if user_choice == computer_choice:
      print("It's a Draw")
  elif user_choice == 0 and computer_choice == 1:
      print("You Lose")
  elif user_choice == 0 and computer_choice == 2:
      print("You Win")
  elif user_choice == 1 and computer_choice == 0:
      print("You Win")
  elif user_choice == 1 and computer_choice == 2:
      print("You Lose")
  elif user_choice == 2 and computer_choice == 0:
      print("You Lose")
  elif user_choice == 2 and computer_choice == 1:
      print("You Win")
  else:
      print("Type a valid number you foool!!!!")
