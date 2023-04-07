import tkinter as tk

class RadioButtonExample:
    def __init__(self, master):
        self.master = master
        master.title("Radio Button Example")

        # Create a StringVar to hold the selected option
        self.selected_option = tk.StringVar()

        # Set the default option
        self.selected_option.set("Option 1")

        # Create the radio buttons
        self.radio_button_1 = tk.Radiobutton(master, text="Option 1", variable=self.selected_option, value="Option 1")
        self.radio_button_2 = tk.Radiobutton(master, text="Option 2", variable=self.selected_option, value="Option 2")
        self.radio_button_3 = tk.Radiobutton(master, text="Option 3", variable=self.selected_option, value="Option 3")

        # Pack the radio buttons
        self.radio_button_1.pack()
        self.radio_button_2.pack()
        self.radio_button_3.pack()

        # Create a button to print the selected option
        self.print_button = tk.Button(master, text="Print Option", command=self.print_selected_option)
        self.print_button.pack()

    def print_selected_option(self):
        # Print the selected option
        print(self.selected_option.get())

root = tk.Tk()
example = RadioButtonExample(root)
root.mainloop()