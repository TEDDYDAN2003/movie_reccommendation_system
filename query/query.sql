-- SQLite
SELECT m.movieId, m.title,
       COUNT(r.userId) AS num_ratings,
       ROUND(AVG(r.rating), 3) AS avg_rating
FROM movies m
JOIN ratings r ON m.movieId = r.movieId
GROUP BY m.movieId, m.title
ORDER BY num_ratings DESC
LIMIT 10;
