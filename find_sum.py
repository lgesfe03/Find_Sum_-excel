#2023/04/03 22:43 v0

#************************Part1 : search for sum************************
def subset_sum_indices(arr, target_sum): 
    n = len(arr)
    dp = [[None for j in range(target_sum+1)] for i in range(n+1)]
    for i in range(n+1):
        dp[i][0] = []
    for i in range(1, n+1):
        for j in range(1, target_sum+1):
            if arr[i-1] <= j:
                prev_subset = dp[i-1][j]
                if prev_subset is not None:
                    dp[i][j] = prev_subset
                else:
                    prev_subset = dp[i-1][j-arr[i-1]]
                    if prev_subset is not None:
                        dp[i][j] = prev_subset + [i-1]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][target_sum]

# #Part1-1 
# arr = [3, 34, 4, 12, 5, 2]
# target_sum = 18
# result = subset_sum_indices(arr, target_sum)
# if result is not None:
#     print("Subset found:", [arr[i] for i in result])
# else:
#     print("No subset found")


#************************Part2 : import data from excel************************
# import pandas as pd
# #Input
# excel_filename  = 'example.xlsx'
# excel_sheetname = 'Sheet1'
# excel_columnname = 'ColumnB'
# # Read the Excel file
# df = pd.read_excel(excel_filename, sheet_name = excel_sheetname)
# # Extract the column as a NumPy array
# column_array = df[excel_columnname].to_numpy()
# print(type(column_array))
# print("Column" )
# print(column_array )



# #************************Part3 combination************************
# target_sum = 28
# result = subset_sum_indices(column_array, target_sum)
# if result is not None:
#     print("Excel Subset found:", [column_array[i] for i in result])
# else:
#     print("Excel No subset found")

#************************Part4 UserInterface choose reading file************************
import tkinter as tk
from tkinter import filedialog
import pandas as pd

# Create a GUI window
root = tk.Tk()
root.withdraw()
# Create a GUI window to choose a column
column_window = tk.Toplevel(root)
column_window.title("Choose a column")
# # Ask the user to choose an Excel file
# file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])

# # Read the Excel file into a pandas DataFrame
# df = pd.read_excel(file_path)
# # Get a list of column names from the DataFrame
# column_names = list(df.columns)
# # Create a GUI window to choose a column
# column_window = tk.Toplevel(root)
# column_window.title("Choose a column")
# # Create a dropdown menu to select a column
# column_var = tk.StringVar(column_window)
# column_dropdown = tk.OptionMenu(column_window, column_var, *column_names)
# column_dropdown.pack(padx=20, pady=10)


# # Create a label to display instructions
# label = tk.Label(column_window, text="Type a number:")
# label.pack(padx=40, pady=40)
# # Create an entry widget for the user to type a number
# entry = tk.Entry(column_window)
# entry.pack(padx=40, pady=40)


# Add a button to import the selected excel file
def import_excel():
    # Ask the user to choose an Excel file
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])

    # Read the Excel file into a pandas DataFrame
    df = pd.read_excel(file_path)
    # Get a list of column names from the DataFrame
    column_names = list(df.columns)
   
    # Create a dropdown menu to select a column
    column_var = tk.StringVar(column_window)
    column_dropdown = tk.OptionMenu(column_window, column_var, *column_names)
    column_dropdown.pack(padx=20, pady=10)


    # Create a label to display instructions
    label = tk.Label(column_window, text="Type a number:")
    label.pack(padx=40, pady=40)
    # Create an entry widget for the user to type a number
    entry = tk.Entry(column_window)
    entry.pack(padx=40, pady=40)

# Add a button to read the selected column
def read_column():
    input_number = entry.get()
    input_number = int(input_number)
    print("The entered number is:", input_number)

    selected_column = column_var.get()
    column_data = df[selected_column]
    # target_sum = 28
    result = subset_sum_indices(column_data, input_number)
    if result is not None:
        print("Excel Subset found:", [column_data[i] for i in result])
    else:
        print("Excel No subset found")

#add button for import file
import_button = tk.Button(column_window, text="1.Select excel file", command=import_excel)
import_button.pack(padx=20, pady=10)

#add button for analyze excel
read_button = tk.Button(column_window, text="3.Read and Find in column", command=read_column)
read_button.pack(padx=20, pady=20)

# Display the column window
column_window.mainloop()

