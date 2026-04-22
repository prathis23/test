# 1. Even or Odd Checker
input = int(input("Enter a number: "))
if input % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

2. positive, negative, or zero
input = int(input("Enter a number: "))
if input > 0 :
    print("The number is positive.")
elif input < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

3. largest of two numbers
num = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if num > num2:
    print("The first number is larger.")
elif num < num2:
    print("The second number is larger.")
else:
    print("Both numbers are equal.")

4.Grade calculator
score = int(input("Enter the score (0-100): "))
if score >= 90:
    print("Grade: A")
elif score < 90 and score >= 70:
    print("Grade: B")
elif score < 70 and score >= 50:
    print("Grade: C")
elif score < 50 and score >= 0:
    print("Fail")
else:
    print("Invalid score. Please enter a number between 0 and 100.")

5. login system
username = input("Enter username: ")
password = input("Enter password: ")    
if username == "admin" and password == "1234":
    print ("Login successful!")
else :
        print("Invalid username or password. Please try again.")

6. ATM Withdrawal system

username = input("Enter username: ")
password = input("Enter password: ")
if username == "user" and password == "pass":
    print("login sucessful!")
    print("Welcome to the ATM!")
    balance = 10000
    print("Your current balance is: ", balance)
    withdraw = int( input("Enter the amount to withdraw: "))
    if withdraw <= balance:
        balance -= withdraw
        print("Withdrawal successful! Your new balance is: ", balance)
    else:
            print("Insufficient funds. Your current balance is: ", balance)
check_amount = withdraw // 100 
print("Withdraw amount having" , check_amount,)

7. ticket pricing system
age = int(input("Enter your age: "))
if age < 5 :
    print("You are a baby. Your ticket is free.")

elif age >= 5 and age < 18 :
        print("You are a child. Your ticket price is 100.")
elif age >= 18 and age < 60 :
        print("You are an adult. Your ticket price is 200.")
elif age >= 60 :
            print("You are a senior citizen. Your ticket price is 150.")

else :
    print("Invalid age. Please enter a valid age.")

8.Electricity bill calcula2tor
units = int(input("Enter the number of units consumed: "))
if units <= 100 :
    bill = units * 2
    print("Your electricity bill is: ", bill)
elif units > 100 and units <= 200 :
        bill =units * 5
        print("Your electricity bill is: ", bill)
elif units > 200 :
        bill = units * 10
        print("Your electricity bill is: ", bill)
else :
    print("Invalid input. Please enter a valid number of units.")
    
9. password strength checker
password = input("Enter a password: ")
if len (password) < 6 :
    print("Weak password. Password should be at least 6 characters long.")
elif len (password)>= 6 and len(password) < 10 :
    print("Medium password. Consider adding more characters or special symbols.")
elif len (password) > 10 :
        print("Strong password. Your password is secure.")
else :
    print("Invalid input. Please enter a valid password.") 

10. mini banking system 
select = int(input("welcome to the bank \n please select option below : \n 1. check balance \n  2. Deposit \n 3.withdraw \n 4.Exit \n Press the key : "))
Balance = 1000
if select== 1:
    print("Thanks for selecting option 1 \n balance ")
    print(f"your balance amount { Balance}")


elif select == 2 :
    Deposit = int (input("Enter the deposit Amount :" ))
    Balance += Deposit
    print("Your balance amount :" , Balance)


elif select == 3:
    new_withdraw= int(input(" withdraw amount : "))
    new_withdraw -= Balance
    print (f"Your withdraw amount is :{new_withdraw} \n your balance amount is : {Balance} ")
       
elif select == 4 :
   print("Thanks using using our service")

else : 
    print ( "invaild")





11. number guessing game
import random 
guess = int(input("Guess a number between 1 and 10: "))
secret_number = random.randint(1, 10)
if guess == secret_number : 
    print("Congratulations! You guessed the correct number.")
elif guess < secret_number :
    print("Too low! Try again.")    
elif guess > secret_number :
    print("Too high! Try again.")
else :
    print("Invalid input. Please enter a number between 1 and 10.")

12. Student result system

select = input("Check the result \n 1.Maths \n 2.Science \n 3.English \n Enter your choice: ")

if select == "1" :
    marks = int(input("Enter your marks in Maths: "))
    if marks >= 90 :
        print("Distanction")
    elif marks >= 60 and marks < 90 :
        print("First Class")
    elif marks >= 35 and marks < 60 :
         print("pass")
    elif marks < 35 :
        print("Fail")
    else :
        print("Invalid input. Please enter a valid mark between 0 and 100.")
elif select == "2" :
    marks = int(input("Enter your marks in Science: "))
    if marks >= 90 :
        print("Distanction")
    elif marks >= 60 and marks < 90 :
        print("First Class")
    elif marks >= 35 and marks < 60 :
         print("pass")
    elif marks < 35 :
        print("Fail")
    else :
        print("Invalid input. Please enter a valid mark between 0 and 100.")
elif select == "3" :
    marks = int(input("Enter your marks in English: "))
    if marks >= 90 :
        print("Distanction")
    elif marks >= 60 and marks < 90 :
        print("First Class")
    elif marks >= 35 and marks < 60 :
         print("pass")
    elif marks < 35 :
        print("Fail")
    else :
        print("Invalid input. Please enter a valid mark between 0 and 100.")

