#2023/04/04 23:51 v4

import tkinter as tk
from tkinter import filedialog,messagebox
from tkinter import ttk
import pandas as pd
import numpy as np


# class ExcelReader(tk.Frame):
class ExcelReader(tk.Tk):
    def __init__(self):
        super().__init__()
        # self.master = master
        self.initUI()
        # self.pack()
        self.create_widgets()

    def initUI(self):
        self.title('Excel_Sum_Finder v0.3')
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
        
    def UI_button(self):
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
        self.option_label = tk.Label(self, text="4.Choose Equal / Close search below")
        self.option_label.pack(padx=20, pady=10)
        # Create a StringVar to hold the selected option
        self.selected_option = tk.StringVar()
        # Set the default option
        self.selected_option.set("Equal  ")
        # Create the radio buttons
        self.radio_button_0 = tk.Radiobutton(self, text="Equal  ", variable=self.selected_option, value="Equal  " )
        self.radio_button_1 = tk.Radiobutton(self, text="Closest", variable=self.selected_option, value="Closest" )
        # Pack the radio buttons
        self.radio_button_0.pack()
        self.radio_button_1.pack()

        #add Label
        self.press_label = tk.Label(self, text="5.Press Readcolumn button below")
        self.press_label.pack(padx=20, pady=10)
        #add buttons
        self.read_button = tk.Button(self, text="Readcolumn", command=self.read_column)
        self.read_button.pack(padx=20, pady=10)
        self.first_choose = True
        #add Processbar
        self.progressbar = ttk.Progressbar(self, orient="horizontal", length=300, mode="determinate")
        self.progressbar.pack(pady=10)
    def choose_file(self):
        try:
            self.erase_error_alert()
            self.filename = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
            if self.filename == "":
                return 1
            if self.first_choose == False:
                self.UI_button()
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
            
    #Algorithm1 : find equal to target sum 
    def subset_sum_indices(self,arr, target_sum):
        n = len(arr)
        dp = [[None for j in range(target_sum+1)] for i in range(n+1)]
        for i in range(n+1):
            dp[i][0] = []
        for i in range(1, n+1):
            self.progressbar['value'] = int(i*100/(n+1))
            self.update_idletasks()
            complete = int(i*100/n+1)
            # print(int(i*100/(n+1)))
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
    #Algorithm2 : find not equal but most close to target sum   
    def find_closest_sum(self,arr, target_sum):
        self.closest_equal = False
        # Sort the array in ascending order
        arr = np.sort(arr)
        # Initialize the closest_sum to a large positive number
        closest_sum = float('inf')
        # Iterate through all possible subsets of the array
        for i in range(2**len(arr)):
            subset = [arr[j] for j in range(len(arr)) if (i & (1 << j))]
            # Compute the sum of the current subset
            subset_sum = sum(subset)
            # If the subset sum is closer to the target sum than the current closest sum, update the closest sum
            if abs(subset_sum - target_sum) < abs(closest_sum - target_sum):
                closest_sum = subset_sum
                self.closest_sum = closest_sum
                self.closest_subset = subset
            # If we find a subset that sums up to the target sum, we can stop searching and return that subset
            if closest_sum == target_sum:
                self.closest_equal = True
                return subset
        # If no subset sums up to the target sum, return the closest sum
        return closest_sum
    #Print out result for Algorithm1
    def show_result_equal(self):
        result_s_title      = "Result_"
        result_s_equal      = "Equal = "
        result_s_target_sum = "Target = " + str(self.taget_sum) 
        result_s_cloest     = "Cloest = "
        result_s_compose    = "Values = "
        if self.result is not None:
            result_s_equal += "Yes"
            if (isinstance(self.result,np.float64)):
                #if true mean only one number
                result_s_title += "  "
                result_s_compose += int(self.result)
            elif(isinstance(self.result,list)):
                #if true means contain list number
                result_s_title += "L "
                result_s_compose += str([int(self.column_data[i]) for i in self.result]) 
            messagebox.showinfo(result_s_title, result_s_equal +"\r\n" + result_s_compose)
        else:
            result_s_title += "  "
            result_s_equal += "No"
            end_text = "Excel NOT found"
            messagebox.showinfo(result_s_title, result_s_equal +"\r\n" +end_text)
    #Print out result for Algorithm2
    def show_result_close(self):
        if self.result is not None:
                result_s_title      = "Result_"
                result_s_equal      = "Equal = "
                result_s_target_sum = "Target = " + str(self.taget_sum) 
                result_s_cloest     = "Cloest = "
                result_s_compose    = "Values = "
                if (isinstance(self.result,np.float64)):
                    #if true mean only one number
                    result_s_title += "  "
                    if(self.closest_equal):
                        result_s_equal += "Yes"
                    else:
                        result_s_equal += "No"
                        result_s_cloest += str(int(self.closest_sum))
                    result_s_compose += str([int(i) for i in self.closest_subset]) 
                elif(isinstance(self.result,list)):
                    #if true mean only one number
                    result_s_title += "L "
                    if(self.closest_equal):
                        result_s_equal += "Yes"
                    else:
                        result_s_equal += "No"
                        result_s_cloest += str(int(self.closest_sum))
                    result_s_compose += str([int(i) for i in self.result])
                if(self.closest_equal):
                    messagebox.showinfo( result_s_title , result_s_equal+ "\r\n" +result_s_target_sum+ "\r\n"  +result_s_compose+ "\r\n" )      
                else:
                    messagebox.showinfo( result_s_title , result_s_equal+ "\r\n" +result_s_target_sum+ "\r\n" +result_s_cloest+ "\r\n" +result_s_compose+ "\r\n" )      
        else:
            end_text = "Excel NOT found"
            messagebox.showinfo('Result', end_text)
    def read_column(self):
        try:
            self.erase_error_alert()
            self.selected_option.get()
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
            
            if(self.selected_option.get() == "Equal  "):
                #find equal to target sum 
                self.result = self.subset_sum_indices(self.column_data, self.taget_sum)
                self.show_result_equal()
            elif(self.selected_option.get() == "Closest"):
                #find not equal but most close to target sum   
                self.result = self.find_closest_sum(self.column_data, self.taget_sum)
                self.show_result_close()

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
            if self.taget_sum =='':
                end_text = "3.Type sum want to find first"
            else:
                end_text = "3.Type sum can ONLY type integer"
            messagebox.showwarning('Warning', end_text)
        

if __name__ == '__main__':
    app = ExcelReader()
    app.mainloop()