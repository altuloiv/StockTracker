import tkinter as tk
from tkinter import *
import tkinter.messagebox
from tkinter.ttk import *
from openPos import *
from closedPos import *
from tkinter import ttk

master = tk.Tk()
### set values for window screen taking values from your window to size app window ###
width_value=master.winfo_screenwidth()
height_value=master.winfo_screenheight()
master.geometry("%dx%d+0+0" % (width_value, height_value))
tabControl = ttk.Notebook(master)
tab1 = tk.Frame(tabControl)
tab2 = tk.Frame(tabControl)
tabControl.add(tab1, text ='Home')
tabControl.add(tab2, text ='Closed Positions')
tabControl.pack(expand = 1, fill ="both")

### variables for various information when submitting to a database ###
varStk = StringVar()
varType = StringVar()
varType.set("Buy")
varQuan = StringVar()
varEnPr = StringVar()
closeQuan = StringVar()
closePrice = StringVar()

        ##### Little function to clearly pull information from the database for active trades, seperating the proper information to the columns and rows #####
def show():
    stktik = Label(tab1, text="Ticker:", font=("Helvetica", 12))
    stktik.grid(row=4, column=1, padx=(5,0), pady=(30,0))
    txtStkTik = Entry(tab1, text=varStk)
    txtStkTik.grid(row=4, column=2, padx=(5,0), pady=(30,0))

####### Entry Type & Title #####
    entrytype = Label(tab1, text="Entry Type: ", font=("Helvetica", 12))
    entrytype.grid(row=4, column=3, padx=(5,0), pady=(30,0))
                ### Drop Down Menu for Buy Type##
    txtEntryType = OptionMenu(tab1,varType, "Buy","Short")
    txtEntryType.grid(row=4, column=4, padx=(5,0), pady=(30,0))
        ###### Position Quantity & Title ######
    pos_quan = Label(tab1, text= "Position Quantity: ", font=("Helvetica", 12))
    pos_quan.grid(row=4, column=5, padx=(5,0), pady=(30,0))
    txtpos_quan = Entry(tab1, text=varQuan)
    txtpos_quan.grid(row=4, column=6, padx=(5,0), pady=(30,0))
        #### Position Entry Price & Title #########
    pos_price = Label(tab1, text= "Entry Price per Share: ", font=("Helvetica", 12))
    pos_price.grid(row=4, column=7, padx=(5,0), pady=(30,0))
    txtpos_price = Entry(tab1, text=varEnPr)
    txtpos_price.grid(row=4, column=8, padx=(5,0), pady=(30,0))
        ###### Submit Trade Button #######
    btnSubmit = Button(tab1, text="Submit", width=10, command=lambda : submit())
    btnSubmit.grid(row=5, column=4, padx=(5,0),pady=(30,0), columnspan=2, sticky=NE)
        ######### Table for Database Info #########
    dataID = Label(tab1, text= "ID", font=("Helvetica", 12))
    dataID.grid(row=6, column=1, padx=(5,0), pady=(5,0), columnspan=1)
    dataTicker = Label(tab1, text= "Ticker", font=("Helvetica", 12))
    dataTicker.grid(row=6, column=2, padx=(5,0), pady=(5,0), columnspan=1)
    dataType = Label(tab1, text= "Entry Type", font=("Helvetica", 12))
    dataType.grid(row=6, column=3, padx=(5,0), pady=(5,0), columnspan=1)
    dataQuan = Label(tab1, text= "Quantity", font=("Helvetica", 12))
    dataQuan.grid(row=6, column=4, padx=(5,0), pady=(5,0), columnspan=1)
    dataPrice = Label(tab1, text= "Price Per Share", font=("Helvetica", 12))
    dataPrice.grid(row=6, column=5, padx=(5,0), pady=(5,0), columnspan=1)
    dataSize = Label(tab1, text= "Total Pos Size", font=("Helvetica", 12))
    dataSize.grid(row=6, column=6, padx=(5,0), pady=(5,0), columnspan=1)
    r_set=c.execute("SELECT * FROM openPositions")
    i=7
    for openPositions in r_set:
        for j in range(len(openPositions)):
            e = Label(tab1, width=10, text=(openPositions[j]), font=("Helvetica", 12))
            e.grid(row=i, column = j + 1, padx=(50,0), pady=(5,0), columnspan=1)
                    ### Close position button to populate for every trade ### 
        e = Button(tab1, text="Close Position", width=30, command=lambda d=openPositions[0] : popupwin(d))
        e.grid(row=i, column = 6, padx=(10,0), pady=(5,0), columnspan=3)
        i=i+1 # increments for each to next row
    return(txtStkTik, txtEntryType,txtpos_quan,txtpos_price)

####################### SHOWS CLOSED POSITIONS FROM CLOSEDPOSITIONS DATABASE ################################
def show2():
    r_set=cc.execute("SELECT * FROM closedPositions")
    i=2
    for closedPositions in r_set:
        for j in range(len(closedPositions)):
            e = Label(tab2, width=10, text=(closedPositions[j]), font=("Helvetica", 12))
            e.grid(row=i, column = j + 1, padx=(50,0), pady=(5,0), columnspan=1)
                    ### Close position button to populate for every trade ### 
        i=i+1 # increments for each to next row

### Defining function to open Popup window ###
def popupwin(id):
    top = Toplevel()
    top.geometry("1000x200")
    label= Label(top, text="Closing Position")
    label.grid(row=1, column= 1, columnspan= 2)
    c.execute("SELECT stock_ticker, entrytype, pos_quan, entryPrice, pos_size FROM openPositions WHERE s_id=" + str(id))
    row = c.fetchone()
    for j in range(len(row)):
        stk = Label(top, text=row[j], font=("Helvetica", 12))
        stk.grid(row=2, column = j + 1, padx = (70,0), pady=(5,0))
    closingQ = Label(top, text="Closing Quantity:", font=("Helvetica", 14))
    closingQ.grid(row=3, column=1, padx=(30,0), pady=(30,0), columnspan=1)
    quan = Entry(top, text=closeQuan)
    quan.grid(row=3, column=2, padx=(5,0), pady=(30,0))
    closingP = Label(top, text="Closing Price:", font=("Helvetica", 14))
    closingP.grid(row=3, column=3, padx=(30,0), pady=(30,0), columnspan=1)
    quan = Entry(top, text=closePrice)
    quan.grid(row=3, column=4, padx=(5,0), pady=(30,0))
    confirm = Button(top, text = "Confirm", command=lambda:[closePosition(id),show2(), Tk.destroy(top)])
    confirm.grid(row=4, column=2, padx=(10,0), pady=(5,0), columnspan=3)

########## Defining function for entering Closed Positions into the closedPositions database for use later ############
def closePosition(id):
    c.execute("SELECT stock_ticker, entrytype, pos_quan, entryPrice, pos_size FROM openPositions WHERE s_id=" + str(id))
    row = c.fetchone()
    ticker = row[0]
    EnType = row[1]
    PosQuan = row[2]
    EntPrice = row[3]
    PositionSize = row[4]
    cloQuan =int(closeQuan.get())
    cloPrice = float(closePrice.get())
    varA = cloQuan * cloPrice
    ###Changing math operation depending on if the stock was shortered or bought for entry###
    if EnType == "Buy":
        out = varA - PositionSize
    if EnType == "Short":
        out = PositionSize - varA
    ###Ensuring that user is not closing more stocks then entered and showing the corresponding error message accordingly###
    if cloQuan > PosQuan:
        tkinter.messagebox.showinfo("Error:", "Closing Quantity can not be more than Entry Quantity.")
        popupwin(id)
        return
    if cloQuan < PosQuan:
        tkinter.messagebox.showinfo("Error:", "This application currently does not support partial closed positions. We apologize for the inconvience.")
        popupwin(id)
        return
    ###Setting all new data to be entered into the closedPositions Database to be entered.###
    array2= [ticker,EnType,PosQuan,EntPrice,cloQuan,cloPrice,out]
    con.executemany('INSERT INTO closedPositions(stock_ticker, entryType, pos_quan, entryPrice, close_quan, close_price, outcome) VALUES (?,?,?,?,?,?,?)', (array2,))
    con.commit()
    #calls my_delete() function to perform if every thing has been met previously#
    my_delete(id)
    tkinter.messagebox.showinfo("Trade Submitted.", "You closed the position for {} in the amount of {} shares at an exit price of ${} for a total profit of {}".format(ticker,cloQuan,cloPrice,out))

##### current delete function to remove data from database and from screen #####
def my_delete(id):
    c.execute("DELETE FROM openPositions WHERE s_id=" + str(id) )
    for row in tab1.grid_slaves():
        row.grid_forget()
    conn.commit()
    #calling show and profitLoss functions to update the information accordingly when called#
    show()
    profitLoss()
    
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
    varType.set("Buy")
            ## setting variables into an array for easy submitting to database ##
    array1 = [stk,typ,quan,entPr,posSize]
            ## connecto to database and inserting array of variables into database ##
    conn.executemany('INSERT INTO openPositions(stock_ticker, entryType, pos_quan, entryPrice, pos_size) VALUES (?,?,?,?,?)', (array1,))
    conn.commit()
            ## pop up message displaying that commit of stock was completed ##
    tkinter.messagebox.showinfo("Trade Submitted.", "You submitted {} for {} order in amount of {} share at an entry price of ${} for a total Position Size of ${}".format(stk,typ,quan,entPr,posSize))
    #call show() function to update information on the screen accordingly#
    show()

###Function to show the profit loss current on tab 2 pulling information from closed position database and adding them together####
def profitLoss():
    cc.execute("SELECT outcome FROM closedPositions")
    rows = cc.fetchall()
    out = 0
    for row in rows:
        out += row[0]
        ####### if statements to change background color of the output representing gains or losses. 
        if(out > 0):
            winLose = Label(tab2, text = out, font=("Helvetica",12), background="#00AC4B")
            winLose.grid(row=1, column = 9, padx=(5,0), pady=(30,0))
        if(out < 0):
            winLose = Label(tab2, text = out, font=("Helvetica",12), background= "#DA0000")
            winLose.grid(row=1, column = 9, padx=(5,0), pady=(30,0))
    
######Calling functions so they load the proper information in order when the app is started. #########
show()
show2()
profitLoss()

########### tab 2 #################
    ### Closed Positions ###
closedTicker = Label(tab2, text="Ticker", font= ("Helvetica", 12))
closedTicker.grid(row=1, column= 1, padx=(5,0), pady=(30,0))
closedType = Label(tab2, text="Entry Type", font=("Helvetica", 12))
closedType.grid(row=1, column=2, padx=(5,0), pady=(30,0))
closedQuantity = Label(tab2, text="Quantity", font=("Helvetica",12))
closedQuantity.grid(row=1, column=3, padx=(5,0), pady=(30,0))
closedEntry = Label(tab2, text="Entry Price", font=("Helvetica",12))
closedEntry.grid(row=1, column=4, padx=(5,0), pady=(30,0))
closedQuan = Label(tab2, text="Closed Quantity", font=("Helvetica", 12))
closedQuan.grid(row=1, column=5, padx=(5,0), pady=(30,0))
closedPrice = Label(tab2, text="Exit Price", font=("Helvetica", 12))
closedPrice.grid(row=1, column=6, padx=(5,0), pady=(30,0))
closedOutcome = Label(tab2, text="Outcome", font=("Helvetica", 12))
closedOutcome.grid(row=1, column=7, padx=(5,0), pady=(30,0))
profLoss = Label(tab2, text="Profit/Loss", font=("Helvetica",12))
profLoss.grid(row=1, column = 8, padx=(5,0), pady=(30,0))

##Main loop keeping app open##
master.mainloop()