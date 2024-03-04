# This is ProcessProwler, a free and open-source application made by me.. Adrian.
# I made this to scan my task manager processes and save them into a text file.
# I created it to save the processes as a list so that I could review them later to identify any suspicious activity.


# The imports needed
import psutil  # Library for retrieving system/process information
from datetime import datetime  # Library for handling date and time
import tkinter as tk # Library for GUI
from tkinter import filedialog

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
root.title("Process Prowler") # Window Name
root.geometry("300x150") # Set Size
root.configure(bg="#1A1A1A")  # Set background color

# File path selection
file_path_var = tk.StringVar()
file_path_label = tk.Label(root, text="Select file path to save process names:", bg="#1A1A1A", fg="white")
file_path_label.pack()
file_path_entry = tk.Entry(root, textvariable=file_path_var, bg="#444444", fg="white")
file_path_entry.pack()
file_path_button = tk.Button(root, text="Browse", command=lambda: file_path_var.set(filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])), bg="#444444", fg="white")
file_path_button.pack()

# Run button
run_button = tk.Button(root, text="Run Process Prowler", command=run_process_and_display_message, bg="#BB4143", fg="white")
run_button.pack()

# Completion message
completion_label = tk.Label(root, text="", bg="#1A1A1A", fg="white")
completion_label.pack()

root.mainloop()

