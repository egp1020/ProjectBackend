import sqlite3

DATABASE_NAME = "tables.db"


def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn


def create_tables():
    tables = [
        """CREATE TABLE IF NOT EXISTS category (
            id          INT     PRIMARY KEY UNIQUE NOT NULL,
            photo       BLOB,
            name        VARCHAR NOT NULL,
            description TEXT
        )"""
    ]
    db = get_db()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)
