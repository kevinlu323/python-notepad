# -*- encoding: utf-8 -*-

from tkinter import *

root = Tk()
root.title('python notepad')
root.geometry('700x500+100+100')

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
about_menu.add_command(label='Editor')
about_menu.add_command(label='Copyright')
menuBar.add_cascade(label='About', menu=about_menu)

root.mainloop()
