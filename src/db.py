import sqlite3
import os

DATABASE_NAME = "src/database/tables.db"

def get_db():
    connection = sqlite3.connect(DATABASE_NAME)
    return connection

def cursor():
    cursor = get_db.cursor()
    return cursor

def create_tables():
        sql = myfile.read()
        cursor = get_db().cursor()
        cursor.execute(sql)

def create_tables():
    cursor = get_db().cursor()
    tables = [
        """CREATE TABLE IF NOT EXISTS category (
            id          INT     PRIMARY KEY UNIQUE NOT NULL,
            photo       BLOB,
            name        VARCHAR NOT NULL,
            description TEXT
            );""",
        """CREATE TABLE IF NOT EXISTS category (
                id          INT     PRIMARY KEY UNIQUE NOT NULL,
                photo       BLOB,
                name        VARCHAR NOT NULL,
                description TEXT
            );""",
        """CREATE TABLE IF NOT EXISTS inventory (
                id        INT  PRIMARY KEY NOT NULL UNIQUE,
                stock     INT  NOT NULL,
                date_hour TEXT NOT NULL
            );""",
        """
            CREATE TABLE IF NOT EXISTS products (
                id          INT     PRIMARY KEY UNIQUE NOT NULL,
                photo       BLOB,
                description TEXT,
                category    VARCHAR REFERENCES category (name),
                quantity    INT,
                stock       INT     NOT NULL REFERENCES inventory (stock),
                price       NUMERIC NOT NULL,
                tax         VARCHAR NOT NULL REFERENCES tax (taxType)
            );""",
            """CREATE TABLE IF NOT EXISTS tax (
                id      INT  NOT NULL UNIQUE PRIMARY KEY,
                taxType TEXT UNIQUE NOT NULL,
                rate    INT  NOT NULL
            );
            """
    ]

    for sql in tables:
        cursor.execute(sql)
