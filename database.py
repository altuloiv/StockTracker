import sqlite3

conn = sqlite3.connect('stocks.db')
c = conn.cursor()

c.execute('''
        CREATE TABLE IF NOT EXISTS stocks
        (
        [stock_ticker] TEXT NOT NULL,
        [entryType] TEXT NOT NULL,
        [pos_quan] INTEGER NOT NULL,
        [entryPrice] REAL NOT NULL,
        [pos_size] REAL
        )
        ''')
conn.commit()
