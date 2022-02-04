import sqlite3

conn = sqlite3.connect('stocks')
c = conn.cursor()

c.execute('''
        CREATE TABLE IF NOT EXISTS stocks
        ([stock_id] INTEGER PRIMARY KEY,
        [stock_ticker] TEXT NOT NULL,
        [buy_price] INTEGER NOT NULL,
        [buy_amount] INTEGER NOT NULL)
        ''')
conn.commit()
