-- Table: Category
CREATE TABLE IF NOT EXISTS Category (
    id          INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
    photo       BLOB,
    name        VARCHAR NOT NULL,
    description TEXT
);

-- Table: Inventory
CREATE TABLE IF NOT EXISTS Inventory (
    id          INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
    description TEXT    REFERENCES products (description) NOT NULL,
    stock       INT     NOT NULL,
    date_hour   TEXT    NOT NULL
);


-- Table: Products
CREATE TABLE IF NOT EXISTS Products (
    id          INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
    photo       BLOB,
    description TEXT,
    category    VARCHAR REFERENCES category (name),
    quantity    INT,
    stock       INT     NOT NULL REFERENCES inventory (stock),
    price       NUMERIC NOT NULL,
    barcode     BLOB,
    tax         VARCHAR NOT NULL REFERENCES tax (taxType) 
);


-- Table: Tax
CREATE TABLE IF NOT EXISTS Tax (
    id      INTEGER NOT NULL UNIQUE PRIMARY KEY AUTOINCREMENT,
    taxType TEXT    UNIQUE NOT NULL,
    rate    INT     NOT NULL
);


-- Table: TaxDetails
CREATE TABLE IF NOT EXISTS TaxDetails (
    id        INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
    taxType   TEXT    NOT NULL REFERENCES Tax (taxType),
    amountBuy DOUBLE  NOT NULL,
    baseBuy   DOUBLE  NOT NULL,
    valueTax  DOUBLE  NOT NULL
);