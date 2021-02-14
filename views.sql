
-- Show deaths by country in descending order
CREATE VIEW deaths_by_country 
AS 
SELECT "Country", "TotalDeaths", "NewDeaths" 
FROM public.summary
ORDER BY "TotalDeaths" DESC, "NewDeaths" DESC;

-- Show total global deaths
CREATE VIEW total_global_deaths
AS 
SELECT sum("TotalDeaths") AS "Worldwide Deaths"
FROM public.summary;

-- Show the number of new cases in descending order
CREATE VIEW new_cases_by_country
AS 
SELECT "Country", "NewConfirmed"
FROM public.summary
ORDER BY "NewConfirmed" DESC;

-- Show total confirmed cases
CREATE VIEW total_cases_per_country
AS 
SELECT "Country", "TotalConfirmed"
FROM public.summary 
ORDER BY "TotalConfirmed" DESC;

-- Show the total number of recoveries by country
CREATE VIEW total_recoveries_by_country
AS 
SELECT "Country", "TotalRecovered", "NewRecovered"
FROM public.summary
ORDER BY "TotalRecovered" DESC;

-- Show the total number of recoveries by country
CREATE VIEW new_recoveries_by_country
AS 
SELECT "Country", "NewRecovered", "TotalRecovered"
FROM public.summary
ORDER BY "NewRecovered" DESC;

