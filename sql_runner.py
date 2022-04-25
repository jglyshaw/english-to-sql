import sqlite3
    
def run_code(sql_text):
    connection = sqlite3.connect("myDB.db")
    crsr = connection.cursor()
    crsr.execute(sql_text)
    for row in crsr:
        print('row = %r' % (row,))
    connection.commit()
    connection.close()



