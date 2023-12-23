# Q2. Write a Python program to count and display the vowels of a given text.

s = input("Enter a string: ")
v = 0
for i in s:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        v += 1
print("Number of vowels= ", v)