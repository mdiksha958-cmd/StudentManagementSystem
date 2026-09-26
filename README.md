# Student Management System

A console-based Student Management System built using Python and PostgreSQL.

This project allows users to manage student information and their marks through a simple command-line interface.

## Features

### Student Management
- Add new students
- View all students
- Update student information
- Delete students
- Search students by name or email

### Marks Management
- Add marks for students
- View all student marks
- Update marks
- Delete marks
- Input validation and error handling
- PostgreSQL database integration
- Relational database design with foreign key relationship
- Environment-based database configuration

## Tech Stack

- *Programming Language:* Python
- *Database:* PostgreSQL
- *Database Driver:* psycopg2
- *Environment Management:* python-dotenv
- *Version Control:* Git & GitHub

## Project Structure

```text
StudentManagementSystem/
│
├── database/
│   └── connection.py
│
├── services/
│   ├── student_services.py
│   └── marks_services.py
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md

## Database Setup

This project uses PostgreSQL as the database.

### Database Name

```text
student_management


### Tables

#### Students

| Column | Description |
|---|---|
| student_id | Unique ID of the student |
| name | Student name |
| email | Student email |
| phone | Student phone number |
| course | Course name |
| year | Current year |

#### Marks

| Column | Description |
|---|---|
| mark_id | Unique ID of the mark record |
| student_id | ID of the student |
| subject | Subject name |
| marks | Marks obtained |

The student_id in the marks table is related to the student_id in the students table.

## Installation & Setup

### Prerequisites

Make sure the following are installed:

- Python 3.x
- PostgreSQL
- Git

### 1. Clone the repository

```bash
git clone https://github.com/mdiksha958-cmd/StudentManagementSystem.git
cd StudentManagementSystem
```

## Database Schema

The application uses PostgreSQL with two related tables:

### Students
Stores basic student information such as:
- Student ID
- Name
- Email
- Phone
- Course
- Year

### Marks
Stores marks associated with students:
- Mark ID
- Student ID
- Subject
- Marks

### Relationship

The marks.student_id column references students.student_id
as a foreign key, establishing a one-to-many relationship between
students and marks.

## Installation & Setup

### Prerequisites

Make sure the following are installed:

- Python 3.x
- PostgreSQL
- Git

### 1. Clone the repository

```bash
git clone https://github.com/mdiksha958-cmd/StudentManagementSystem.git
cd StudentManagementSystem

### 2. Create a virtual environment

```bash
python -m venv venv
```


**Windows:**

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
DB_HOST=localhost
DB_NAME=student_management
DB_USER=postgres
DB_PASSWORD=your_postgresql_password
DB_PORT=5433


Replace your_postgresql_password with your PostgreSQL password.

### 5. Set up the database

Create a PostgreSQL database named:

```text
student_management
```

Run the SQL commands from `schema.sql` to create the required tables and relationships.

You can execute `schema.sql` using PostgreSQL or pgAdmin.

### 6. Run the application

```bash
python main.py
```

## Usage

After running the application, the following menu is displayed:

1. Add Student
2. View Students
3. Update Student
4. Delete Student
5. Add Marks
6. View Marks
7. Update Marks
8. Delete Marks
9. Search Student
10. Exit

The application allows users to manage student information and their marks through a simple console-based interface.

## Project Highlights

- Implemented CRUD operations for students and marks.
- Used PostgreSQL with a foreign key relationship between students and marks.
- Used psycopg2 for database connectivity.
- Used environment variables to keep database credentials outside the source code.
- Followed a modular service-based structure for better code organization.
- Added input validation and database error handling.

## Future Improvements

- Add user authentication and role-based access.
- Add a graphical or web-based interface.
- Add student performance reports and grade calculation.
- Add pagination and advanced search/filtering.
- Add automated tests.