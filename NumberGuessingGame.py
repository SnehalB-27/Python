import random
guesses = 0
while True:
     guesses += 1
     UserInput = int(input("Your number is:"))
     if UserInput > 11:
          print("You are above the number")
          quit()

     r = random.randint(1,11)
     print("Computer's number is:", r)

     if UserInput == r:
         print("Yeah!! You guess it right")
         break
     else:
          print("You got it wrong")

print("You got it in", guesses, "guesses")