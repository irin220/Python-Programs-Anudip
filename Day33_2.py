import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    'Subject': ['Math', 'Physics', 'Chemistry', 'Biology'],
    'Student_A': [80, 85, np.nan, 70],
    'Student_B': [90, np.nan, 75, 85],
    'Student_C': [80, 88, np.nan, 78]
}

df_lab2 = pd.DataFrame(data)

df_lab2_interpolated = df_lab2.interpolate()

subject_wise_highest = df_lab2_interpolated.set_index('Subject').max(axis=1)

subject_wise_highest.plot(kind='bar', color='skyblue')
plt.title('Subject-wise Highest Score')
plt.xlabel('Subject')
plt.ylabel('Highest Score')
plt.show()
