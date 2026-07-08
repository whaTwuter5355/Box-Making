import tkinter as tk
from tkinter import ttk

# 1. Initialize the application window
root = tk.Tk()
root.title("Small & Simple Notes")
root.geometry("400x300")

# 2. Create a frame layout to hold the text box and scrollbar
frame = ttk.Frame(root)
frame.pack(expand=True, fill="both", padx=10, pady=10)

# 3. Add the vertical scrollbar
scrollbar = ttk.Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

# 4. Create the multi-line text box and link it to the scrollbar
note_box = tk.Text(frame, wrap="word", yscrollcommand=scrollbar.set)
note_box.pack(side="left", expand=True, fill="both")

# Configure scrollbar to move the text view
scrollbar.config(command=note_box.yview)

# Start the application loop
root.mainloop()
