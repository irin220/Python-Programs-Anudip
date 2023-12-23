# Q1.  Write a Python program to traverse a given list in reverse order, and print the elements with the original index. 


list = ['red', 'green', 'white', 'black']
print("Original list: ", list)

print("\nReversed list: ", list[::-1])

print("\nReversed list with original index: ")
for i in range(len(list)-1, -1, -1):
    print(i, list[i])

