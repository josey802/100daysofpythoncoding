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
---'    ____)____
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
import random

hand_sign = [rock, paper, scissors]
user_input = input('What do you choose? Type 0 for Rock, 1 for paper or 2 for scissors.')
computer_input = random.choice(hand_sign)
# print(computer_input)
if user_input == '0':
  print(rock)
  print(f"Computer chose:\n{computer_input}")
  if computer_input == scissors and user_input == '0':
    print("You win.")
  elif computer_input == rock and user_input == '0':
    print(f'Draw.')
  else:
    print('You lose.')  
elif user_input == '1':
  print(paper) 
  print(f"Computer chose:\n{computer_input}") 
  if computer_input == rock and user_input == '1':
     print('You win')
  elif computer_input == paper and user_input == '1':
    print(f'Draw.')   
  else:
    print('You lose.')
elif user_input == '2':
  print(scissors)
  print(f"Computer chose:\n{computer_input}") 
  if computer_input == paper and user_input == '2':
    print('You win.')
  elif computer_input == scissors and user_input == '2':
    print(f'Draw.')  
  else:
    print('You lose.')      
else:
  print('You lose.')

                                                                       #shadow    