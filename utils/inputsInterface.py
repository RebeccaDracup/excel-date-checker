import tkinter as tk
from tkinter import filedialog


def get_source_location():
    # Select Excel or csv file with the tabular data
    root = tk.Tk()  # Create a Tk root widget

    root.title("Source Excel")  # Add a title
    canvas1 = tk.Canvas(root, width=300, height=300,
                        bg='#FFFFFF')  # Canvas using the root widget as its parent.
    canvas1.pack()

    # Opens a Windows Explorer window
    def getexcel():
        global tablefile
        # Saves the filepath of the selected file
        tablefile = filedialog.askopenfilename()
        root.quit()

    browseButton_Excel = tk.Button(root, text='Select Excel or csv file',
                                   command=getexcel, bg='#60605F', fg='white',
                                   font=(
                                       'helvetica', 12, 'bold'))  # Button settings

    canvas1.create_window(150, 150, window=browseButton_Excel)

    root.mainloop()  # Enter the Tk event loop
    root.destroy()  # Destroy the main window when the event loop is terminated.
    return tablefile
