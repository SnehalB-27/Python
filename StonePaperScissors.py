import random

User_win = 0
Computer_win = 0

options = ["stone", "paper","scissors"]
# 0=Stone, 1=Paper, 2=Scissors

while True:
    user_input = input("Enter Stone/Paper/Scissors Or Q to quit the game: ").lower()

    if user_input == "q":
       break

    if user_input not in options:
       continue
    
    random_number = random.randint(0,2)
    computer_choice = options[random_number]
    print("Computer picked", computer_choice)
    
    if user_input == computer_choice:
        print("Game tied")

    elif user_input == "paper" and computer_choice == "stone":
       print("You Won") 
       User_win +=1

    elif user_input == "scissors" and computer_choice == "paper":
       print("You Won") 
       User_win +=1

    elif user_input == "stone" and computer_choice == "scissors":
       print("You Won")
       User_win +=1
    else:
       print("Compuer Won")
       Computer_win +=1

print("User win", User_win, "Games")
print("Computer win", Computer_win, "Games")
