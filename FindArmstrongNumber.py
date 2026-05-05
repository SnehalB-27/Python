number = int(input("Enter the number"))
order = len(str(number))
sum = 0
copy_n = number
while(number > 0):
    digit = number % 10
    sum += digit ** order
    number = number // 10
   

if(sum == copy_n):
        print("The number is Armstrong Number")
else:
        print("The number is not an Armstrong Number")
 
