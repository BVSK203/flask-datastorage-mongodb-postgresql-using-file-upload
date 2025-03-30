
# Flask Data Storage in MongoDB & PostgreSQL with File Upload

## Overview
This Flask-based project allows users to upload files and store metadata in both **MongoDB** and **PostgreSQL**. The frontend interacts with the backend via RESTful APIs.

## Features
- File Upload via Frontend
- Data Storage in **MongoDB** and **PostgreSQL**
- RESTful APIs for Data Retrieval
- Flask for Backend
- React/HTML-JS for Frontend (Optional)

## Tech Stack
- **Backend**: Flask, Flask-RESTful, Flask-PyMongo, SQLAlchemy
- **Database**: PostgreSQL, MongoDB
- **Frontend**: React.js / HTML, CSS, JavaScript

---

## Installation & Setup

### 1. Clone the Repository
```sh
git clone https://github.com/your-username/flask-mongo-postgres.git
cd flask-mongo-postgres
```

### 2. Backend Setup (Flask)
#### a) Create a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

#### b) Install Dependencies
```sh
pip install -r requirements.txt
```

#### c) Configure Environment Variables
Create a `.env` file in the backend directory:
```
MONGO_URI=mongodb://localhost:27017/flaskdb
POSTGRES_URI=postgresql://user:password@localhost/flaskdb
SECRET_KEY=your_secret_key
UPLOAD_FOLDER=uploads
```

#### d) Apply Migrations (PostgreSQL)
```sh
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

#### e) Run the Flask Server
```sh
python app.py
```

---

### 3. Frontend Setup
If using React:
```sh
cd frontend
npm install
npm start
```
If using simple HTML:
- Place `index.html` inside the `static/` folder in Flask.

---

## API Endpoints
| Method | Endpoint         | Description           |
|--------|----------------|----------------------|
| POST   | `/upload`       | Upload a file       |
| GET    | `/files`        | Get all uploaded files |
| GET    | `/file/<id>`    | Retrieve file by ID |

---

## Contribution
Feel free to fork this project and submit pull requests!

---

## License
MIT License. Free to use and modify.

