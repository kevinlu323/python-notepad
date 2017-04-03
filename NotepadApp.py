from tkinter import *
from tkinter import messagebox, filedialog
from functools import partial
import os


class NotePadApp(Frame):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.pack()
        self.master.title('Python Notepad App')
        self.master.geometry('800x500+100+100')
        self.fileName = None
        self.createWidgets()

    def createWidgets(self):
        # Add Menu
        self.menuBar = Menu(self)
        self.master.config(menu=self.menuBar)

        # File menu
        self.fileMenu = Menu(self.menuBar, tearoff=False)
        self.fileMenu.add_command(label='New', accelerator='Ctrl + N', command=self.newNote)
        self.fileMenu.add_command(label='Open', accelerator='Ctrl + O', command=self.openFile)
        self.fileMenu.add_command(label='Save', accelerator='Ctrl + s', command=self.saveContent)
        self.fileMenu.add_command(label='Save As', accelerator='Ctrl + Shift + S', command=self.saveContentAs)
        self.menuBar.add_cascade(label='File', menu=self.fileMenu)

        # Edit menu
        self.editMenu = Menu(self.menuBar, tearoff=False)
        self.editMenu.add_command(label='Undo', accelerator='Ctrl + Z', command=self.undoOperation)
        self.editMenu.add_command(label='Redo', accelerator='Ctrl + Y', command=self.redoOperation)
        self.editMenu.add_separator()
        self.editMenu.add_command(label='Cut', accelerator='Ctrl + X', command=self.cutText)
        self.editMenu.add_command(label='Copy', accelerator='Ctrl + C', command=self.copyText)
        self.editMenu.add_command(label='Paste', accelerator='Ctrl + V', command=self.pasteText)
        self.editMenu.add_separator()
        self.editMenu.add_command(label='Search', accelerator='Ctrl + F', command=self.searchContent)
        self.editMenu.add_command(label='Select All', accelerator='Ctrl + A', command=self.selectAll)
        self.menuBar.add_cascade(label='Edit', menu=self.editMenu)

        # About menu
        self.about_menu = Menu(self.menuBar, tearoff=False)
        self.about_menu.add_command(label='Author', command=self.showAuthor)
        self.about_menu.add_command(label='About', command=self.showVersionInfo)
        self.menuBar.add_cascade(label='About', menu=self.about_menu)

        # Toolbar
        self.toolBar = Frame(self, height=5, bg='grey')
    def createWidgets(self):
        # Add Menu
        self.menuBar = Menu(self)
        self.master.config(menu=self.menuBar)

        # File menu
        self.fileMenu = Menu(self.menuBar, tearoff=False)
        self.fileMenu.add_command(label='New', accelerator='Ctrl + N', command=self.newNote)
        self.fileMenu.add_command(label='Open', accelerator='Ctrl + O', command=self.openFile)
        self.fileMenu.add_command(label='Save', accelerator='Ctrl + s', command=self.saveContent)
        self.fileMenu.add_command(label='Save As', accelerator='Ctrl + Shift + S', command=self.saveContentAs)
        self.menuBar.add_cascade(label='File', menu=self.fileMenu)

        # Edit menu
        self.editMenu = Menu(self.menuBar, tearoff=False)
        self.editMenu.add_command(label='Undo', accelerator='Ctrl + Z', command=self.undoOperation)
        self.editMenu.add_command(label='Redo', accelerator='Ctrl + Y', command=self.redoOperation)
        self.editMenu.add_separator()
        self.editMenu.add_command(label='Cut', accelerator='Ctrl + X', command=self.cutText)
        self.editMenu.add_command(label='Copy', accelerator='Ctrl + C', command=self.copyText)
        self.editMenu.add_command(label='Paste', accelerator='Ctrl + V', command=self.pasteText)
        self.editMenu.add_separator()
        self.editMenu.add_command(label='Search', accelerator='Ctrl + F', command=self.searchContent)
        self.editMenu.add_command(label='Select All', accelerator='Ctrl + A', command=self.selectAll)
        self.menuBar.add_cascade(label='Edit', menu=self.editMenu)

        # About menu
        self.about_menu = Menu(self.menuBar, tearoff=False)
        self.about_menu.add_command(label='Author', command=self.showAuthor)
        self.about_menu.add_command(label='About', command=self.showVersionInfo)
        self.menuBar.add_cascade(label='About', menu=self.about_menu)

        # Create a PanedWindow for all widgets
        self.parentPanel = PanedWindow(orient=VERTICAL)
        self.parentPanel.pack(expand=YES, fill=BOTH)

        # Toolbar
        self.toolBar = Frame(self.parentPanel, height=5, bg='grey')
        self.buttonOpen = Button(self.toolBar, text='Open', command=self.openFile)
        self.buttonOpen.pack(side=LEFT, padx=5, pady=2)
        self.buttonSave = Button(self.toolBar, text='Save', command=self.saveContent)
        self.buttonSave.pack(side=LEFT)
        # self.toolBar.pack(expand=YES, fill=X)
        self.parentPanel.add(self.toolBar, minsize=30)

        self.textPanel = PanedWindow(self.parentPanel, orient=HORIZONTAL)
        # self.textPanel.pack(expand=1, fill=BOTH)

        # line number
        self.lnLabel = Label(self.textPanel, width=2, bg='antique white')
        # self.lnLabel.pack(side=LEFT, fill=Y)
        # self.lnLabel.grid(row=0, column=0)

        # text area
        self.textArea = Text(self.textPanel, undo=True, font=('Consolas', 16))
        # self.textArea.pack(side=LEFT, expand=YES, fill=BOTH)
        # self.textArea.grid(row=0, column=1)

        # scroll bar for text area
        self.scrollBar = Scrollbar(self.textPanel, width=15)
        self.textArea.config(yscrollcommand=self.scrollBar.set)
        self.scrollBar.config(command=self.textArea.yview)
        # self.textPanel.paneconfigure(self.scrollBar, minsize=40)
        # self.scrollBar.pack(side=LEFT, expand=0, fill=Y)
        # self.scrollBar.grid(row=0, column=2)

        self.textPanel.add(self.lnLabel, minsize=15)
        self.textPanel.add(self.textArea, width=760, height=440)
        self.textPanel.add(self.scrollBar, minsize=15)

        self.parentPanel.add(self.textPanel)

        # Status bar
        self.status = Label(self.parentPanel, text='Status: ok', bd=1, relief='sunken', anchor=W)
        # self.status.pack(fill=X)
        self.parentPanel.add(self.status, minsize=15)

    def showAuthor(self):
        messagebox.showinfo('Author', 'Author is ...')

    def showVersionInfo(self):
        messagebox.showinfo('About', 'Python Notepad App beta v1.0')

    def openFile(self):
        self.fileName = filedialog.askopenfilename(defaultextension='.txt')
        if self.fileName:
            self.master.title('File: ' + os.path.abspath(self.fileName))
            self.textArea.delete(1.0, END)
            with open(self.fileName, 'r') as f:
                try:
                    self.textArea.insert(1.0, f.read())
                except Exception as e:
                    messagebox.showinfo('Error', 'Error while open file, cannot read file')

    def saveContent(self):
        if not self.fileName:
            self.saveContentAs()
        else:
            with open(self.fileName, 'w') as f:
                msg = self.textArea.get(1.0, END)
                f.write(msg)

    def saveContentAs(self):
        self.fileName = filedialog.asksaveasfilename(initialfile='unnamed.txt', defaultextension='.txt')
        if self.fileName:
            with open(self.fileName, 'w') as f:
                msg = self.textArea.get(1.0, END)
                f.write(msg)
            self.master.title('File: ' + os.path.abspath(self.fileName))

    def newNote(self):
        self.fileName = None
        self.master.title('new note')
        self.textArea.delete(1.0, END)

    def copyText(self):
        self.textArea.event_generate('<<Copy>>')

    def cutText(self):
        self.textArea.event_generate('<<Cut>>')

    def pasteText(self):
        self.textArea.event_generate('<<Paste>>')

    def undoOperation(self):
        self.textArea.event_generate('<<Undo>>')

    def redoOperation(self):
from tkinter import *
from tkinter import messagebox, filedialog
from functools import partial
import os


class NotePadApp(Frame):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.pack()
        self.master.title('Python Notepad App')
        self.master.geometry('800x500+100+100')
        self.fileName = None
        self.createWidgets()

    def createWidgets(self):
        # Add Menu
        self.menuBar = Menu(self)
        self.master.config(menu=self.menuBar)

        # File menu
        self.fileMenu = Menu(self.menuBar, tearoff=False)
        self.fileMenu.add_command(label='New', accelerator='Ctrl + N', command=self.newNote)
        self.fileMenu.add_command(label='Open', accelerator='Ctrl + O', command=self.openFile)
        self.fileMenu.add_command(label='Save', accelerator='Ctrl + s', command=self.saveContent)
        self.fileMenu.add_command(label='Save As', accelerator='Ctrl + Shift + S', command=self.saveContentAs)
        self.menuBar.add_cascade(label='File', menu=self.fileMenu)

        # Edit menu
        self.editMenu = Menu(self.menuBar, tearoff=False)
        self.editMenu.add_command(label='Undo', accelerator='Ctrl + Z', command=self.undoOperation)
        self.editMenu.add_command(label='Redo', accelerator='Ctrl + Y', command=self.redoOperation)
        self.editMenu.add_separator()
        self.editMenu.add_command(label='Cut', accelerator='Ctrl + X', command=self.cutText)
        self.editMenu.add_command(label='Copy', accelerator='Ctrl + C', command=self.copyText)
        self.editMenu.add_command(label='Paste', accelerator='Ctrl + V', command=self.pasteText)
        self.editMenu.add_separator()
        self.editMenu.add_command(label='Search', accelerator='Ctrl + F', command=self.searchContent)
        self.editMenu.add_command(label='Select All', accelerator='Ctrl + A', command=self.selectAll)
        self.menuBar.add_cascade(label='Edit', menu=self.editMenu)

        # About menu
        self.about_menu = Menu(self.menuBar, tearoff=False)
        self.about_menu.add_command(label='Author', command=self.showAuthor)
        self.about_menu.add_command(label='About', command=self.showVersionInfo)
        self.menuBar.add_cascade(label='About', menu=self.about_menu)

        # Create a PanedWindow for all widgets
        self.parentPanel = PanedWindow(orient=VERTICAL)
        self.parentPanel.pack(expand=YES, fill=BOTH)

        # Toolbar
        self.toolBar = Frame(self.parentPanel, height=5, bg='grey')
        self.buttonOpen = Button(self.toolBar, text='Open', command=self.openFile)
        self.buttonOpen.pack(side=LEFT, padx=5, pady=2)
        self.buttonSave = Button(self.toolBar, text='Save', command=self.saveContent)
        self.buttonSave.pack(side=LEFT)
        # self.toolBar.pack(expand=YES, fill=X)
        self.parentPanel.add(self.toolBar, minsize=30)

        self.textPanel = PanedWindow(self.parentPanel, orient=HORIZONTAL)
        # self.textPanel.pack(expand=1, fill=BOTH)

        # line number
        self.lnLabel = Label(self.textPanel, width=2, bg='antique white')
        # self.lnLabel.pack(side=LEFT, fill=Y)
        # self.lnLabel.grid(row=0, column=0)

        # text area
        self.textArea = Text(self.textPanel, undo=True, font=('Consolas', 16))
        # self.textArea.pack(side=LEFT, expand=YES, fill=BOTH)
        # self.textArea.grid(row=0, column=1)

        # scroll bar for text area
        self.scrollBar = Scrollbar(self.textPanel, width=15)
        self.textArea.config(yscrollcommand=self.scrollBar.set)
        self.scrollBar.config(command=self.textArea.yview)
        # self.textPanel.paneconfigure(self.scrollBar, minsize=40)
        # self.scrollBar.pack(side=LEFT, expand=0, fill=Y)
        # self.scrollBar.grid(row=0, column=2)

        self.textPanel.add(self.lnLabel, minsize=15)
        self.textPanel.add(self.textArea, width=760, height=440)
        self.textPanel.add(self.scrollBar, minsize=15)

        self.parentPanel.add(self.textPanel)

        # Status bar
        self.status = Label(self.parentPanel, text='Status: ok', bd=1, relief='sunken', anchor=W)
        # self.status.pack(fill=X)
        self.parentPanel.add(self.status, minsize=15)

    def showAuthor(self):
        messagebox.showinfo('Author', 'Author is ...')

    def showVersionInfo(self):
        messagebox.showinfo('About', 'Python Notepad App beta v1.0')

    def openFile(self):
        self.fileName = filedialog.askopenfilename(defaultextension='.txt')
        if self.fileName:
            self.master.title('File: ' + os.path.abspath(self.fileName))
            self.textArea.delete(1.0, END)
            with open(self.fileName, 'r') as f:
                try:
                    self.textArea.insert(1.0, f.read())
                except Exception as e:
                    messagebox.showinfo('Error', 'Error while open file, cannot read file')

    def saveContent(self):
        if not self.fileName:
            self.saveContentAs()
        else:
            with open(self.fileName, 'w') as f:
                msg = self.textArea.get(1.0, END)
                f.write(msg)

    def saveContentAs(self):
        self.fileName = filedialog.asksaveasfilename(initialfile='unnamed.txt', defaultextension='.txt')
        if self.fileName:
            with open(self.fileName, 'w') as f:
                msg = self.textArea.get(1.0, END)
                f.write(msg)
            self.master.title('File: ' + os.path.abspath(self.fileName))

    def newNote(self):
        self.fileName = None
        self.master.title('new note')
        self.textArea.delete(1.0, END)

    def copyText(self):
        self.textArea.event_generate('<<Copy>>')

    def cutText(self):
        self.textArea.event_generate('<<Cut>>')

    def pasteText(self):
        self.textArea.event_generate('<<Paste>>')

    def undoOperation(self):
        self.textArea.event_generate('<<Undo>>')

    def redoOperation(self):
        self.textArea.event_generate('<<Redo>>')

    def selectAll(self):
        self.textArea.tag_add('sel', '1.0', END)

    def searchText(self, textEntry, searchTop):
        # Before each search, clear previous selection tag
        self.textArea.tag_delete('highlightText')
        textToSearch = textEntry.get()
        # Config a tag to highlight search results
        self.textArea.tag_config('highlightText', background='yellow')

        # Show error messagebox if user enters nothing to search
        if not textToSearch or textToSearch.strip() == '':
            searchTop.destroy()
            messagebox.showinfo('Error', 'Please enter the content to be searched!')
            return

        start = '1.0'
        while True:
            pos = self.textArea.search(textToSearch, start, END)
            if not pos:
                break
            start = pos + ('+' + str(len(textToSearch)) + 'c')
            self.textArea.tag_add('highlightText', pos, start)

        # Show messagebox if content not found
        if start == '1.0':
            messagebox.showinfo('Not Found!', 'Content not found!')

        # Close search Toplevel widget
        searchTop.destroy()
        # Focus on the Text widget
        self.textArea.focus()

    def searchContent(self):
        searchTop = Toplevel(self)
        # searchTop.geometry('300x30+200+250')
        Label1 = Label(searchTop, text='Search text:')
        Label1.grid(row=0, column=0, padx=5, pady=5)
        textEntry = Entry(searchTop, width=20)
        textEntry.grid(row=0, column=1, padx=5)
        searchFunc = partial(self.searchText, textEntry=textEntry, searchTop=searchTop)
        button1 = Button(searchTop, text='Search', command=searchFunc)
        button1.grid(row=0, column=2, padx=5)
        textEntry.focus()


def main():
    app = NotePadApp()
    app.mainloop()


if __name__ == '__main__':
    main()
