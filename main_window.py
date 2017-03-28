# -*- encoding: utf-8 -*-

from tkinter import *
from tkinter import messagebox, filedialog
import os

fileName = None

def showAuthor():
    messagebox.showinfo('Author', 'Author is ...')


def showVersionInfo():
    messagebox.showinfo('About', 'Python Notepad beta V0.1')

def openFile():
    global fileName
    fileName = filedialog.askopenfilename(defaultextension='.txt')
    if fileName:
        root.title('File: ' + os.path.abspath(fileName))
        textArea.delete(1.0, END)
        with open(fileName, 'r') as f:
            try:
                textArea.insert(1.0, f.read())
            except Exception as e:
                messagebox.showinfo('Error', 'Error while open file, cannot read file')

def saveContent():
    global fileName
    if not fileName:
        saveContentAs()
    else:
        with open(fileName, 'w') as f:
            msg = textArea.get(1.0, END)
            f.write(msg)


def saveContentAs():
    global fileName
    fileName = filedialog.asksaveasfilename(initialfile='unnamed.txt', defaultextension='.txt')
    if fileName:
        with open(fileName, 'w') as f:
            msg = textArea.get(1.0, END)
            f.write(msg)
        root.title('File: ' + os.path.abspath(fileName))

def newNote():
    global fileName
    fileName = None
    root.title('new note')
    textArea.delete(1.0, END)

def copyText():
    textArea.event_generate('<<Copy>>')

def cutText():
    textArea.event_generate('<<Cut>>')

def pasteText():
    textArea.event_generate('<<Paste>>')

def undoOperation():
    textArea.event_generate('<<Undo>>')

def redoOperation():
    textArea.event_generate('<<Redo>>')

root = Tk()
root.title('Python Notepad')
root.geometry('800x500+100+100')

# Add Menu
menuBar = Menu(root)
root.config(menu=menuBar)

# File menu
fileMenu = Menu(menuBar, tearoff=False)
fileMenu.add_command(label='New', accelerator='Ctrl + N', command=newNote)
fileMenu.add_command(label='Open', accelerator='Ctrl + O', command=openFile)
fileMenu.add_command(label='Save', accelerator='Ctrl + s', command=saveContent)
fileMenu.add_command(label='Save As', accelerator='Ctrl + Shift + S', command=saveContentAs)
menuBar.add_cascade(label='File', menu=fileMenu)

# Edit menu
editMenu = Menu(menuBar, tearoff=False)
editMenu.add_command(label='Undo', accelerator='Ctrl + Z', command=undoOperation)
editMenu.add_command(label='Redo', accelerator='Ctrl + Y', command=redoOperation)
editMenu.add_separator()
editMenu.add_command(label='Cut', accelerator='Ctrl + X', command=cutText)
editMenu.add_command(label='Copy', accelerator='Ctrl + C', command=copyText)
editMenu.add_command(label='Paste', accelerator='Ctrl + V', command=pasteText)
editMenu.add_separator()
editMenu.add_command(label='Search', accelerator='Ctrl + F')
editMenu.add_command(label='Select All', accelerator='Ctrl + A')
menuBar.add_cascade(label='Edit', menu=editMenu)

# About menu
about_menu = Menu(menuBar, tearoff=False)
about_menu.add_command(label='Author', command=showAuthor)
about_menu.add_command(label='About', command=showVersionInfo)
menuBar.add_cascade(label='About', menu=about_menu)

# Toolbar
toolBar = Frame(root, height=5, bg='grey')
buttonOpen = Button(toolBar, text='Open', command=openFile)
buttonOpen.pack(side=LEFT, padx=5, pady=2)
buttonSave = Button(toolBar, text='Save', command=saveContent)
buttonSave.pack(side=LEFT)
toolBar.pack(expand=NO, fill=X)


textPanel = PanedWindow(root, orient=HORIZONTAL, height=80)

# line number
lnLabel = Label(textPanel, width=2, bg='antique white')
# lnLabel.pack(fill=Y)
lnLabel.grid(row=0, column=0)

# text area
textArea = Text(textPanel, undo=True, width=63, font=('Consolas', 16))
# textArea.pack(expand=0, fill=BOTH)
textArea.grid(columnspan=2, row=0, column=1)

# scroll bar for text area
scrollBar = Scrollbar(textPanel, width=4)
textArea.config(yscrollcommand=scrollBar.set)
scrollBar.config(command=textArea.yview)
# scrollBar.pack(expand=0, fill=Y)
textPanel.paneconfigure(scrollBar, minsize=4)
scrollBar.grid(row=0, column=2)

textPanel.add(lnLabel)
textPanel.add(textArea)
textPanel.add(scrollBar)
textPanel.pack(expand=1, fill=BOTH)

# Status bar
status = Label(root, text='Status: ok', bd=1, relief='sunken', anchor=W)
status.pack(fill=X)

root.mainloop()
