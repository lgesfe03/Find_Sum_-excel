import tkinter as tk
from tkinter import filedialog,messagebox
import time

def do_something():
    start_time = time.time()
    # do some time-consuming task here
    time.sleep(1)
    end_time = time.time()
    elapsed_time = round(end_time - start_time,3)
    print("Elapsed time: {:.2f} seconds<<".format(elapsed_time))
    print("elapsed_time:",elapsed_time)
    print("type(elapsed_time):",type(elapsed_time))
    messagebox.showinfo( "show time",str(elapsed_time )      )


def start_program():
    # start the program and call do_something after 2 seconds
    root.after(100, do_something)

root = tk.Tk()
root.geometry("200x100")
start_button = tk.Button(root, text="Start program", command=start_program)
start_button.pack(pady=20)
root.mainloop()