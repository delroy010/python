import json
import os
import time as t

# Load user data from JSON file
def load_data():
    if os.path.exists('data.json'):
        with open('data.json', 'r') as file:
            return json.load(file)
    return {}  # Return an empty dictionary if the file doesn't exist

# Save user data to JSON file
def save_data(data):
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)

# Tools
def starter():
    os.system('clear')
    print("Starting Bank Simulation v2.0...\n")
    t.sleep(1)
    
    # Progress Bar Animation
    for i in range(51):
        progress = "█" * i + "-" * (50 - i)
        print(f"[{progress}] {i * 2}%")
        t.sleep(0.03)
        os.system('clear')
    
    print("System Initialized Successfully!")
    t.sleep(1)
    os.system('clear')


def shutdown():
    os.system('clear')
    print("Shutting Down Bank Simulation v2.0...\n")
    t.sleep(1)
    
    # Fade-Out Text Effect
    message = "Goodbye! All banking details have been securely saved."
    for i in range(len(message), 0, -1):
        print(message[:i])
        t.sleep(0.05)
        os.system('clear')
    
    print("System Powered Off.")
    t.sleep(1)
    os.system('clear')
    
def screen():
    os.system('clear')

class Bank:
    def __init__(self, username, name, surname, age, balance=0.0):
        self.username = username
        self.name = name
        self.surname = surname
        self.age = age
        self.balance = balance

    def getbalance(self):
        print("\n Your Current Balance: $"+str(self.balance),"\n")

    def statement(self):
        print("\n", self.name, self.surname)
        self.getbalance()

    def deposit(self, x):
        if x > 0:
            self.balance += x
            print("\n Deposit Successful!")
            self.getbalance()
        else:
            print("\n Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, x):
        if x <= self.balance and x > 0:
            self.balance -= x
            print("\n Withdrawal Successful!")
            self.getbalance()
        elif x <= 0:
            print("\n Invalid withdrawal amount. Please enter a positive value.")
        else:
            print(f"\n {self.name}, Your Account Does Not Have That Much Money.")
            self.getbalance()

def login_or_signup():
    data = load_data()

    print("Welcome to the Bank Simulation!")
    choice = input("Do you have an account? (yes/no): ").strip().lower()

    if choice == 'yes':
        username = input("Enter your username: ").strip()
        if username in data:
            print("\n Login Successful!")
            user_info = data[username]
            return Bank(username, user_info['name'], user_info['surname'], user_info['age'], user_info['balance'])
        else:
            print("\n Username not found. Please sign up first.")
            return login_or_signup()
    elif choice == 'no':
        username = input("Choose a username: ").strip()
        if username in data:
            print("\n Username already taken. Try logging in.")
            return login_or_signup()
        else:
            name = input("Enter your name: ")
            surname = input("Enter your surname: ")
            age = int(input("Enter your age: "))
            new_user = Bank(username, name, surname, age)
            data[username] = {
                "name": name,
                "surname": surname,
                "age": age,
                "balance": new_user.balance
            }
            save_data(data)
            print("\n Signup Successful!")
            return new_user
    else:
        print("\n Invalid input. Please type 'yes' or 'no'.")
        return login_or_signup()

def main():
    starter()
    user = login_or_signup()
    t.sleep(1.5)
    screen()
    while True:
        print("\n 1) Deposit     2) Statement     3) Withdraw     4) Logout")
        choice = input(f" {user.name} ~>@ ").strip()
        if choice == "1":
            screen()
            amount = float(input("Enter amount to deposit: "))
            user.deposit(amount)
        elif choice == "2":
            screen()
            user.statement()
        elif choice == "3":
            screen()
            amount = float(input("Enter amount to withdraw: "))
            user.withdraw(amount)
        elif choice == "4":
            print("\n Logging out...")
            # Save user data before logging out
            data = load_data()
            data[user.username] = {
                "name": user.name,
                "surname": user.surname,
                "age": user.age,
                "balance": user.balance
            }
            save_data(data)
            shutdown
            break
        else:
            print("\n Invalid input. Please try again.")

if __name__ == "__main__":
    main()