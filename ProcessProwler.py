# This is ProcessProwler, a free and open-source application made by me.. Adrian.
# I made this to scan my task manager processes and save them into a text file.
# I created it to save the processes as a list so that I could review them later to identify any suspicious activity.


# The imports needed
import psutil  # Library for retrieving system/process information
from datetime import datetime  # Library for handling date and time
import tkinter as tk # Library for GUI
from tkinter import filedialog
#import customtkinter # Library for better GUI (can not get it to work)
from PIL import Image, ImageTk # Library for icon

def get_process_names():
    """Function to retrieve process names."""
    process_names = []
    for proc in psutil.process_iter():
        try:
            process_names.append(proc.name())
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return process_names

def write_to_file(process_names, file_path):
    """Function to write process names to a text file."""
    current_time = datetime.now()  # Gets the current date and time
    with open(file_path, 'a') as file:
        file.write(f"Date: {current_time.strftime('%Y-%m-%d')}\n")
        file.write(f"Time: {current_time.strftime('%H:%M:%S')}\n")
        file.write("Process names:\n")  # Write a header for process names
        for name in process_names:
            file.write(name + '\n')
        file.write('\n')  # Add a newline to separate entries

def run_process_and_display_message():
    """Function to run the process and display completion message."""
    # File path to save the process names
    file_path = file_path_var.get()

    try:
        # Retrieve process names
        process_names = get_process_names()

        # Write process names to a text file along with date and time
        write_to_file(process_names, file_path)

        # Display completion message
        completion_label.config(text=f"Process names have been saved to:\n{file_path}", fg="green")
    except Exception as e:
        # Display error message
        completion_label.config(text=f"An error occurred: {str(e)}", fg="red")

# Create GUI
root = tk.Tk()
root.title("Process Prowler: By Adrian") # Window Name
root.geometry("350x440") # Set Size
root.configure(bg="#1A1A1A")  # Set background color
# This will get icon for app but if not found then skip.
try:
    ico = Image.open('ProcessProwler_icon.png')
    photo = ImageTk.PhotoImage(ico)
    root.wm_iconphoto(False, photo)
except FileNotFoundError:
    print("Icon file not found. Skipping icon setting.")


# File path selection
file_path_var = tk.StringVar()
file_path_label = tk.Label(root, wraplength=300, text="Select file path to save process names:", font='Helvetica 13 bold', bg="#1A1A1A", fg="white")
file_path_label.pack(pady=6)
file_path_entry = tk.Entry(root, textvariable=file_path_var, bg="#444444", fg="white")
file_path_entry.pack(pady=6)
file_path_button = tk.Button(root, text="Browse", width=15, height=3, command=lambda: file_path_var.set(filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])), bg="#444444", fg="white")
file_path_button.pack(pady=6)

# Run button
run_button = tk.Button(root, text="Run Process Prowler", width=15, height=3, command=run_process_and_display_message, bg="#BB4143", fg="white")
run_button.pack(pady=5)

# Completion message
completion_label = tk.Label(root, text="", wraplength=300, bg="#1A1A1A", fg="white")
completion_label.pack(pady=2)

# Exit Button
exit_button = tk.Button(root, text="Exit", bg="#1A1A1A", fg="white", width=15, height=3, command=root.destroy) 
exit_button.pack(pady=6) 

# Text for How to use app title
how_to_use_title = tk.Label(root, wraplength=300, text="How To Use:", font='Helvetica 11 bold', bg="#1A1A1A", fg="white")
how_to_use_title.pack()

# Text for How to use app
how_to_use = tk.Label(root, wraplength=300, text="Click Browse -> Select or make text file -> Hit Save -> Press Run Process Prowler.", font='Helvetica 10 bold', bg="#1A1A1A", fg="white")
how_to_use.pack()

# Text for "File will saved where you saved it in browse."
where_is_file = tk.Label(root, wraplength=300, text="File will saved where you saved it in browse.", font='Helvetica 10 bold', bg="#1A1A1A", fg="white")
where_is_file.pack()


root.mainloop()

