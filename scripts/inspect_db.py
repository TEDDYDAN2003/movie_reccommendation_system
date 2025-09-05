# scripts/inspect_db.py
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///data/movielens.db")
print(pd.read_sql_query("SELECT COUNT(*) AS c FROM movies", engine))
print(pd.read_sql_query("SELECT COUNT(*) AS c FROM ratings", engine))
print(pd.read_sql_query("SELECT COUNT(*) AS c FROM movie_genres", engine))
