import psycopg2

def connect():
    return psycopg2.connect(
        dbname="loan_app_db",
        user="ayaahmed",
        password="ayaahmed123",  # Replace with the one you set earlier
        host="localhost",
        port="5432"
    )
