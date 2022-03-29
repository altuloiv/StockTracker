import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from openPos import *
from closedPos import *
from tkinter import ttk
from app_class import *


### set values for window screen taking values from your window to size app window ###

tabControl = ttk.Notebook(master)
tab2 = ttk.Frame(tabControl)

tabControl.add(tab2, text ='Closed Positions')
tabControl.pack(expand = 1, fill ="both")



