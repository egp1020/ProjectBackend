import os
import sqlite3
from flask import Flask
from flask import render_template as render

app = Flask(__name__)


currentDirectory = os.getcwd()
DATABASE_NAME = "tables.db"


def get_db():
    connection = sqlite3.connect(currentDirectory+DATABASE_NAME)
    return connection


def create_tables():
    cursor = get_db().cursor()
    tables = [
        """CREATE TABLE IF NOT EXISTS Category (
                id          INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                photo       BLOB,
                name        VARCHAR NOT NULL,
                description TEXT
            );""",
        """CREATE TABLE IF NOT EXISTS Inventory (
                id          INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
                description TEXT    REFERENCES products (description)  NOT NULL,
                stock       INT     NOT NULL,
                date_hour   TEXT    NOT NULL
            );""",
        """CREATE TABLE IF NOT EXISTS Products (
                id          INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                photo       BLOB,
                description TEXT,
                category    VARCHAR REFERENCES category (name),
                quantity    INT,
                stock       INT     NOT NULL REFERENCES inventory (stock),
                price       NUMERIC NOT NULL,
                barcode     BLOB,
                tax         VARCHAR NOT NULL REFERENCES tax (taxType)
            );""",
        """CREATE TABLE IF NOT EXISTS Tax (
                id          INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT,
                taxType     TEXT UNIQUE NOT NULL,
                rate        INT  NOT NULL
            );""",
        """CREATE TABLE IF NOT EXISTS TaxDetails (
                id          INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                taxType     TEXT    NOT NULL REFERENCES Tax (taxType),
                amountBuy   DOUBLE  NOT NULL,
                baseBuy     DOUBLE  NOT NULL,
                valueTax    DOUBLE  NOT NULL
        );"""
    ]

    for sql in tables:
        cursor.execute(sql)

from .category.routes import bpcategory
app.register_blueprint(bpcategory)

from .inventory.routes import bpinventory
app.register_blueprint(bpinventory)

from .product.routes import bpproduct
app.register_blueprint(bpproduct)

from .tax.routes import bptax
app.register_blueprint(bptax)

from .taxDetails.routes import bptaxDetails
app.register_blueprint(bptaxDetails)