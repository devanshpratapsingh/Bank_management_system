import sqlite3 as sq

conn = sq.connect('bank.db')

conn.execute('''CREATE TABLE IF NOT EXISTS employee_login
         (
             ID INT,
             password TEXT);''')

conn.execute("INSERT INTO employee_login values (1,'nikhil@123')")
conn.execute("INSERT INTO employee_login values (2,'surya@123')")
conn.execute("INSERT INTO employee_login values (3,'ajay@123')")
conn.commit()
conn.close()