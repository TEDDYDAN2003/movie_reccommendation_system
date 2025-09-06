SELECT mg.genre,
       COUNT(r.rating) AS num_ratings,
       ROUND(AVG(r.rating),3) AS avg_rating
FROM movie_genres mg
JOIN ratings r ON mg.movieId = r.movieId
GROUP BY mg.genre
ORDER BY num_ratings DESC;
