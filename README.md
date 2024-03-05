# ProcessProwler
![ProcessProwler Img](https://raw.githubusercontent.com/Adrian-atsign-VU/ProcessProwler/main/readme%20media%20%5Bnot%20for%20app%5D/ProcessProwler.png)

**ProcessProwler** is a free and open-source application designed by Adrian to scan task manager processes and save them into a text file. This tool was created so I could see what bad things are running later on.

## How it works

ProcessProwler uses the `psutil` library to retrieve system and process information. It provides a simple GUI (Graphical User Interface) using `tkinter` for ease of use. The main functionalities include:

- **Retrieving process names:** The application retrieves the names of running processes using `psutil.process_iter()` and stores them in a list.
- **Writing to a text file:** It writes the retrieved process names along with the current date and time to a specified text file.
- **GUI for user interaction:** ProcessProwler has a basic interface.
- **Error handling:** The application handles exceptions by displaying error messages if any issues occur during the process.
- 
## Want To Add
- [ ] Add exe/app for windwos and mac users to run in one click.
- [ ] More system info at top of txt (once generated).
- [ ] Want to add html and css to style gui (python to hard and ugly for gui).
## Usage

To use ProcessProwler:

1. Run the application. (IN POWERSHELL or TERMINAL)
2. Select the file path where you want to save the process names by clicking on the "Browse" button. Name the txt and hit save.
3. Click on the "Run Process Prowler" button to start the process.
4. When done, ProcessProwler will display a message showing the success or failure of the operation along with the file path where the process names are saved.

## Dependencies

- `psutil`: Library for retrieving system/process information.
- `tkinter`: Library for GUI.
- `datetime`: Library for handling date and time.
- `Image, ImageTk`: Library for icon gui handling.

## Note

This application is developed and "maintained" by Adrian. If you encounter any issues or have suggestions for improvements, feel free to reach out or contribute to the project on [GitHub](https://github.com/Adrian-atsign-VU/ProcessProwler).

I hope and want people to use and help build this up! Enjoy.

