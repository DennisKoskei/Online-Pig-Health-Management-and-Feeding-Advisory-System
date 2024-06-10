CREATE DATABASE ophmfas;

USE ophmfas;

-- Users Table
CREATE TABLE Users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(80) UNIQUE NOT NULL,
    password VARCHAR(120) NOT NULL
);

-- Pigs Table
CREATE TABLE Pigs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(80) NOT NULL,
    owner_id INT,
    FOREIGN KEY (owner_id) REFERENCES Users(id)
);

-- HealthRecords Table
CREATE TABLE HealthRecords (
    id INT AUTO_INCREMENT PRIMARY KEY,
    pig_id INT,
    symptoms TEXT NOT NULL,
    diagnosis VARCHAR(120) NOT NULL,
    treatment TEXT NOT NULL,
    FOREIGN KEY (pig_id) REFERENCES Pigs(id)
);

-- FeedRecords Table
CREATE TABLE FeedRecords (
    id INT AUTO_INCREMENT PRIMARY KEY,
    pig_id INT,
    feed_type VARCHAR(120) NOT NULL,
    quantity FLOAT NOT NULL,
    date DATETIME NOT NULL,
    FOREIGN KEY (pig_id) REFERENCES Pigs(id)
);

-- Diseases Table
CREATE TABLE Diseases (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(80) NOT NULL,
    symptoms TEXT NOT NULL,
    treatment TEXT NOT NULL
);
