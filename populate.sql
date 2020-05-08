-- TABLE brand
INSERT INTO brand(brand_name) VALUES ('Starbucks');
INSERT INTO brand(brand_name) VALUES ('Teavana');


-- TABLE ownerships
INSERT INTO ownerships(ownership_type) VALUES ('Licensed');
INSERT INTO ownerships(ownership_type) VALUES ('Joint Venture');
INSERT INTO ownerships(ownership_type) VALUES ('Company Owned');
INSERT INTO ownerships(ownership_type) VALUES ('Franchise');

--TABLE States1

INSERT INTO States1(state_name,country ) VALUES ('AJ','AE');
INSERT INTO States1(state_name,country) VALUES ('AZ','AE');
INSERT INTO States1(state_name,country) VALUES ('AL','AE');
INSERT INTO States1(state_name,country) VALUES ('DU','AE');
INSERT INTO States1(state_name,country) VALUES ('B','AR');
INSERT INTO States1(state_name,country) VALUES ('C','AR');
INSERT INTO States1(state_name,country) VALUES ('K','AR');




--TABLE States1
INSERT INTO Stores(brand_name,store_number,store_name,ownership_type,address,city,state_name,country,postcode,longitude,latitude)
VALUES ('Starbucks','47370-257954','Ajman Drive','Licensed','1 Street','Ajman','AJ','AE','2111',55.47,25.42);


INSERT INTO Stores(brand_name,store_number,store_name,ownership_type,address,city,state_name,country,postcode,longitude,latitude)
VALUES ('Starbucks','22126-218024','Twofour 54','Joint Venture','Al Salam Street','Abu Dhabi','AZ','AE','32224',54.38,24.48);

INSERT INTO Stores(brand_name,store_number,store_name,ownership_type,address,city,state_name,country,postcode,longitude,latitude)
VALUES ('Starbucks','18182-182165','Dalma Mall Level 1','Joint Venture','Dalma Mall','Abu Dhabi','AL','AE','22115',54.49,24.4);


INSERT INTO Stores(brand_name,store_number,store_name,ownership_type,address,city,state_name,country,postcode,longitude,latitude)
VALUES ('Starbucks','25823-198067','Terrazas','Franchise','Cruce 202 ','Buenos Aires','B','AR','C1663',-58.7,-34.53);

INSERT INTO Stores(brand_name,store_number,store_name,ownership_type,address,city,state_name,country,postcode,longitude,latitude)
VALUES ('Teavana','19945-198044','Abasto 2','Company Owned','Avenida Corrien','Buenos Aires','C','AR','C1193AAE',-58.41,-34.6);

INSERT INTO Stores(brand_name,store_number,store_name,ownership_type,address,city,state_name,country,postcode,longitude,latitude)
VALUES ('Starbucks','15458-161684','Triunvirato','Company Owned','Av Triunvirato','Buenos Aires','K','AR','C1431FBT',-58.48,-34.58);
