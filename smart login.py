import json
import random
import getpass
import time
import json

{
    data =(users)
}

# Add new user
users["prathis"] = {
    "password": "2222",
    "balance": 0,
    "locked": False,
    "transactions": []
}

# Save back
with open("users.json", "w") as file:
    json.dump(users, file, indent=4)

print("User added!")
# OTP
def generate_otp():
    return random.randint(1000, 9999)

# Login system
def login(users):
    for attempt in range(3):
        username = input("Username: ")
        password = getpass.getpass("Password: ")

        if username in users:
            if users[username]["locked"]:
                print("Account is locked!")
                return None

            if password == users[username]["password"]:
                print("Login successful!")
                return username
            else:
                print("Wrong password")
        else:
            print("User not found")

    print("Too many attempts! Account locked.")
    if username in users:
        users[username]["locked"] = True
   
    return None

# OTP verification
def otp_verification():
    otp = generate_otp()
    print(f"OTP: {otp}")

    for _ in range(3):
        user_otp = input("Enter OTP: ")
        if user_otp == str(otp):
            print("OTP Verified!")
            return True
        else:
            print("Wrong OTP")

    print("OTP failed!")
    return False

# Transaction log
def add_transaction(users, username, text):
    users[username]["transactions"].append(text)
    save_users(users)

# Wallet menu
def wallet(users, username):
    while True:
        print("\n1. Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. History")
        print("5. Logout")

        choice = input("Choose: ")

        if choice == "1":
            print(f"Balance: ₹{users[username]['balance']}")

        elif choice == "2":
            amount = int(input("Deposit (100/200/500): "))
            if amount in [100, 200, 500]:
                users[username]["balance"] += amount
                add_transaction(users, username, f"Deposited ₹{amount}")
                print("Deposit successful")
            else:
                print("Invalid amount")

        elif choice == "3":
            amount = int(input("Withdraw amount: "))
            if amount <= users[username]["balance"]:
                users[username]["balance"] -= amount
                add_transaction(users, username, f"Withdrew ₹{amount}")
                print("Withdraw successful")
            else:
                print("Insufficient balance")

        elif choice == "4":
            print("\nTransaction History:")
            for t in users[username]["transactions"]:
                print("-", t)

        elif choice == "5":
            print("Logged out")
            break

        else:
            print("Invalid choice")

