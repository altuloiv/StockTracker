from tkinter import *

my_window = Tk()

width_value=my_window.winfo_screenwidth()
height_value=my_window.winfo_screenheight()
my_window.geometry("%dx%d+0+0" % (width_value, height_value))

my_window.mainloop()
