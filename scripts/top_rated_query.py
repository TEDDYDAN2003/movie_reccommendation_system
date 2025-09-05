import sqlite3
import pandas as pd

# Connect to your DB
conn = sqlite3.connect("data/movielens.db")

query = """
SELECT m.title, 
       AVG(r.rating) AS avg_rating, 
       COUNT(r.rating) AS num_ratings
FROM ratings r
JOIN movies m ON r.movieId = m.movieId
GROUP BY m.movieId
HAVING num_ratings > 50
ORDER BY avg_rating DESC
LIMIT 10;
"""

df = pd.read_sql_query(query, conn)
print(df)

conn.close()
