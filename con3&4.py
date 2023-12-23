# Q3. Write a Python program to check leap year.


yr = int(input("Enter a year: "))
if(yr%400==0 or yr%4==0 and yr%100!=0):
    print(yr, "is a Leap Year.")
else:
    print(yr, "is not a Leap Year.")




# Q4. Write a Python program and using input() function take one number from the user and using ternary operators check whether the number is even or odd.


n = int(input("Enter a number: "))
print(n, "is an Even Number." if n%2==0 else "is an Odd Number.")