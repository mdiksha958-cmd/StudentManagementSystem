# Student Management System

A console-based Student Management System built using Python and PostgreSQL.

This project allows users to manage student information and their marks through a simple command-line interface.

## Features

- Add new students
- View all students
- Update student information
- Delete students
- Search students by name or email
- Add marks for students
- View student marks
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


## Installation

### 1. Clone the repository

```bash
git clone https://github.com/mdiksha958-cmd/StudentManagementSystem.git

### 2. Navigate to the project directory

```bash
cd StudentManagementSystem

### 3. Install dependencies

```bash
pip install -r requirements.txt


### 4. Configure environment variables

Create a `.env` file in the project root and add the following:

```env
DB_HOST=localhost
DB_NAME=student_management
DB_USER=postgres
DB_PASSWORD=your_password
DB_PORT=5433
```

### 5. Run the application

```bash
python main.py
```
