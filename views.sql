
-- Show deaths by country in ascending order
CREATE VIEW deaths_by_country 
AS 
SELECT "Country", "TotalDeaths"
FROM public.summary
ORDER BY TotalDeaths ASC;
