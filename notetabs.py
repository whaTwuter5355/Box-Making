import tkinter as tk
from tkinter import ttk
import os
import json # Used to cleanly save multiple tabs into one file
from pathlib import Path

# 1. Initialize the application window
window = tk.Tk()
window.title("Small & Simple Notes")
window.geometry("500x400") # Made slightly larger to accommodate tabs
window.configure(bg="#08728f")

# Memory setup - changed to a JSON file to hold multiple tabs
SAVE_FILE = "my_notes_save.json"
SAVE_PATH = Path.home() / ".my_notes_save.json"

# 2. Create the Notebook (Tab Container)
notebook = ttk.Notebook(window)
notebook.pack(expand=True, fill="both", padx=10, pady=10)

# A list to keep track of our text boxes so we can save them later
text_boxes = []

def create_tab(title, content=""):
    """Helper function to generate a new tab with a scrollbar and text box."""
    # Create a frame for this specific tab
    frame = ttk.Frame(notebook)
    notebook.add(frame, text=title)
    
    # Add the vertical scrollbar
    scrollbar = ttk.Scrollbar(frame)
    scrollbar.pack(side="right", fill="y")
    
    # Create the text box
    note_box = tk.Text(frame, wrap="word", yscrollcommand=scrollbar.set)
    note_box.pack(side="left", expand=True, fill="both")
    note_box.config(bg="#ffffff", fg="#000000", font=("American Typewriter", 12), relief="solid", bd=2)
    
    # Link scrollbar to text box
    scrollbar.config(command=note_box.yview)
    
    # Insert any existing content
    note_box.insert("1.0", content)
    
    # Save the title and text box widget to our list so we can extract the text on close
    text_boxes.append((title, note_box))

def load_notes():
    """Reads the JSON save file and recreates the tabs."""
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r", encoding="utf-8") as file:
            try:
                # Load the dictionary of notes
                data = json.load(file)
                for title, content in data.items():
                    create_tab(title, content)
            except json.JSONDecodeError:
                # Fallback in case the file gets corrupted
                create_tab("Note 1")
    else:
        # Default tabs to create if no save file exists yet
        create_tab("Personal")
        create_tab("Work")
        create_tab("Ideas")
        create_tab("Code Issues")

def save_and_close():
    """Loops through all tabs, gets their text, saves to JSON, and closes."""
    data = {}
    
    # Loop through our saved list of text boxes
    for title, note_box in text_boxes:
        # Extract text and save it to the dictionary under the tab's title
        current_text = note_box.get("1.0", "end-1c")
        data[title] = current_text
        
    # Write the dictionary to a JSON file
    with open(SAVE_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
        
    # Close the application
    window.destroy()

# Intercept the window's close button
window.protocol("WM_DELETE_WINDOW", save_and_close)

# Load previous notes (or create default tabs)
load_notes()

# Start the application loop
window.mainloop()