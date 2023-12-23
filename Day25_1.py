import pandas as pd

categories = ['Groceries', 'Utilities', 'Rent', 'Transportation', 'Entertainment']
expenses = [500, 200, 1200, 300, 150]

expense_series = pd.Series(expenses, index=categories)

print(expense_series)