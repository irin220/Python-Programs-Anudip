import pandas as pd
import matplotlib.pyplot as plt

student_data = pd.DataFrame({
    'school_code': ['s001', 's002', 's003', 's001', 's002', 's004'],
    'class': ['V', 'VI', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'age': [12, 12, 13, 13, 14, 12],
    'height': [173, 192, 186, 167, 151, 159],
    'weight': [35, 32, 33, 30, 31, 32],
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4'],
})

class_counts = student_data.groupby('class')['name'].count().reset_index()

plt.bar(class_counts['class'], class_counts['name'], color='skyblue')
plt.xlabel('Class')
plt.ylabel('Number of Students')
plt.title('Number of Students in Each Class')
plt.show()

print("Number of Students in Each Class:")
print(class_counts)