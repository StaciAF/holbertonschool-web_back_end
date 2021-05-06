-- use metal_bands table attr to rank
-- countries by fan #, bring over band origin
SELECT origin AS origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
