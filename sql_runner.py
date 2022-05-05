import sqlite3
    
def run_code(sql_text):
    connection = sqlite3.connect("chinook.db")
    crsr = connection.cursor()
    crsr.execute(sql_text)
    for row in crsr:
        print(row)
    connection.commit()
    connection.close()



