print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")


choice1 = input("You found a pink corridor with apple and a banana icon on each path. Which path will you choose? type 'apple' or 'banana'\n").lower()
if choice1=="apple":
          choice2 = input("Your path is blocked by a muddy water. Will you swim or wait? type 'swim' or 'wait'\n").lower()
          if choice2=="wait":
                    choice3 = input("Three magic door suddenly appeared please choose wisely. type 'red', 'blue' or 'yellow'\n").lower()
                    if choice3=="yellow":
                              print("You've found the treasure. You win!")
                    elif choice3=="red":
                                        print("Burned by fire. Game Over.")
                    elif choice3=="blue":
                              print("Eaten by blue ogres. Game Over")
                    else:
                              print("The doors disappeared and a giant meteor is on your way. Game Over.")
          else:
                    print("A mudshark suddenly attacked you. Game over.")
elif choice1=="banana":
          print("A hole suddenly appeared in the ground. You fell into the hole. Game over.")
else:
          print("You've made a bad decision and ultimately killed you. Game over.")