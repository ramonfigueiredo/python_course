import pandas as pd

# Reading data from a CSV file into a DataFrame
df = pd.read_csv('data/data_name_age.csv')

# Writing DataFrame to an Excel file
df.to_excel('data/data_name_age.xlsx', index=False)