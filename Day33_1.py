import pandas as pd

df = pd.DataFrame({
    "Math": [12, 4, 7, None, 2],
    "English": [4, 3, 57, 3, None],
    "Hindi": [20, 16, None, 3, 8],
    "Science": [14, 3, None, None, 6]
})

df_interpolated = df.interpolate()

print("Lab 1 Output:")
print(df_interpolated)