# Candidate-Manager
Welcome to the Candidate-Manager repository! This is a Django web application for managing candidate information.

## Prerequisites

Before you start, make sure you have the following installed:

- Python (version 3)
- pip (Python package installer)
- Virtualenv (optional, but recommended for isolated environments)
- Git (version control system)

## Clone the Repository

1. Open your terminal or command prompt.
2. Navigate to the directory where you want to store the project:
`cd /path/to/your/directory`
3. Clone the repository:
`git clone https://github.com/divyamt50/Candidate-Manager`


## Set Up the Virtual Environment (Optional but Recommended)

1. Create a virtual environment in the project directory:
`python -m venv venv`
2. Activate the virtual environment:
- On Windows:
  ```
  venv\Scripts\activate
  ```
- On macOS and Linux:
  ```
  source venv/bin/activate
  ```

## Install Dependencies

1. Navigate to the project directory:
`cd candidate-manager`

2. Install project dependencies using pip:
`pip install -r requirements.txt`


## Configure the Database

By default, this repository includes the SQLite database file (db.sqlite3). However, for a fresh setup, you might want to create a new database or apply migrations.

1. Apply migrations to set up the database:
`python manage.py migrate`


## Run the Development Server

1. Start the development server:
`python manage.py runserver`

2. Open your web browser and go to http://127.0.0.1:8000/ to access the application.

## Usage

- Use the navigation bar to manage candidates.
- The admin interface is accessible at http://127.0.0.1:8000/admin/ (login required).

