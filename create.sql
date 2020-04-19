CREATE TABLE brand(
      brand_name VARCHAR(20) NOT NULL UNIQUE PRIMARY KEY
);
 
CREATE TABLE ownerships(
      ownership_type VARCHAR(20) NOT NULL UNIQUE PRIMARY KEY
);


CREATE TABLE States1(
country VARCHAR(20) NOT NULL,
state_name VARCHAR(20) NOT NULL ,
CONSTRAINT PK_States PRIMARY KEY (country,state_name)
);
CREATE TABLE Stores(
    brand_name VARCHAR (20) NOT NULL REFERENCES brand(brand_name),
    ownership_type VARCHAR (20) NOT NULL REFERENCES ownerships(ownership_type),
    state_name VARCHAR (20) ,
    country VARCHAR (20),
    store_number VARCHAR(20) NOT NULL PRIMARY KEY
    ,store_name VARCHAR(20) NOT NULL 
    ,address VARCHAR(20)
    ,city VARCHAR(20)
    ,postcode VARCHAR(20)
    ,longitude FLOAT(10)
    ,latitude FLOAT(10)
    ,CONSTRAINT FK_place FOREIGN KEY (country,state_name) REFERENCES States1(country,state_name)
);
