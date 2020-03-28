/*
* Create table queries for 
* the COVID 19 tracker database
*/

-- Basic data organized, by country
CREATE TABLE Summary
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



