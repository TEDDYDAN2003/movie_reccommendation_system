# scripts/load_movielens_sqlite.py
import pandas as pd
from sqlalchemy import create_engine, inspect
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "ml-latest-small")
DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "movielens.db")
DB_URI = f"sqlite:///{DB_PATH}"

def load():
    engine = create_engine(DB_URI, echo=False)
    print("Using DB URI:", DB_URI)

    # read CSVs
    movies = pd.read_csv(os.path.join(DATA_DIR, "movies.csv"))
    ratings = pd.read_csv(os.path.join(DATA_DIR, "ratings.csv"))
    tags = pd.read_csv(os.path.join(DATA_DIR, "tags.csv"))
    links = pd.read_csv(os.path.join(DATA_DIR, "links.csv"))

    # write to sqlite
    movies.to_sql("movies", engine, if_exists="replace", index=False)
    ratings.to_sql("ratings", engine, if_exists="replace", index=False)
    tags.to_sql("tags", engine, if_exists="replace", index=False)
    links.to_sql("links", engine, if_exists="replace", index=False)

    # create a normalized movie_genres table (explode genres)
    movies['genres'] = movies['genres'].fillna("(no genres listed)")
    mg = movies[['movieId', 'genres']].copy()
    mg['genres'] = mg['genres'].str.split('|')
    mg = mg.explode('genres').rename(columns={'genres': 'genre'})
    mg[['movieId','genre']].to_sql("movie_genres", engine, if_exists="replace", index=False)

    inspector = inspect(engine)
    print("Tables in DB:", inspector.get_table_names())

if __name__ == "__main__":
    load()
