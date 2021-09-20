import sqlite3

DATABASE_NAME = "tables.db"

def get_db():
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()
    return cursor


def create_tables():
    tables = [
        """CREATE TABLE IF NOT EXISTS category (
            id          INT     PRIMARY KEY UNIQUE NOT NULL,
            photo       BLOB,
            name        VARCHAR NOT NULL,
            description TEXT
        )"""
    ]
    cursor = get_db()
    for table in tables:
        cursor.execute(table)
