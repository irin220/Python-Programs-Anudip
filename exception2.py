#Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.

def acceptNum():
    try:
        x = int(input("Enter 1st number: "))
        y = int(input("Enter 2nd number: "))
        z = x+y
        print("Sum= ", z)
        
    except ValueError:
        print("Input is not a number")

acceptNum()