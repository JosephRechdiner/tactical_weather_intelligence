CREATE DATABASE weather_db;

USE weather_db;

CREATE TABLE IF NOT EXISTS records_weather(
    id INT AUTO_INCREMENT,
    timestamp DATETIME,
    location_name VARCHAR(255),
    country VARCHAR(255),
    latitude FLOAT,
    longitude FLOAT,
    temperature FLOAT,
    wind_speed FLOAT,
    humidity INT,
    temperature_category VARCHAR(255),
    wind_category VARCHAR(255),
    PRIMARY KEY (id)
);
