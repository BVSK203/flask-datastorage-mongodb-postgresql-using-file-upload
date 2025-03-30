import pandas as pd
from sqlalchemy import create_engine
import pymongo
from app.config import Config

# PostgreSQL Functions
def insert_to_postgres(df):
    """Insert data into PostgreSQL database"""
    engine = create_engine(Config.POSTGRES_URI)
    df.to_sql('cars', engine, if_exists='replace', index=False)

def get_postgres_data():
    """Retrieve data from PostgreSQL"""
    engine = create_engine(Config.POSTGRES_URI)
    df = pd.read_sql_table('cars', engine)
    return df.to_dict('records')

# MongoDB Functions
def insert_to_mongodb(df):
    """Insert data into MongoDB"""
    client = pymongo.MongoClient(Config.MONGO_URI)
    db = client['cars_db']
    collection = db['cars']
    collection.drop()  # Clears old data
    collection.insert_many(df.to_dict('records'))
    client.close()
    