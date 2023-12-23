# Q4. Write a Python program and using input() function take one number from the user and using ternary operators check whether the number is even or odd.


n = int(input("Enter a number: "))
print(n, "is an Even Number." if n%2==0 else "is an Odd Number.")