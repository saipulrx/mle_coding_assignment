/* CREATE_TABLE_my_table.sql */
CREATE TABLE IF NOT EXISTS iris (
    Id int NOT NULL , 
    SepalLengthCm DECIMAL(5,2) NOT NULL, 
    SepalWidthCm DECIMAL(5,2) NOT NULL, 
    PetalLengthCm DECIMAL(5,2) NOT NULL,
    PetalWidthCm DECIMAL(5,2) NOT NULL,
    Species VARCHAR(50),
    PRIMARY KEY (Id));