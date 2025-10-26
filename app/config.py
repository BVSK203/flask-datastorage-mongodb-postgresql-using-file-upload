import os

class Config:
    SECRET_KEY = 'your secret key'
    UPLOAD_FOLDER = 'uploads'
    ALLOWED_EXTENSIONS = {'csv'}

    # Database Configurations
    #POSTGRES_URI = "database url"
    POSTGRES_URI = "url"

    MONGO_URI = "mongo database url"

    # Ensure upload folder exists
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
