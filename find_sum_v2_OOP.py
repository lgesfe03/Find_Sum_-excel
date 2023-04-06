#2023/04/04 23:51 v2

import tkinter as tk
from tkinter import filedialog
import pandas as pd


class ExcelReader(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.create_widgets()

    def create_widgets(self):
        self.output_info = tk.Label(self, text="Infomation..")
        self.output_info.pack(padx=20, pady=10)
        
        self.file_label = tk.Label(self, text="Choose an Excel file:")
        self.file_label.pack(padx=20, pady=10)

        self.choose_file_button = tk.Button(self, text="Choose file", command=self.choose_file)
        self.choose_file_button.pack(padx=20, pady=10)

        #mark add
        # Create a dropdown menu to select a column
        self.column_var = tk.StringVar(self)
        
        

    def choose_file(self):
        filename = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
        self.file_label.config(text="Chosen file: " + filename)
        self.data = pd.read_excel(filename)
        #mark add
        # Get a list of column names from the DataFrame
        self.column_names = list(self.data.columns)
        self.column_dropdown = tk.OptionMenu(self, self.column_var, *self.column_names)
        self.column_dropdown.pack(padx=20, pady=10)
        #add last buttons
        self.column_label = tk.Label(self, text="Type sum want to find")
        self.column_label.pack(padx=20, pady=10)

        self.taget_sum_entry = tk.Entry(self)
        self.taget_sum_entry.pack(padx=20, pady=10)

        self.read_button = tk.Button(self, text="Read column", command=self.read_column)
        self.read_button.pack(padx=20, pady=10)
        

    def subset_sum_indices(self,arr, target_sum): 
        n = len(arr)
        self.dp = [[None for j in range(target_sum+1)] for i in range(n+1)]
        for i in range(n+1):
            self.dp[i][0] = []
            # print("arr[" , i ,"]=",arr[i])
            # if arr[i] == 'nan':
            #     arr[i] = 0
        for i in range(1, n+1):
            for j in range(1, target_sum+1):
                if arr[i-1] <= j:
                    prev_subset = self.dp[i-1][j]
                    if prev_subset is not None:
                        self.dp[i][j] = prev_subset
                    else:
                        prev_subset = self.dp[i-1][j-arr[i-1]]
                        if prev_subset is not None:
                            self.dp[i][j] = prev_subset + [i-1]
                else:
                    self.dp[i][j] = self.dp[i-1][j]
            return self.dp[n][target_sum]    

    def read_column(self):
        self.selected_column = self.column_var.get()
        self.column_data = self.data[self.selected_column]
        print("self.column_data=",self.column_data)
        # print("type=",type(self.column_data))
        length = len(self.column_data)
        for i in range(length) :
            print("self.column_data[" , i ,"]=",self.column_data[i])
            if pd.isna(self.column_data[i]):
                # np.isnan(self.column_data[i])
                print(">>>>self.column_data[i] == nan")
                self.column_data[i] = 0.0
        print("**self.column_data=",self.column_data)
        # print("**type=",type(self.column_data))

        self.taget_sum = self.taget_sum_entry.get()
        self.taget_sum = int(self.taget_sum)
        print("self.taget_sum=",self.taget_sum)
        print("type(self.taget_sum)=",type(self.taget_sum))
        
        result = self.subset_sum_indices(self.column_data, self.taget_sum)
        if result is not None:
            end_text = "Excel Subset found:", [self.column_data[i] for i in result]
            self.output_info.config(text=  end_text)
            print("Excel Subset found:", [self.column_data[i] for i in result])
        else:
            self.output_info.config(text="Excel No subset found")
            print("Excel No subset found")
            


root = tk.Tk()
app = ExcelReader(master=root)
app.mainloop()