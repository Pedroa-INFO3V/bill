from mysql.connector import (connection)

cnx = connection.MySQLConnection(
    user='root', 
    password='labinfo',
    host='127.0.0.1',
    database='cliente')

cursor = cnx.cursor()
sql = "INSERT INTO pessoa (nome, cidade, nascimento) VALUES ('Pedro', 'SGA', '2008-07-01')"
bora = "INSER INTO pessoa ('Bill', 'Natal', '1945-10-21')"

cursor.execute(sql, bora)
cnx.commit()

cnx.close()