# Import necessary packages
from tkinter import *
from PyPDF2 import PdfFileReader, PdfFileWriter

# Initializing the root window
win  = Tk()
win.title("PDF_Encrypter")
win.geometry("700x200")

# Initialising Frames inside the main window
names = Frame(win, width = 100, relief = RIDGE)
names.pack(side = LEFT, padx= 10)
entries = Frame(win, width = 300, relief = RAISED)
entries.pack(side = RIGHT, padx= 10)

# Input names
path_name = Label(names, text = "Drop file path here: ", font= ("ubuntu", 16))
path_name.grid(row = 0, column= 0)
pass_name = Label(names, text = "Enter new password: ", font= ("ubuntu", 16))
pass_name.grid(row = 1, column= 0)
space = Label(names, text = " ", font= ("ubuntu", 16))
space.grid(row = 3, column= 0)

file_name = Label(names, text = "Enter a new name for the file: ", font = ("ubuntu", 16))
file_name.grid(row = 2, column = 0)

# Variables Entry
path_entry = Entry(entries, fg = "#252525", bg = "#a1a1a1", font = ("ubuntu", 18), borderwidth= 5)
path_entry.grid(row = 0, column= 0, padx= 5)
pass_entry = Entry(entries, bg = "#252525", fg = "#a1a1a1", font = ("ubuntu", 18), borderwidth= 5)
pass_entry.grid(row = 1, column= 0, padx = 5)
# Creating a new  file

file_entry = Entry(entries, fg = "#252525", bg = "#a1a1a1", font = ("ubuntu", 18), borderwidth= 5)
file_entry.grid(row = 2, column = 0, padx = 5)

# Getting the input into a variable
path = path_entry.get()
pword = pass_entry.get()

# THE LOGIC PART (FUNCTION)
def enc(path, pword, newfile):
    # Initializing output object
    out = PdfFileWriter()

    # Reading the file at the path
    file = PdfFileReader(path)
    num = file.numPages

    # Iterating through the file, one page at a time
    for pg in range(num):
        page = file.getPage(pg)
        # Adding the pages to the output object
        out.addPage(page)
    
    # Encrypting the output obejct (file)
    out.encrypt(pword)
    
    # adding the output object to a new file
    with open(newfile, "wb") as f:
        out.write(f)

    # Printing the result
    res = Label(names, text = "File Encrypted!\nRemember the password", font = ("ubuntu", 14), fg = "#05ff00")
    res.grid(row= 4, column=0)


# Encrypt button
enc_btn = Button(entries, bg = "#f10000", fg = "#fff", text = "Encrypt", font = ("ubuntu", 16), borderwidth= 5, width = 23, 
                                        activebackground= "#f0f000", activeforeground= "#ff0000",
                                    command= lambda:enc(path_entry.get(), pass_entry.get(), file_entry.get()))
enc_btn.grid(row = 3, column= 0)

# Lets's not forget..,
win.mainloop()

