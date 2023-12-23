# Q3. Write a Python program to count uppercase, lowercase, special character and numeric values in agiven string.

s = input("Enter a string: ")
u = l = sc = n = 0
for i in s:
    if i.isupper():
        u += 1
    elif i.islower():
        l += 1
    elif i.isnumeric():
        n += 1
    else:
        sc += 1
print("UpperCase: ", u, "\nLowercase: ", l, "\nNumberCase: ", n, "\nSpecialCase: ", sc)
