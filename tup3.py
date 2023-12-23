#  Write a Python program to Remove items from set1 that are not common to both set1 and set2.


set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

i= set1.intersection(set2)
print(i)