#2023/04/04 23:51 v2

import tkinter as tk
from tkinter import filedialog,messagebox
import pandas as pd


# class ExcelReader(tk.Frame):
class ExcelReader(tk.Tk):
    def __init__(self):
        super().__init__()
        # self.master = master
        self.initUI()
        # self.pack()
        self.create_widgets()

    def initUI(self):
        self.title('Excel_Sum_Finder v0.1')
        # self.geometry('300x450') 

    def erase_error_alert(self):
        default_color = 'SystemButtonFace'
        try:
            self.column_menu.config(bg          = default_color )
            self.column_dropdown_text.config(bg = default_color)
            self.column_label.config(bg         = default_color)
            self.taget_sum_entry.config(bg      = default_color)
        except AttributeError:
            return 1


    def create_widgets(self):
        self.output_info = tk.Label(self, text="Info: Author: Mark Lin YL - 2023.04.06")
        self.output_info.pack(padx=20, pady=10)
        
        self.file_label = tk.Message(self, text="1.Choose an Excel file:",aspect=400)
        self.file_label.pack(padx=20, pady=10)

        self.choose_file_button = tk.Button(self, text="Choose file", command=self.choose_file)
        self.choose_file_button.pack(padx=20, pady=10)
        self.first_choose = False
        

    def choose_file(self):
        try:
            self.erase_error_alert()
            self.filename = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
            if self.filename == "":
                return 1
            if self.first_choose == False:
                # Get a list of column names from the DataFrame
                self.column_dropdown_text = tk.Label(self, text="2.choose column below")
                self.column_dropdown_text.pack(padx=20, pady=10)
                # Create a dropdown menu to select a column
                self.column_var = tk.StringVar()
                self.column_menu = tk.OptionMenu(self, self.column_var, "")
                self.column_menu.pack(padx=20, pady=10)
                #add Label
                self.column_label = tk.Label(self, text="3.Type sum want to find")
                self.column_label.pack(padx=20, pady=10)
                #add etnry space
                self.taget_sum_entry = tk.Entry(self)
                self.taget_sum_entry.pack(padx=20, pady=10)
                #add Label
                self.press_label = tk.Label(self, text="4.Press Readcolumn button below")
                self.press_label.pack(padx=20, pady=10)
                #add buttons
                self.read_button = tk.Button(self, text="Readcolumn", command=self.read_column)
                self.read_button.pack(padx=20, pady=10)
                self.first_choose = True
            self.file_label.config(text="1.Chosen file: " + self.filename)
            self.data = pd.read_excel(self.filename)
            
                # Update the column menu with the column names from the new file
            self.column_var.set("")
            # self.column_menu.destroy()
            self.column_menu['menu'].delete(0, 'end')
            for column_name in self.data.columns:
                self.column_menu['menu'].add_command(label=column_name, command=tk._setit(self.column_var, column_name))
        except FileNotFoundError:
            #Alert user to choose File first
            print("FileNotFoundError: no file been choose")
            
        
    def subset_sum_indices(self,arr, target_sum):
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
                        #has force array index change into integer
                        prev_subset = dp[i-1][int(j-arr[i-1])]
                        if prev_subset is not None:
                            dp[i][j] = prev_subset + [i-1]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n][target_sum]

    def read_column(self):
        try:
            self.erase_error_alert()
            self.selected_column = self.column_var.get()
            self.column_data = self.data[self.selected_column]
            # print("self.column_data=\r\n",self.column_data)
            # print("type=",type(self.column_data))
            length = len(self.column_data)
            # check data if 'nan' replace with 0
            for i in range(length) :
                # print("self.column_data[" , i ,"]=",self.column_data[i])
                if pd.isna(self.column_data[i]):
                    # np.isnan(self.column_data[i])
                    print(">>>>self.column_data[i] == nan")
                    self.column_data[i] = 0
                    int(self.column_data[i])
            # print("***\r\nself.column_data=",self.column_data,"\r\n***\r\n")
            # print("**type=",type(self.column_data))

            self.taget_sum = self.taget_sum_entry.get()
            self.taget_sum = int(self.taget_sum)
            print("self.taget_sum=",self.taget_sum)
            # print("type(self.taget_sum)=",type(self.taget_sum))
            
            result = self.subset_sum_indices(self.column_data, self.taget_sum)
            if result is not None:
                end_text = "Target:"+ str(self.taget_sum) + "\r\nExcel Found: " + str([int(self.column_data[i]) for i in result])          
                messagebox.showinfo('Result', end_text)
            else:
                end_text = "Excel NOT found"
                messagebox.showinfo('Result', end_text)

        except FileNotFoundError:
            #Alert user to choose certain file
            end_text = "1.Choose File First"
            messagebox.showwarning('Warning', end_text)
        except KeyError:
            #Alert user to choose column first
            # self.column_menu.config(fg = 'red')
            self.column_menu.config(bg = 'red')
            self.column_dropdown_text.config(bg = 'red')
            end_text = "2.Choose Column below First"
            messagebox.showwarning('Warning', end_text)
        except ValueError:
            #Alert user to choose column first
            self.column_label.config(bg = 'red')
            self.taget_sum_entry.config(bg = 'red')
            end_text = "3.Type sum want to find first"
            messagebox.showwarning('Warning', end_text)
        

if __name__ == '__main__':
    app = ExcelReader()
    app.mainloop()