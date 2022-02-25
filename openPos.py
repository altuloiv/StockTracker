import sqlite3

conn = sqlite3.connect('openPositions.db')
c = conn.cursor()

c.execute('''
        CREATE TABLE IF NOT EXISTS openPositions
        (
        [S_id] INTEGER PRIMARY KEY AUTOINCREMENT,
        [stock_ticker] TEXT NOT NULL,
        [entryType] TEXT NOT NULL,
        [pos_quan] INTEGER NOT NULL,
        [entryPrice] REAL NOT NULL,
        [pos_size] REAL
        )
        ''')
conn.commit()
