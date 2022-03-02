import tkinter as tk
from tkinter import *
import tkinter.messagebox
from tkinter.ttk import *
from openPos import *
from closedPos import *

master = Tk()


width_value=master.winfo_screenwidth()
height_value=master.winfo_screenheight()
master.geometry("%dx%d+0+0" % (width_value, height_value))

frame =  Frame(master)

varStk = StringVar()
varType = StringVar()
varType.set("Buy")
varQuan = StringVar()
varEnPr = StringVar()







        ##### Little function to clearly pull information from the database for active trades, seperating the proper information to the columns and rows #####

            
def show():
    stktik = Label(master, text="Ticker:", font=("Helvetica", 16))
    stktik.grid(row=4, column=1, padx=(30,0), pady=(30,0))

    txtStkTik = Entry(master, text=varStk)
    txtStkTik.grid(row=4, column=2, padx=(5,0), pady=(30,0))

####### Entry Type & Title #####
    entrytype = Label(master, text="Entry Type: ", font=("Helvetica", 16))
    entrytype.grid(row=4, column=3, padx=(30,0), pady=(30,0))
                ### Drop Down Menu for Buy Type##
    txtEntryType = OptionMenu(master,varType, "Buy","Short")
    txtEntryType.grid(row=4, column=4, padx=(5,0), pady=(30,0))

        ###### Position Quantity & Title ######
    pos_quan = Label(master, text= "Position Quantity: ", font=("Helvetica", 16))
    pos_quan.grid(row=4, column=5, padx=(30,0), pady=(30,0))

    txtpos_quan = Entry(master, text=varQuan)
    txtpos_quan.grid(row=4, column=6, padx=(5,0), pady=(30,0))

        #### Position Entry Price & Title #########
    pos_price = Label(master, text= "Entry Price per Share: ", font=("Helvetica", 16))
    pos_price.grid(row=4, column=7, padx=(30,0), pady=(30,0))

    txtpos_price = Entry(master, text=varEnPr)
    txtpos_price.grid(row=4, column=8, padx=(5,0), pady=(30,0))


        ###### Submit Trade Button #######

    btnSubmit = Button(master, text="Submit", width=10, command=lambda : submit())
    btnSubmit.grid(row=4, column=9, padx=(30,90),pady=(30,0), sticky=NE)


        ######### Table for Database Info #########

    dataTicker = Label(master, text= "Ticker", font=("Helvetica", 14))
    dataTicker.grid(row=5, column=1, padx=(30,0), pady=(5,0), columnspan=1)

    dataType = Label(master, text= "Entry Type", font=("Helvetica", 14))
    dataType.grid(row=5, column=2, padx=(30,0), pady=(5,0), columnspan=1)

    dataQuan = Label(master, text= "Quantity", font=("Helvetica", 14))
    dataQuan.grid(row=5, column=3, padx=(30,0), pady=(5,0), columnspan=1)

    dataPrice = Label(master, text= "Price Per Share", font=("Helvetica", 14))
    dataPrice.grid(row=5, column=4, padx=(30,0), pady=(5,0), columnspan=1)

    dataSize = Label(master, text= "Total Pos Size", font=("Helvetica", 14))
    dataSize.grid(row=5, column=5, padx=(30,0), pady=(5,0), columnspan=1)
    
    r_set=c.execute("SELECT * FROM openPositions")
    i=6
    for openPositions in r_set:
        for j in range(len(openPositions)):
            e = Label(master, width=10, text=(openPositions[j]), font=("Helvetica", 12))
            e.grid(row=i, column = j + 1, padx=(70,0), pady=(5,0), columnspan=1)
                    ### Close position button to populate for every trade ### 
        e = Button(master, text="Close Position", width=30, command=lambda d=openPositions[0] : my_delete(d))
        e.grid(row=i, column = 6, padx=(10,0), pady=(5,0), columnspan=3)
            
        i=i+1 # increments for each to next row
    return(txtStkTik, txtEntryType,txtpos_quan,txtpos_price)



def my_delete(id):
    my_var=tkinter.messagebox.askyesnocancel("DELETE?", "Delete id:"+str(id),icon='warning',default="no")
    if my_var:
        r_set=c.execute("DELETE FROM openPositions WHERE s_id=" + str(id) )
        for row in master.grid_slaves():
            row.grid_forget()
        conn.commit()
        show()
        tkinter.messagebox.showerror("Deleted ","No of records deleted=" +str(r_set.rowcount))
    


    ### Function for when Button is Pressed ###    
def submit():
        ### convert string values to a new variable ##
    stk = varStk.get()
    typ = varType.get()
            ## changing quan and etrPr from string to integer and float values for multiplication ##
    quan = int(varQuan.get())
    entPr = float(varEnPr.get())
            ## multiplying quan and entPr to give us the Position Size for database and submitted text ##
    posSize = quan * entPr
            ## Clearing entered data and resetting drop down menu to buy once button is clicked ##

    varType.set("Buy")
            ## setting variables into an array for easy submitting to database ##
    array1 = [stk,typ,quan,entPr,posSize]
            ## connecto to database and inserting array of variables into database ##
    conn.executemany('INSERT INTO openPositions(stock_ticker, entryType, pos_quan, entryPrice, pos_size) VALUES (?,?,?,?,?)', (array1,))
    conn.commit()
            ## pop up message displaying that commit of stock was completed ##
    tkinter.messagebox.showinfo("Trade Submitted.", "You submitted {} for {} order in amount of {} share at an entry price of ${} for a total Position Size of ${}".format(stk,typ,quan,entPr,posSize))

            #### Copied over the function for writing the information on screen to auto populate info when clicking submit instead of refreshing the app ###
    show()

show()


master.mainloop()