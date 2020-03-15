#A começar pelo inicio como deve ser!####
#########################################

# Clear the terminal screen
import sqlite3
import os
os.system('clear')

#conexao db
conn = sqlite3.connect('customer.db')
#cursor
c = conn.cursor()
'''
#create table
c.execute("""CREATE TABLE customer (
			first_name text,
			last_name text,
			email text
			)""")
'''
#c.execute("INSERT INTO customer VALUES ('Pedro','Dias','pedro@dias.com')")
c.execute("SELECT * FROM customer")
items = c.fetchall()

for i in items:
	print(i)

#commit na bd
conn.commit()

# fechar conexao
conn.close()
