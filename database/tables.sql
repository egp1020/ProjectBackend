PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: category
CREATE TABLE IF NOT EXISTS category (
    id          INT     PRIMARY KEY UNIQUE NOT NULL,
    photo       BLOB,
    name        VARCHAR NOT NULL,
    description TEXT
);

-- Table: inventory
CREATE TABLE IF NOT EXISTS inventory (
    id        INT  PRIMARY KEY NOT NULL UNIQUE,
    stock     INT  NOT NULL,
    date_hour TEXT NOT NULL
);

-- Table: products
CREATE TABLE IF NOT EXISTS products (
    id          INT     PRIMARY KEY UNIQUE NOT NULL,
    photo       BLOB,
    description TEXT,
    category    VARCHAR REFERENCES category (name),
    quantity    INT,
    stock       INT     NOT NULL REFERENCES inventory (stock),
    price       NUMERIC NOT NULL,
    tax         VARCHAR NOT NULL REFERENCES tax (taxType)
);

-- Table: tax
CREATE TABLE IF NOT EXISTS tax (
    id      INT  NOT NULL UNIQUE PRIMARY KEY,
    taxType TEXT UNIQUE NOT NULL,
    rate    INT  NOT NULL
);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
