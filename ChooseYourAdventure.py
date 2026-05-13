user_name = input("Enter Your Name: ")
print("Welcome", user_name, "to the adventure!")

answer = input("You are on the dirt road, and it has come to end, you can go to left or rigth, on which side want to go? ").lower()

if answer == "right":
    answer = input('''You come to Ravenhill Town.
                   Suddenly, you hear a faint whisper:
                   “Don’t trust the bell…”
                   What do you do? Will you trust or ignore?''').lower()
    if answer == "trust":
        print("DONG... DONG... DONG...You will never escape from here")
    elif answer == "ignore":
        print("Yay, You escaped!!")
    else:
        print("Not a valid option, You lose")

elif answer == "left":
    answer = input('''You step into Blackwood Forest.
                   A deer standing perfectly still, staring at you
                   Then the deer speaks.
                   What do you do? "Talk to the deer" or "Run deeper into the forest"''').lower()
    if answer == "Talk to the deer":
        print("Great! You will get the golden gate which will take you to your place")
    elif answer == "Run deeper into the forest":
        print("If you go into the forest, you will get lost.")
    else:
        print("Not a valid option, You lose")

print("Thank You for Playing")