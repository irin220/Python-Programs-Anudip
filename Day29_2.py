import pandas as pd

data = {
    'Region': ['East', 'Central', 'Central', 'Central', 'West', 'East', 'Central', 'Central', 'West', 'East',
               'Central', 'East', 'East', 'East', 'Central', 'East', 'Central', 'East', 'East', 'Central',
               'Central', 'East', 'Central', 'Central', 'East', 'West', 'Central', 'Central', 'East', 'Central',
               'East', 'Central', 'Central', 'West', 'West', 'Central', 'Central', 'Central', 'Central', 'East'],
    'Manager': ['Martha', 'Hermann', 'Hermann', 'Timothy', 'Timothy', 'Martha', 'Hermann', 'Hermann', 'Douglas', 'Martha',
                'Hermann', 'Martha', 'Douglas', 'Martha', 'Douglas', 'Martha', 'Hermann', 'Martha', 'Douglas', 'Martha',
                'Douglas', 'Martha', 'Timothy', 'Douglas', 'Martha', 'Timothy', 'Hermann', 'Martha', 'Martha', 'Douglas',
                'Martha', 'Timothy', 'Timothy', 'Douglas', 'Martha', 'Timothy', 'West', 'Central', 'Hermann', 'Hermann',
                'Martha'],
    'Salesman': ['Alexander', 'Shelli', 'Luis', 'David', 'Stephen', 'Alexander', 'Steven', 'Luis', 'Michael', 'Alexander',
                 'Sigal', 'Diana', 'Karen', 'Alexander', 'John', 'Alexander', 'Sigal', 'Alexander', 'Karen', 'David',
                 'John', 'Alexander', 'David', 'John', 'Alexander', 'Stephen', 'Luis', 'Steven', 'Diana', 'David',
                 'Alexander', 'Karen', 'David', 'Stephen', 'Michael', 'Steven', 'Luis', 'Luis', 'Steven', 'Stephen',
                 'David'],
    'Item': ['Television', 'Home Theater', 'Television', 'Cell Phone', 'Television', 'Home Theater', 'Television',
             'Television', 'Television', 'Home Theater', 'Television', 'Home Theater', 'Home Theater', 'Television',
             'Desk', 'Video Games', 'Home Theater', 'Cell Phone', 'Cell Phone', 'Video Games', 'Television', 'Video Games',
             'Home Theater', 'Home Theater', 'Home Theater', 'Desk', 'Television', 'Cell Phone', 'Television', 'Home Theater',
             'Home Theater', 'Video Games', 'Television', 'Home Theater', 'Video Games', 'Video Games', 'Video Games',
             'Desk', 'Television', 'Cell Phone', 'Home Theater', 'Television', 'Home Theater', 'Home Theater'],
    'Units': [95, 50, 36, 27, 56, 60, 75, 90, 32, 60, 90, 29, 81, 35, 2, 16, 28, 64, 15, 96, 53, 80, 46, 87, 4, 7, 50,
              66, 96, 53, 80, 50, 74, 46, 87, 4, 7, 76, 57, 14, 11, 94, 28],
    'Unit_price': [1198, 500, 1198, 225, 1198, 500, 1198, 1198, 1198, 500, 1198, 500, 500, 1198, 125, 58.5, 500, 225,
                   225, 58.5, 1198, 58.5, 500, 500, 500, 1198, 500, 1198, 225, 1198, 500, 1198, 58.5, 225, 58.5, 1198,
                   500, 225, 500, 500, 500, 500, 58.5, 1198, 225, 500, 1198, 500, 500],
    'Sale_amt': [113810, 25000, 43128, 6075, 67088, 30000, 89850, 107820, 38336, 30000, 107820, 14500, 40500, 41930,
                 250, 936, 14000, 14400, 3375, 5616, 80266, 4329, 23000, 43500, 2000, 3500, 107820, 79068, 21600, 63494,
                 40000, 625, 3627, 3217.5, 2457, 375, 8386, 17100, 28500, 16772, 5500, 47000, 14000],
}

df = pd.DataFrame(data)

pivot_table = pd.pivot_table(df, values='Units',
                                  index='Item',
                                  aggfunc='sum').reset_index()

print("\nLab 2 Output:")
print(pivot_table)