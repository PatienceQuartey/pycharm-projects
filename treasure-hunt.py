print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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

option_1 = input("You are being chased by a Tiger. Which way do you run?\n Type 'Left' or 'Right' ")
if option_1 == 'Right'.lower():
    print("You run and climbed up a tall tree to safety")
    option_2 = input("There is a branch sticking out on your left and on your right is a liana.\n "
                     "Type 'Branch' to swing off the branch or 'Liana' to swing off the Liana ")
    if option_2 == 'Liana'.lower():
        print ("You swung on the lianas to the nearest Village. safe from the Tiger")
        option_3 = input(" The Village has three entryways. Which do you go through?\n Type 'Green' for the Green Entryway"
                         " 'Blue' for the Blue Entryway or 'Red' the Red Entryway? ")
        if option_3 == "Blue".lower():
            print("Noo, you walked into the Sea Entry and drowned. Game Over")
        elif option_3 == "Green".lower():
            print("Noo, you entered the entryway with venomous snakes. You are bitten to death. Game Over")
        elif option_3 == "Red".lower():
            print("Yay you made it to the Palace and found the treasure. The Treasure is yours!!! You Win")
        else:
            print("This is not an option. You lose. Game Over")
    elif option_2 == 'Branch'.lower():
        print("The branch broke so you fell to the ground, in front of the tiger. You are eaten. Game Over")
    else:
        print("This is not an option. You lose. Game Over")

elif option_1 == 'Left'.lower():
    print("Noo. You ran into a cave of tigers. You're eaten alive. Game Over! ")

else:
    print("This is not an option. You lose. Game Over")
