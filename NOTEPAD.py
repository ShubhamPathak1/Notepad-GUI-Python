from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

#---------------------------DEFINING FUNCTIONS------------------
def NewFile():
    global file
    root.title('Untitled - NotePad')
    file = None
    TextArea.delete(1.0, END)    # IT WILL DELETE EVERYTHING FROM THE 0th CHARACTER OF THE FIRST LINE TO THE END OF THE TEXTAREA.

def OpenFile():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    # the above statements says the default extension i.e. .txt and if the filetypes if allfiles anything can be opened and if it is text documents, then .txt files can be opened.

    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()

def SaveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if file =="":
            file = None

        else:
            #Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()


def ExitFile():
    root.destroy()

def cut():
    TextArea.event_generate(('<<Cut>>'))  # IT AUTOMATICALLY HANDLES CUT.

def copy():
    TextArea.event_generate(('<<Copy>>'))  # IT AUTOMATICALLY HANDLES COPY.

def paste():
    TextArea.event_generate(('<<Paste>>'))  # IT AUTOMATICALLY HANDLES PASTE.

def dark_theme():
    TextArea.config(bg='black', fg='white', insertbackground='white')

def light_theme():
    TextArea.config(bg='white', fg='black', insertbackground='black')

def about():
    showinfo("NOTEPAD", "THIS NOTEPAD BY SHUBHAM PATHAK\nALLOWS YOU TO WRITE ANYTHING\nAND EDIT THEM AS PER YOUR WISH")

if __name__ == "__main__":
    #----------------BASIC TKINTER SETUP------------
    root = Tk()
    root.title('Untitled - NotePad')
    root.wm_iconbitmap(r'notepad.ico')
    root.geometry('800x500')

    #---------------ADDING TEXT AREA-----------
    TextArea = Text(root, font='lucida 13 ')
    file = None    # This file points to the file which is currently opened.
    TextArea.pack(expand=True, fill=BOTH)  # Packing the text area. 

    #----------------------CREATING A MENU BAR--------------------
    MenuBar = Menu(root)

    # FILE MENU
    FileMenu = Menu(MenuBar, tearoff=0)

    FileMenu.add_command(label='New', command=NewFile)   # adding a open new file submenu

    FileMenu.add_command(label='Open', command=OpenFile)   # adding a open existing file submenu

    FileMenu.add_command(label='Save As', command=SaveFile)   # adding a save existing file submenu
    
    FileMenu.add_separator()
    FileMenu.add_command(label='Exit', command=ExitFile)   # adding a exit app submenu
    
    MenuBar.add_cascade(label='File', menu=FileMenu)
    

    # EDIT MENU
    EditMenu = Menu(MenuBar, tearoff=0)

    EditMenu.add_command(label='Cut', command=cut)    # adding a cut submenu

    EditMenu.add_command(label='Copy', command=copy)    # adding a copy submenu

    EditMenu.add_command(label='Paste', command=paste)    # adding a paste submenu
    
    MenuBar.add_cascade(label='Edit', menu=EditMenu)

    # TOOLS MENU
    ToolsMenu = Menu(MenuBar, tearoff=0)

    Theme = Menu(ToolsMenu, tearoff=0)

    Theme.add_command(label="Dark Theme", command=dark_theme)    # activate dark theme
    Theme.add_command(label="Light Theme", command=light_theme)  # activates light theme
    ToolsMenu.add_cascade(label='Theme', menu = Theme)


    MenuBar.add_cascade(label='Tools', menu=ToolsMenu)
    
    #HELP MENU

    HelpMenu = Menu(MenuBar, tearoff=0)

    HelpMenu.add_command(label='About', command=about)    # adding an about submenu
    
    MenuBar.add_cascade(label='Help', menu=HelpMenu)


    root.config(menu=MenuBar)

    #----------------------ADDING SCROLL BAR---------------------
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT, fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)


    root.mainloop()
