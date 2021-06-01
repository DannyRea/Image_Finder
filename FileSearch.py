from tkinter import *
from tkinter import filedialog
from FileFinder import scanFiles, logGet
import tk as tk


def browseSource():
    # Allow user to select a directory and store it in global var
    # called folder_path

    directory = filedialog.askdirectory()
    folderSource.set(directory)


def browseDest():
    # Allow user to select a directory and store it in global var
    # called folder_path

    directory = filedialog.askdirectory()
    folderDest.set(directory)


def initCopy():
    output.insert('1.0', "Copy in progress. Please wait...\n")
    scanFiles(str(folderSource.get()), str(folderDest.get()))
    output.insert(END, "Copy complete!\n\n--------------------------RESULTS---------------------------")
    result = logGet()
    output.insert(END, '\nTOTAL FILES: ' + result[0]+'\n')
    output.insert(END, '\nRUNTIME: ' + result[1] + ' seconds\n')
    output.insert(END, '\nTOTAL FILES UNABLE TO COPY: ' + result[2]+'\n')
    output.insert(END, '\nFILES COPIED: ' + result[3].replace('\\\\', '/')+'\n')
    output.configure(state='disabled')


top = Tk()
p1 = PhotoImage(file='icon.png')
top.iconphoto(False, p1)
top.title("Image Finder & Organizer")
top.geometry("800x600")
top.resizable(False, False)
# Code to add widgets will go here...
Label(top, text='Source Folder', font=25).grid(row=0, sticky="NESW")
Label(top, text='Destination Folder', font=25).grid(row=1, sticky="NESW")
folderSource = StringVar()
folderDest = StringVar()
e1 = Entry(top, width=75, textvariable=folderSource)
e2 = Entry(top, textvariable=folderDest)
e1.grid(row=0, column=1, sticky="NESW")
e2.grid(row=1, column=1, sticky="NESW")
e1.grid_rowconfigure(1, weight=1)
e2.grid_columnconfigure(1, weight=1)
browseSrc = Button(top, text='Browse', width=25, command=browseSource)

browseDst = Button(top, text='Browse', width=25, command=browseDest)

startSearch = Button(top, text='Start Copy', width=29, command=initCopy)

output = Text(top, height=30, width=60)
browseSrc.grid(row=0, column=2)
browseDst.grid(row=1, column=2)
startSearch.grid(row=2, column=1)
output.grid(row=4, column=1)

top.mainloop()
