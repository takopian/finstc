DROP TABLE IF EXISTS dealer_car;
DROP TABLE IF EXISTS car;
DROP TABLE IF EXISTS dealer;

CREATE TABLE car (
    id	INTEGER,
    name TEXT NOT NULL,
    PRIMARY KEY(id AUTOINCREMENT)
);

CREATE TABLE dealer (
    id	INTEGER,
    name TEXT NOT NULL,
    PRIMARY KEY(id AUTOINCREMENT)
);

CREATE TABLE dealer_car (
    dealer_id	INTEGER,
    car_id	INTEGER,
    price  INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    FOREIGN KEY(dealer_id) REFERENCES dealer(id) ON DELETE CASCADE,
    FOREIGN KEY(car_id) REFERENCES car(id) ON DELETE CASCADE,
    UNIQUE(dealer_id, car_id)
);

INSERT INTO car(name) VALUES("kia_rio");
INSERT INTO dealer(name) VALUES("somebody");
INSERT INTO dealer_car(dealer_id, car_id, price, quantity) VALUES(1, 1, 999999, 1);