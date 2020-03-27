
-- Show deaths by country in descending order
CREATE VIEW deaths_by_country 
AS 
SELECT "Country", "TotalDeaths", "NewDeaths" 
FROM public.summary
ORDER BY "TotalDeaths" DESC, "NewDeaths" DESC;

-- Show the number of new cases in descending order
CREATE VIEW new_cases_by_country
AS 
SELECT "Country", "NewConfirmed"
FROM public.summary
ORDER BY "NewConfirmed" DESC;

-- Show the number of recoveries by country
CREATE VIEW recoveries_by_country
AS 
SELECT "Country", "TotalRecovered", "NewRecovered"
FROM public.summary
ORDER BY "TotalRecovered" DESC;