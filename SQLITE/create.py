import sqlite3


db = sqlite3.connect('SERVER.db')
sql = db.cursor()

sql.execute(
    '''CREATE TABLE IF NOT EXISTS users (
       login TEXT,
       password TEXT,
       cash BIGINT
       )'''
)

db.commit()