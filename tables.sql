/*
* Create table queries for 
* the COVID 19 tracker database
*/

-- Basic data organized, by country
CREATE TABLE summary
(
	id SERIAL,
	"Country" VARCHAR(255) NOT NULL,
	"Slug" VARCHAR(255),
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
	"Lat" DEC,
	"Lon" DEC,
	"Date" TIMESTAMP,
	"Cases" INT,
	"Staus" VARCHAR(255),
	PRIMARY KEY(id)
);
