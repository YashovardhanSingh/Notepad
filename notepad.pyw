from tkinter import *
from tkinter import filedialog
import os

window = Tk()
window.title('Notepad')
window.geometry('650x700')

def NewFile():
    global file
    window.title('Untitled - Notepad')
    file = None
    TextArea.delete(1.0, END)

def OpenFile():
    global file
    file = filedialog.askopenfilename(defaultextension='.txt', filetypes=[('All Files', '*.*'), ('Text Documents', '*.txt')])
    if file == '':
        file = None
    else:
        window.title(os.path.basename(file) + '- Notepad')
        TextArea.delete(1.0, END)
        with open(file, 'r') as f:
            TextArea.insert(1.0, f.read())

def SaveFile():
    global file
    if file == None:
        file = filedialog.asksaveasfilename(initialfile='Untitled.txt', defaultextension='.txt', filetypes=[('All Files', '*.*'), ('Text Documents', '*.txt')])
        if file == '':
            file = None
        else:
            with open(file, 'w') as y:
                y.write(TextArea.get(1.0, END))
            window.title(os.path.basename(file) + '- Notepad')
    else:
        with open(file, 'w') as r:
            r.write(TextArea.get(1.0, END))
def ExitApp():
    window.destroy()

def Cut():
    TextArea.event_generate(('<<Cut>>'))

def Copy():
    TextArea.event_generate(('<<Copy>>'))

def Paste():
    TextArea.event_generate(('<<Paste>>'))

def About():
    from tkinter.messagebox import showinfo
    showinfo("Notepad", 'Notepad by Yashovardhan')

TextArea = Text(window, font='lucida 13')
TextArea.pack(fill=BOTH, expand=True)
file = None
MenuBar = Menu(window)
FileMenu = Menu(MenuBar, tearoff=0)
FileMenu.add_command(label='New', command=NewFile)
FileMenu.add_command(label='Open', command=OpenFile)
FileMenu.add_command(label='Save', command=SaveFile)
FileMenu.add_separator()
FileMenu.add_command(label="Exit", command=ExitApp)
MenuBar.add_cascade(label='File', menu=FileMenu)
EditMenu = Menu(MenuBar, tearoff=0)
EditMenu.add_command(label='Cut', command=Cut)
EditMenu.add_command(label='Copy', command=Copy)
EditMenu.add_command(label='Paste', command=Paste)
MenuBar.add_cascade(label='Edit', menu=EditMenu)
HelpMenu = Menu(MenuBar, tearoff=0)
HelpMenu.add_command(label='About', command=About)
MenuBar.add_cascade(label="Help", menu=HelpMenu)
window.config(menu=MenuBar)
scroll = Scrollbar(TextArea)
scroll.pack(side=RIGHT, fill=Y)
scroll.config(command=TextArea.yview)
TextArea.config(yscrollcommand=scroll.set)

window.mainloop()
