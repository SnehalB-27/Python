# Kirana store Calculator And Receipt Generator
sum = 0
while(True):
    userInpt = input("Enter Item Price (Rs) Or Enter q to quit:\n")
    if(userInpt != "q"):
        sum = sum + int(userInpt)
        print(f"Your order total so far:{sum}")
    else:
        print(f"Your Cart total is:{sum}/-. Thanks for shopping with us")
        break