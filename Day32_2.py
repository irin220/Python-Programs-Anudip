import pandas as pd
from scipy.constants import inch

url_lab2 = 'https://raw.githubusercontent.com/AnudipAE/DANLC/master/people_heights.csv'
heights_data = pd.read_csv(url_lab2)

heights_data['Height_cm'] = heights_data['Inches'] * inch

print("\nLab 2 Output - First 5 Records:")
print(heights_data.head())

heights_data.to_csv('heights_cm_data.csv', index=False)
