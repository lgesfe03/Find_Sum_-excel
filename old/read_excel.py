import pandas as pd
import numpy as np

# Read the Excel file
data = pd.read_excel('example20.xlsx', sheet_name='dbb').replace(np.nan, 0)
data = data.astype('int')
# data = pd.read_excel('example20.xlsx', sheet_name='dbb',na_values=0, dtype=int)

print("data=",data)

print("\r\n\r\n")

column_data = data["ColumnA1000"]

print("column_data=",column_data)

