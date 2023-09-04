# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 18:12:00 2023

@author: User
"""

# Initial account balance
account_balance = 1000.0

# Function to display account balance
def check_balance():
    global account_balance
    print(f"Your account balance is ${account_balance:.2f}")

# Function to deposit money
def deposit():
    global account_balance
    amount = float(input("Enter the amount to deposit: $"))
    if amount > 0:
        account_balance += amount
        print(f"${amount:.2f} has been deposited successfully.")
    else:
        print("Invalid amount. Deposit failed.")

# Function to withdraw money
def withdraw():
    global account_balance
    amount = float(input("Enter the amount to withdraw: $"))
    if 0 < amount <= account_balance:
        account_balance -= amount
        print(f"${amount:.2f} has been withdrawn successfully.")
    elif amount > account_balance:
        print("Insufficient funds.")
    else:
        print("Invalid amount. Withdrawal failed.")

# Main ATM loop
while True:
    print("\nOptions:")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        check_balance()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
