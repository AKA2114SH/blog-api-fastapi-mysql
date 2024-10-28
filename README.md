# FastAPI Blog Application

This is a simple API-based blog application built with **FastAPI** and **MySQL**. It provides endpoints to create users and posts, retrieve users, and manage posts. It demonstrates the basics of using FastAPI with SQLAlchemy and a MySQL database.

## Project Structure
├── main.py # FastAPI application ├── models.py # SQLAlchemy ORM models ├── database.py # Database connection and configuration ├── env # Virtual environment (optional) ├── README.md # Project documentation └── requirements.txt # Dependencies


## Features

- **User Management**: Create and retrieve user information.
- **Post Management**: Create, retrieve, and delete posts.
- **MySQL Database**: Uses MySQL as the database for storing user and post information.

## Requirements

- Python 3.8+
- MySQL
- FastAPI
- SQLAlchemy
- Uvicorn

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/fastapi-blog-application.git


Create and activate a virtual environment:

   cd fastapi-blog-application
python -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`

2. Install the dependencies:
   pip install -r requirements.txt

3. Configure the database connection: Update URL_DATABASE in database.py with your MySQL credentials and database name.


4. Run the application:
uvicorn main:app --reload
 
5. Access the API documentation:

Open your browser and go to http://127.0.0.1:8000/docs.