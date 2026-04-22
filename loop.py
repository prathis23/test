#--------while loop---------
#break in while loop
# while True :
#     num = int (input("Enter number"))
#     if num == 0 :
#         break 
#     print("You enter number :" , num)

# continue (skip) in while loop

# i = 0

# while i < 5:
#     i+= 1

#     if i == 3:
#        continue
#     print(i)

#password system

# password = ""
 
# while password != "1234":
#    password= input("enter the password : ")
# print("Access Granted")

# number guessing game
# secret = 7
# while True :
#     guess = int(input("Guess the number :"))

#     if guess == secret :
#         print("Correct !")
#     elif guess > secret :
#         print(" too high")
#     else : 
#         print("too low")

# balance = 100000


# correct_username = "admin"
# correct_password = "1234"

# attempts = 3

# while attempts > 0:
#     username = input("Enter username: ")
#     password = input("Enter password: ")

#     if username == correct_username and password == correct_password:
#         print("Login successful")
#         break
#     else:
#         attempts -= 1
#         print("Invalid credentials")
#         print("Attempts left:", attempts)

# if attempts == 0:
#     print("Account locked")
# import time
# import random

# otp = random.randint(1000, 9999)
# print("OTP:", otp)

# start_time = time.time()

# user_otp = int(input("Enter OTP: "))

# if time.time() - start_time <= 30:
#     if user_otp == otp:
#         print("Verified ✅")
#     else:
#         print("Wrong OTP ❌")
# else:
#     print("OTP expired ⏰")
# while True:
#     print("\n 1. check balance") 
#     print("2. withdraw")
#     print("3. exit")

    # choice = int(input("enter the choice : "))

    # if choice == 1:
    #     print("balance :", balance)

    # elif choice == 2:
    #     amount = int(input("enter the amount: "))
    #     if amount <= balance:
    #         balance -= amount
    #         print("withdraw sucessfully")
    #     else: 
    #         print("insufficient balance")
    # elif choice == 3 :
    #     print("thank you !!")
    #     break
    # else: 
    #     print("invaild choice")
  
# data = [2, 3.4 , "prathis" , "Amulu" ,23]
# i=0
# n= len(data)
# while i <n:
#     print(data[i])
#     i += 1

#-------------FOR LOOP-----------
#1.range in for loop
# for i in range(5):
#   print(i)
#2.loop start and end
# for i in range(1 , 6):
#  print(i)

#2.loop with step
# for i in range (1 , 10, 2):
#     print(i)

#3.for loop in numbers

# number = [10 , 20 , 30]
# for num in number :
#     print (num)

# for ch in "python":
#     print(ch)


# print num 1 to 10
# for num in range(0 ,11):
#     print(num)

#print even number 1 to 20
# for number in range(1 , 20) :
#     if number % 2 == 0:
#       print(number)

# data = [2 , 2.5 , "amulu"]
# for value in data:
#     print(value)

