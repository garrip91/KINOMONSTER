import sqlite3


db = sqlite3.connect('db.sqlite3')
sql = db.cursor()

sql.execute(
    '''DROP TABLE IF EXISTS KinomonsterApp_contacts'''
)

db.commit()