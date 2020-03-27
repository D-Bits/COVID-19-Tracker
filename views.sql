
-- Show deaths by country in descending order
CREATE VIEW deaths_by_country 
AS 
SELECT "Country", "TotalDeaths", "NewDeaths" 
FROM public.summary
ORDER BY TotalDeaths ASC;

-- Show the number of new cases in descending order
CREATE VIEW new_cases_by_country
AS 
SELECT 