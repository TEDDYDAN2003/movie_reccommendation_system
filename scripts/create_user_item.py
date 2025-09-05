# scripts/create_user_item.py
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///data/movielens.db")
ratings = pd.read_sql_table("ratings", engine)
user_item = ratings.pivot(index='userId', columns='movieId', values='rating')
# Option: fillna(0) or keep NaN for sparse workflows
user_item.to_pickle("data/user_item_matrix.pkl")
print("Saved user-item matrix as data/user_item_matrix.pkl")
