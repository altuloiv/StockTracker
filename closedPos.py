import sqlite3

con = sqlite3.connect('closedPositions.db')
cc = con.cursor()

cc.execute('''
        CREATE TABLE IF NOT EXISTS closedPositions
        (
        [stock_ticker] TEXT NOT NULL,
        [entryType] TEXT NOT NULL,
        [pos_quan] INTEGER NOT NULL,
        [entryPrice] REAL NOT NULL,
        [close_quan] INTEGER NOT NULL,
        [close_price] REAL NOT NULL,
        [outcome] FLOAT NOT NULL
        )
        ''')
con.commit()