from mysql.connector import (connection)
from dotenv import load_dotenv
import os

def conectaBD():
    cnx = connection.MySQLConnection(
        user='root', 
        password='labinfo',
        host='127.0.0.1',
        database='cliente'
        )
    return cnx