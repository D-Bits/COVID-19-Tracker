/*
* Create table queries for 
* the COVID 19 tracker database
*/

CREATE TABLE summary
(
	id SERIAL,
	country VARCHAR(255) NOT NULL,
	new_confirmed INT,
	total_confirmed INT,
	new_deaths INT,
	total_deaths INT,
	new_recovered INT,
	total_recovered INT,
	PRIMARY KEY(id)
);