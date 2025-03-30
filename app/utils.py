import os
import pandas as pd
from app.config import Config

def allowed_file(filename):
    """Check if the uploaded file is a valid CSV."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS

def read_car_data(file_path):
    """Read the uploaded CSV file and return a DataFrame."""
    return pd.read_csv(file_path)
