#Show the user a line of text from your favourite poem and ask for a starting and ending point. Display the characters between those two points. 

import random

def addition():
    print()

def subtraction():
    print()

def check_answer():
    print()

print("1) addition: ")

print("2) subtraction: ")

selection = int(input("Enter 1 or 2: "))

if selection == 1:
    print("Thank you")
    try_again = True
elif selection == 2:
    print("Try again")
    msg = input("Enter a message in upper case: ")
else:
    print("Try again")