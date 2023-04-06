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
        self.file_label = tk.Label(self, text="Choose an Excel file:")
        self.file_label.pack(padx=20, pady=10)

        self.choose_file_button = tk.Button(self, text="Choose file", command=self.choose_file)
        self.choose_file_button.pack(padx=20, pady=10)

        self.column_label = tk.Label(self, text="Choose a column:")
        self.column_label.pack(padx=20, pady=10)

        self.column_var = tk.StringVar()
        self.column_menu = tk.OptionMenu(self, self.column_var, "")
        self.column_menu.pack(padx=20, pady=10)

        self.read_button = tk.Button(self, text="Read column", command=self.read_column)
        self.read_button.pack(padx=20, pady=10)

        self.quit_button = tk.Button(self, text="Quit", command=self.quit)
        self.quit_button.pack(padx=20, pady=10)

    def choose_file(self):
        filename = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
        self.file_label.config(text="Chosen file: " + filename)
        self.data = pd.read_excel(filename)

        # Update the column menu with the column names from the new file
        self.column_var.set("")
        self.column_menu['menu'].delete(0, 'end')
        for column_name in self.data.columns:
            self.column_menu['menu'].add_command(label=column_name, command=tk._setit(self.column_var, column_name))

    def read_column(self):
        column_name = self.column_var.get()
        column_data = self.data[column_name]
        print(column_data)

        self.column_var.set("")

    def quit(self):
        self.master.destroy()

root = tk.Tk()
app = ExcelReader(master=root)
app.mainloop()