import os, tkinter

import tkinter as tk
from tkinter import filedialog, IntVar
from doctest import master
      
class EntryWithPlaceholder(tk.Entry):
    def __init__(self, master=None, placeholder="PLACEHOLDER", color='grey'):
        super().__init__(master)

        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']

        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)

        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def foc_in(self, *args):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color

    def foc_out(self, *args):
        if not self.get():
            self.put_placeholder()
       
def filesselected():
    
    files = filedialog.askopenfilenames()
    increment = 0
    from datetime import date 

    try:
        increment = 0+ int(startnumber.get()) 
    except ValueError:
        pass  
    
    textbefore = textbeforeview.get()
    textafter = textafterview.get()

    if textbefore == "Text before file name":
        textbefore = ""
    if textafter == "Text after file name":
        textafter = ""
        
      for x in files:
        os.renames(x, x+"temp")
       
    for x in files:
        increment += 1
        stringit = str(increment)
        filepath = os.path.dirname(x)
        filenameonly = os.path.basename(x).split('.')[0]
        extension = os.path.splitext(x)[1]
        if keep.get() == 0:
            try:
                os.renames(x+"temp", filepath+"/"+textbefore+textafter+ stringit + extension)
            except OSError:
                os.renames(x+"temp", filepath+"/"+textbefore+textafter+ stringit +"-DUBLICATE"+ extension)
                print ('caught')
        
        else:
            try:
                os.renames(x+"temp", filepath+"/"+textbefore+filenameonly+textafter+ stringit + extension)
            except OSError:
                os.renames(x+"temp", filepath+"/"+textbefore+filenameonly+textafter+ stringit +"-DUBLICATE"+ extension)
                print ('caught')
           
window = tk.Tk()
window.title("Bulk rename tool")    
root = window 
textbeforeview = EntryWithPlaceholder(root, "Text before file name")
textafterview = EntryWithPlaceholder(root, "Text after file name")
startnumber = EntryWithPlaceholder(root, "Start numbering from")
keep = IntVar()

def hide():
    if keep.get() == 0:
        textafterview.pack_forget()
    else:
        textafterview.pack(0)
        
radiobutton = tk.Checkbutton (master, command=hide, text="Keep old name", variable=keep, onvalue=1, offvalue=0)

        
radiobutton.grid(row = 0, column = 1, padx = 10)
textbeforeview.grid(row = 0, column = 0)
textafterview.grid(row = 0, column = 2, padx = 10)
startnumber.grid(row=0 , column = 4, padx = 10)
  
button = tk.Button(
    text="Choose files",
    width = 25,

    command=filesselected
)
button.grid(row = 1, columnspan=5)

##window.iconbitmap(r'LINK TO ICON HERE')
window.resizable(False, False)
window.mainloop()

