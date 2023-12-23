import pandas as pd
from scipy.constants import pi

url_lab1 = 'https://raw.githubusercontent.com/AnudipAE/DANLC/master/radius_data.csv'
radius_data = pd.read_csv(url_lab1)

radius_data['Area'] = pi * (radius_data['radius'] ** 2)

print("Lab 1 Output - First 5 Records:")
print(radius_data.head())

radius_data.to_csv('area_data.csv', index=False)