import threading
import time
import tkinter as tk

class App:
    def __init__(self, root):
        self.root = root
        self.start_time = None
        self.elapsed_time = tk.StringVar()
        self.elapsed_time.set("00:00:00")
        
        # Create a label to show the elapsed time
        self.time_label = tk.Label(self.root, textvariable=self.elapsed_time, font=("Helvetica", 20))
        self.time_label.pack(pady=20)

        # Create a button to start the timer
        self.start_button = tk.Button(self.root, text="Start", command=self.start_timer)
        self.start_button.pack(pady=10)

    def start_timer(self):
        # Start the timer in a separate thread
        self.start_time = time.time()
        timer_thread = threading.Thread(target=self.update_time_label)
        timer_thread.start()

    def update_time_label(self):
        while True:
            # Calculate elapsed time
            elapsed = time.time() - self.start_time
            # Update label with formatted elapsed time
            self.elapsed_time.set(time.strftime("%H:%M:%S", time.gmtime(elapsed)))
            # Update UI
            self.root.update()
            # Sleep for 100 milliseconds to prevent the timer from using too much CPU
            time.sleep(0.1)

root = tk.Tk()
app = App(root)
root.mainloop()