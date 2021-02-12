from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *

def change_color():
    pass

def change_font(*args):
    pass

def new_file():
    pass

def open_file():
    pass

def save_file():
    pass

def cut():
    pass

def copy():
    pass

def paste():
    pass

def about():
    pass

def quit():
    pass

window = Tk()
window.title("Text Editor")
file = None

#WINDOW DIMENSIONS
wd = [500,500]
#SCREEN DIMENSIONS
sd = [window.winfo_screenwidth(),window.winfo_screenheight()]


#Divided by for due to having two monitors
x = int((sd[0]/4) - (wd[0]/2))
y = int((sd[1]/2) - (wd[1]/2))

window.geometry("{}x{}+{}+{}".format(wd[0],wd[1],x,y))

font_name = StringVar(window)
font_name.set("Arial")
font_size = StringVar(window)
font_size.set("25")

text_area = Text(window, font =(font_name.get(),font_size.get()))
scroll_bar = Scrollbar(text_area)
window.grid_rowconfigure(0,weight=1)
window.grid_columnconfigure(0,weight=1)
text_area.grid(sticky = N + E + S + W)
window.mainloop()
