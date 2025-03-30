import os

class Config:
    SECRET_KEY = 'siva'
    UPLOAD_FOLDER = 'uploads'
    ALLOWED_EXTENSIONS = {'csv'}

    # Database Configurations
    #POSTGRES_URI = "postgresql://siva:Sivakumar203@@localhost:5432/cars_db"
    POSTGRES_URI = "postgresql+psycopg2://siva:Sivakumar203@@127.0.0.1:5432/cars_db/postgres@PostgreSQL 17*"

    MONGO_URI = "mongodb://localhost:27017/"

    # Ensure upload folder exists
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
