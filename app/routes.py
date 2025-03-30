from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.utils import secure_filename
import os
from app.utils import allowed_file, read_car_data
from app.database import insert_to_postgres, insert_to_mongodb, get_postgres_data
from app.config import Config

main = Blueprint('main', __name__)

@main.route('/')
def index():
    """Display homepage with uploaded car data."""
    cars = get_postgres_data()
    return render_template('templates/index.html', cars=cars)

@main.route('/upload', methods=['POST'])
def upload_file():
    """Handle CSV file uploads and insert data into databases."""
    if 'file' not in request.files:
        flash('No file selected')
        return redirect(url_for('main.index'))
    
    file = request.files['file']
    if file.filename == '' or not allowed_file(file.filename):
        flash('Invalid file. Please upload a CSV file.')
        return redirect(url_for('main.index'))
    
    filename = secure_filename(file.filename)
    filepath = os.path.join(Config.UPLOAD_FOLDER, filename)
    file.save(filepath)

    try:
        df = read_car_data(filepath)
        insert_to_postgres(df)  # Insert into PostgreSQL
        insert_to_mongodb(df)  # Insert into MongoDB
        flash('Data successfully uploaded and inserted into databases')
    except Exception as e:
        flash(f'Error processing file: {str(e)}')

    os.remove(filepath)  # Delete uploaded file after processing
    return redirect(url_for('main.index'))
