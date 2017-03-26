# -*- encoding: utf-8 -*-

from tkinter import *
from tkinter import messagebox


def showAuthor():
    messagebox.showinfo('Author', 'Author is ...')


def showVersionInfo():
    messagebox.showinfo('About', 'Python Notepad beta V0.1')


root = Tk()
root.title('Python Notepad')
root.geometry('800x500+100+100')

# Add Menu
menuBar = Menu(root)
root.config(menu=menuBar)

# File menu
fileMenu = Menu(menuBar)
fileMenu.add_command(label='New', accelerator='Ctrl + N')
fileMenu.add_command(label='Open', accelerator='Ctrl + O')
fileMenu.add_command(label='Save', accelerator='Ctrl + S')
fileMenu.add_command(label='Save As', accelerator='Ctrl + Shift + N')
menuBar.add_cascade(label='File', menu=fileMenu)

# Edit menu
editMenu = Menu(menuBar)
editMenu.add_command(label='Undo', accelerator='Ctrl + Z')
editMenu.add_command(label='Redo', accelerator='Ctrl + Y')
editMenu.add_separator()
editMenu.add_command(label='Cut', accelerator='Ctrl + X')
editMenu.add_command(label='Copy', accelerator='Ctrl + C')
editMenu.add_command(label='Paste', accelerator='Ctrl + V')
editMenu.add_separator()
editMenu.add_command(label='Search', accelerator='Ctrl + F')
editMenu.add_command(label='Select All', accelerator='Ctrl + A')
menuBar.add_cascade(label='Edit', menu=editMenu)

# About menu
about_menu = Menu(menuBar)
about_menu.add_command(label='Author', command=showAuthor)
about_menu.add_command(label='About', command=showVersionInfo)
menuBar.add_cascade(label='About', menu=about_menu)

# Toolbar
toolBar = Frame(root, height=25, bg='grey')
buttonOpen = Button(toolBar, text='Open')
buttonOpen.pack(side=LEFT, padx=5, pady=5)
buttonSave = Button(toolBar, text='Save')
buttonSave.pack(side=LEFT)
toolBar.pack(expand=NO, fill=X)

# Status bar
status = Label(root, text='Status: ok', bd=1, relief='sunken', anchor=W)
status.pack(side=BOTTOM, fill=X)

# line number
lnLabel = Label(root, width=2, bg='antique white')
lnLabel.pack(side=LEFT, fill=Y)

# text area
textArea = Text(root, undo=True)
textArea.pack(expand=YES, fill=BOTH)

# scroll bar for text area
scrollBar = Scrollbar(textArea)
textArea.config(yscrollcommand=scrollBar.set)
scrollBar.config(command=textArea.yview)
scrollBar.pack(side=RIGHT, fill=Y)

root.mainloop()
