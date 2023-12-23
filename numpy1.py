# Q1. Determine which products in a store are out of stock (quantity is 0).


import numpy as np

inventory = np.array([10, 0, 5, 0, 20, 0])
oosi = np.where(inventory == 0)[0]
oosp = inventory[oosi]
print("Products at indices", np.where(inventory == 0), "are out of stock.")
print("Out of Stock Products are:", oosp)
