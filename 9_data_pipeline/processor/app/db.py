import mysql.connector
from mysql.connector import Error
import os

def connect_to_db():
    connection = None
    try:
        connection = mysql.connector.connect(
            host=os.getenv("MYSQL_HOST"),
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSWORD"),
            database=os.getenv("MYSQL_DATABASE")
        )
        print("Conexão Estabelecida.")
    except Error as e:
        print("Erro na conexão",e)

    return connection

def create_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS carbon_intensity (
        id INT AUTO_INCREMENT PRIMARY KEY,
        search_date DATE,
        prevision_date DATE,
        intensity_index VARCHAR(255),
        actual INT,
        forecast INT
    )
    """)

def insert_data(cursor, data):
    for entry in data:
        cursor.execute("""
        INSERT INTO carbon_intensity (search_date, prevision_date, intensity_index, actual, forecast)
        VALUES (%s, %s, %s, %s, %s)
        """, (entry['search_date'], entry['prevision_date'], entry['index'], entry['actual'], entry['forecast']))