print('''
# *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/_______/
# *******************************************************************************
# ''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
first_choice = input(("You're at a cross road. Where do you want to go?\n'Left' or 'Right'? ")).lower()
 
if first_choice == "left":
  second_choice = input("You've come to a lake. There is an island in the middle of the lake.\n" \
  "Type 'wait' to wait for a boat. Type 'swim' to swim across ").lower()
  if second_choice == "wait":
    print("A boat has come to pick you up\n" \
    "You've arrived at an unknown location.")
    third_choice = input("You've come across three doors: Red, Blue and Yellow\nWhich door will you open? ").lower()
    if third_choice == "yellow":
      print("You've entered a room full of gold. You win!")
    elif third_choice == "red":
      print("You've entered a room full of lava. Game over!")
    elif third_choice == "blue":
      print("You've entered a room full of Monsters. Game over!")
    else:
      print("You chose a door that doesn't exist. Game over!")      
  else:
    print("You got attack by crocodiles. Game over!")  
else:
  print("You've entered a Demon's Castle. Game over!")  