import mysql.connector
def connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="123",
        database="e_b_payment"
        )

