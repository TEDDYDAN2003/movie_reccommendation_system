SELECT m.title, COUNT(r.rating) AS cnt, ROUND(AVG(r.rating),3) AS avg_rating
FROM movies m JOIN ratings r ON m.movieId = r.movieId
GROUP BY m.movieId
HAVING cnt >= 50
ORDER BY avg_rating DESC
LIMIT 20;
