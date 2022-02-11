import tkinter
from tkinter import *
import tkinter.messagebox
from tkinter.ttk import *



class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        self.master = master

        self.width_value=self.master.winfo_screenwidth()
        self.height_value=self.master.winfo_screenheight()
        self.master.geometry("%dx%d+0+0" % (self.width_value, self.height_value))

        self.frame= Frame(self.master)
        self.frame.grid(sticky="we")

    


        ### Setting Variables ###
        self.varStk = StringVar()
        self.varType = StringVar()
            #Automatically sets entry type to buy#
        self.varType.set("Buy")
        self.varQuan = StringVar()
        self.varEnPr = StringVar()


        ###### Stock Ticker Entry & Title ######
        self.stktik = Label(self.master, text= "Ticker:", font=("Helvetica", 16))
        self.stktik.grid(row=4, column=1, padx=(30,0), pady=(30,0))

        self.txtStkTik = Entry(self.master, text=self.varStk)
        self.txtStkTik.grid(row=4, column=2, padx=(5,0), pady=(30,0))

        ####### Entry Type & Title #####
        self.entrytype = Label(self.master, text="Entry Type: ", font=("Helvetica", 16))
        self.entrytype.grid(row=4, column=3, padx=(30,0), pady=(30,0))
                ### Drop Down Menu for Buy Type##
        self.txtEntryType = OptionMenu(root,self.varType, "Buy","Short")
        self.txtEntryType.grid(row=4, column=4, padx=(5,0), pady=(30,0))

        ###### Position Quantity & Title ######
        self.pos_quan = Label(self.master, text= "Position Quantity: ", font=("Helvetica", 16))
        self.pos_quan.grid(row=4, column=5, padx=(30,0), pady=(30,0))

        self.txtpos_quan = Entry(self.master, text=self.varQuan)
        self.txtpos_quan.grid(row=4, column=6, padx=(5,0), pady=(30,0))

        #### Position Entry Price & Title #########
        self.pos_price = Label(self.master, text= "Entry Price per Share: ", font=("Helvetica", 16))
        self.pos_price.grid(row=4, column=7, padx=(30,0), pady=(30,0))

        self.txtpos_price = Entry(self.master, text=self.varEnPr)
        self.txtpos_price.grid(row=4, column=8, padx=(5,0), pady=(30,0))


        ###### Submit Trade Button #######

        self.btnSubmit = Button(self.master, text="Submit", width=10, command=self.submit)
        self.btnSubmit.grid(row=5, column=2, padx=(0,90),pady=(30,0), sticky=NE)


    ### Function for when Button is Pressed ###    
    def submit(self):
        ### convert string values to a new variable ##
        stk = self.varStk.get()
        typ = self.varType.get()
        quan = int(self.varQuan.get())
        entPr = float(self.varEnPr.get())
        posSize = quan * entPr
        self.txtStkTik.delete(0, END)
        self.txtpos_quan.delete(0, END)
        self.txtpos_price.delete(0, END)
        self.varType.set("Buy")
        self.txtEntryType
        tkinter.messagebox.showinfo("Trade Submitted.", "You submitted {} for {} order in amount of {} share at an entry price of ${} for a total Position Size of ${}".format(stk,typ,quan,entPr,posSize))





if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
