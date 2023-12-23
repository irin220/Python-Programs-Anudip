# Q2. Suppose you have a dataset containing daily temperature readings for a city, and you want to identify days with extreme temperature conditions. Find days where the temperature either exceeded 35 degrees Celsius (hot day) or dropped below 5 degrees Celsius (cold day).


import numpy as np

temp = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2, 4.0, 30.7, 33.3, -4.0, -12.0])
hdi = np.where(temp > 35.0)[0]
cdi = np.where(temp < 5.0)[0]

print("Hot Days\n")
print("Days \t Temperature\n")
for i in hdi:
    print(i+1, "\t  ", temp[i], "\n")

print("\nCold Days\n")
print("Days \t Temperature\n")
for i in cdi:
    print(i+1, "\t  ", temp[i], "\n")



