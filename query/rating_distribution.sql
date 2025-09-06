SELECT rating, COUNT(*) AS cnt
FROM ratings
GROUP BY rating
ORDER BY rating;
