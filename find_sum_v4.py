import tkinter as tk
from tkinter import filedialog,messagebox
from tkinter import ttk
import pandas as pd
import numpy as np
import math
import time
import threading

version = 'Excel_Sum_Finder v0.4'
pub_date = '2023/04/11'

# class ExcelReader(tk.Frame):
class ExcelReader(tk.Tk):
    def __init__(self):
        super().__init__()
        # self.master = master
        self.initUI()
        # self.pack()
        self.create_widgets()

    def initUI(self):
        self.title(version)
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
        self.output_info = tk.Label(self, text=("Info: Author: Mark Lin YL - " + pub_date))
        self.output_info.pack(padx=20, pady=10)
        
        self.file_label = tk.Message(self, text="1.Choose an Excel file:",aspect=400)
        self.file_label.pack(padx=20, pady=10)

        self.choose_file_button = tk.Button(self, text="Choose file", command=self.choose_file)
        self.choose_file_button.pack(padx=20, pady=10)
        self.first_choose = False      
    #UI complete process-2**************
    def UI_process2(self,process,len):
        self.progressbar['value'] = int(process*100/(len+1))
        self.update_idletasks()
        complete = int(process*100/len+1)
    #UI complete process-1**************
    def update_progress_label(self):
        return f"Current Progress: {self.progressbar['value']}%"
    def UI_process(self, process,len):
        if self.progressbar['value'] <= 100:
            self.progressbar['value'] = int(process*100/(len+1))+1
            self.value_label['text'] = self.update_progress_label()
            self.update_idletasks()
            complete = int(process*100/len+1)
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
        self.selected_option.set("Closest")
        # Create the radio buttons
        self.radio_button_0 = tk.Radiobutton(self, text="Equal", variable=self.selected_option, value="Equal" )
        self.radio_button_1 = tk.Radiobutton(self, text="Closest", variable=self.selected_option, value="Closest" )
        # Pack the radio buttons
        self.radio_button_0.pack()
        self.radio_button_1.pack()

        #add Label
        self.press_label = tk.Label(self, text="5.Press Readcolumn button below")
        self.press_label.pack(padx=20, pady=10)
        #add buttons
        self.is_searching = False
        self.read_button = tk.Button(self, text="Readcolumn", command=self.searching_thread)
        self.read_button.pack(padx=20, pady=10)
        self.first_choose = True
        #add Processbar
        self.progressbar = ttk.Progressbar(self, orient="horizontal", length=300, mode="determinate")
            # label
        self.value_label = ttk.Label(self, text=self.update_progress_label())        
        self.progressbar.pack(pady=10)
        self.value_label.pack(pady=10)
    
    def timercount_start(self):
        self.start_time = time.time()
    def timercount_stop(self):
        self.end_time = time.time()
        elapsed_time = round(self.end_time - self.start_time, 3)
        return elapsed_time
    #Algorithm1 : find equal to target sum 
    def subset_sum_indices(self,arr, target_sum):
        n = len(arr)
        dp = [[None for j in range(target_sum+1)] for i in range(n+1)]
        for i in range(n+1):
            dp[i][0] = []
        for i in range(1, n+1):
            #UI complete process
            self.UI_process(i,n)
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
    #Algorithm2
    def find_closest_sum(self,arr, target_sum):
        #mark add
        self.closest_equal = False
        self.taget_sum = target_sum
        self.closest_sum = 0
        self.closest_compose_v =[]
        self.closest_compose_row =[]
        
        n = int(len(arr))
        dp = [[False for j in range(target_sum + 1)] for i in range(n + 1)]
        dp[0][0] = True
        closest_sum = None
        for i in range(1, n + 1):
            #UI complete process
            self.UI_process(i,n)
            
            for j in range(target_sum + 1):
                i = int(i)
                j = int(j)
                if arr[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][ int(j - arr[i - 1]) ]
                if dp[i][j] and (closest_sum is None or abs(target_sum - j) < abs(target_sum - closest_sum)):
                    closest_sum = j
        closest_sum = int(closest_sum)
        if closest_sum == target_sum:
            # print("The target sum can be obtained exactly.")
            self.closest_equal = True 
        else:
            # print(f"The closest sum to the target is {closest_sum}.")
            self.closest_sum = closest_sum
        #sum components in array
        # print("The components of the closest sum are:")

        i = n
        j = closest_sum
        while i > 0 and j > 0:
            if dp[i - 1][j]:
                i -= 1
            else:
                # print(int(arr[i - 1]))
                print(arr[i - 1])
                # self.closest_compose_v.append(int(arr[i - 1]))
                self.closest_compose_v.append(arr[i - 1])
                self.closest_compose_row.append(i + 1)
                j -= int(arr[i - 1])
                i -= 1  
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
        if self.closest_compose_v is not None:
                result_s_title      = "Result_"
                result_s_equal      = "Equal  = "
                result_s_target_sum = "Target = " + str(self.taget_sum) 
                result_s_cloest     = "Cloest = "
                result_s_compose    = "Values = "
                result_s_compose_row    = "Rows = "
                
                if(self.closest_equal):
                    result_s_equal += "Yes"
                else:
                    result_s_equal += "No"
                    result_s_cloest += str(int(self.closest_sum))
                print("self.result = " ,  self.closest_compose_v, " type = ", type(self.closest_compose_v))
                result_s_compose += str(self.closest_compose_v)
                result_s_compose_row += str(self.closest_compose_row)
                
                time_spent = self.timercount_stop()
                if(self.closest_equal):
                    messagebox.showinfo( result_s_title , result_s_equal+ "\r\n" +result_s_target_sum+ "\r\n"  +result_s_compose+ "\r\n\r\n" +result_s_compose_row+ "\r\n"+ str(self.timediff) + " seconds" )      
                else:
                    messagebox.showinfo( result_s_title , result_s_equal+ "\r\n" +result_s_target_sum+ "\r\n" +result_s_cloest+ "\r\n" +result_s_compose+ "\r\n\r\n" +result_s_compose_row+ "\r\n"+ str(self.timediff) + " seconds" )      
        else:
            end_text = "Excel NOT found"
            messagebox.showinfo('Result', end_text)
    #button functions
    def choose_file(self):
        try:
            self.erase_error_alert()
            self.filename = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
            if self.filename == "":
                return 1
            if self.first_choose == False:
                self.UI_button()
            self.file_label.config(text="1.Chosen file: " + self.filename)
            #old one
            # self.data = pd.read_excel(self.filename)
            self.data = pd.read_excel(self.filename).replace(np.nan, 0)
            self.data = self.data.astype('int')
            # Update the column menu with the column names from the new file
            self.column_var.set("")
            # self.column_menu.destroy()
            self.column_menu['menu'].delete(0, 'end')
            for column_name in self.data.columns:
                self.column_menu['menu'].add_command(label=column_name, command=tk._setit(self.column_var, column_name))
        except FileNotFoundError:
            #Alert user to choose File first
            print("FileNotFoundError: no file been choose")
    def read_column(self):
        try:
            #start time count
            self.timercount_start()
            self.erase_error_alert()
            #renew excel column selected name
            self.selected_option.get()
            self.selected_column = self.column_var.get()
            self.column_data = self.data[self.selected_column]
            # print("self.column_data = ",self.column_data)
            length = len(self.column_data)
            #input: target sum
            self.taget_sum = self.taget_sum_entry.get()
            self.taget_sum = int(self.taget_sum)
            print("self.taget_sum=",self.taget_sum)
            self.is_searching = True
            #from Select Option List, choose different algorithm
            if(self.selected_option.get() == "Equal"):
                #find equal to target sum 
                self.result = self.subset_sum_indices(self.column_data, self.taget_sum)
                self.timediff = self.timercount_stop()
                self.show_result_equal()
            elif(self.selected_option.get() == "Closest"):
                #find not equal but most close to target sum 
                self.result = self.find_closest_sum(self.column_data, self.taget_sum)
                self.timediff = self.timercount_stop()
                self.show_result_close()
            self.is_searching = False
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
    def searching_thread(self):
        if(self.is_searching==False):
            # Start searching in a separate thread
            search_thread = threading.Thread(target=self.read_column)
            search_thread.start()
        else:
            messagebox.showwarning('Warning', "Please wait until current process done!")
if __name__ == '__main__':
    app = ExcelReader()
    app.mainloop()
