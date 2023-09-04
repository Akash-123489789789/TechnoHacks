# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 18:20:36 2023

@author: User
"""

import random
import string

def generate_password(length):
    # Define characters to use in the password (letters, digits, and symbols)
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password by selecting characters randomly
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Get user-defined password length
try:
    password_length = int(input("Enter the desired password length: "))
    if password_length <= 0:
        raise ValueError("Password length should be a positive integer.")
    
    # Generate and print the random password
    password = generate_password(password_length)
    print("Generated Password:", password)

except ValueError as e:
    print("Invalid input:", e)
