/*
* Create table queries for 
* the COVID 19 tracker database
*/

-- Basic data organized, by country
CREATE TABLE summary
(
	id SERIAL,
	"Country" VARCHAR(255) NOT NULL,
	"NewConfirmed" INT,
	"TotalConfirmed" INT,
	"NewDeaths" INT,
	"TotalDeaths" INT,
	"NewRecovered" INT,
	"TotalRecovered" INT,
	PRIMARY KEY(id)
);

-- Table for confirmed U.S. cases
CREATE TABLE us_cases
(
	id SERIAL,
	"Province" VARCHAR(255),
	"Lat" INT,
	"Lon" INT,
	"Date": TIMESTAMP,
	"Cases" INT,
);
