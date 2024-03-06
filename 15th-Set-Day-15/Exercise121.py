#Ask the user to type in a word in upper case. If they type it in lower case, ask them to try again. Keep repeating this until they type in a message all in uppercase. 

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
elif selection == 3:
    print("Thank you")
    try_again = True
elif selection == 4:
    print("Try again")
    msg = input("Enter a message in upper case: ")
elif selection == 5:
    again = "n"
else:
    print("Try again")