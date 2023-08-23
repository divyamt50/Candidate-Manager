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




# CRUD Operations

The project implements CRUD operations (Create, Read, Update, Delete) to manage candidate information. This section provides an overview of how these operations are performed within the project.

### Create (Add Candidate)

To add a new candidate to the system:
1. Navigate to the "Add Candidate" page by clicking the "Add Candidate" link in the navigation bar.
2. Fill in the required fields in the candidate creation form.
3. Ensure that you provide valid input, as per the error handling rules mentioned in the "Error Handling" section of this `readme.md`.
4. Click the "Create" button to submit the form.
5. Upon successful submission, you will be redirected to the candidate's detail page.

### Read (View Candidate Details)

To view the details of a candidate:
1. From the candidate list page, click on the name of the candidate you wish to view.
2. The candidate's detailed information, including personal details, qualifications, and other relevant information, will be displayed.

### Update (Edit Candidate)

To edit an existing candidate's information:
1. From the candidate list page, click the "Edit" link next to the candidate's name.
2. Update the fields you wish to modify. Ensure the modifications comply with the error handling rules specified in the "Error Handling" section.
3. Click the "Update" button to save the changes.
4. Upon successful update, you will be redirected to the candidate's detail page.

### Delete (Remove Candidate)

To remove a candidate from the system:
1. From the candidate list page, click the "Delete" link next to the candidate's name.
2. A confirmation prompt will appear to confirm your action.
3. Once confirmed, the candidate's information will be permanently deleted from the system.



# Error Handling

In order to ensure data consistency and accuracy, the project includes error handling mechanisms that validate the user input for specific fields in various forms. These error handling rules have been implemented to maintain data integrity and provide a user-friendly experience. Below are some of the key error handling validations that have been applied:

### Phone Number Validation

For fields that require phone numbers, the project enforces the following rules:
- Phone numbers must be exactly 10 digits long.
- Only numeric digits are allowed.

### Email Validation

For email fields, the project enforces the following rules:
- The email address must contain the "@" symbol to be considered valid.
- The email address should follow the standard format for email addresses.

### Date of Birth Validation

Fields that require the user's date of birth follow these rules:
- The date must be in a specific date format (e.g., YYYY-MM-DD).
- The entered date must be a valid calendar date.

### Other Field Validations

In addition to the above examples, similar error handling mechanisms have been applied to various other form fields throughout the project. These validations ensure that the data entered by users meets the required format and criteria, reducing the risk of inaccurate or inconsistent data.

Please note that these error handling rules are designed to provide feedback to users when they enter data that doesn't meet the specified criteria. This enhances the user experience by preventing invalid data from being submitted and processed.

It's important to maintain these error handling mechanisms and keep them up-to-date as the project evolves and new fields are introduced. This will help maintain the overall quality and integrity of the data stored in the system.
