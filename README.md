# Student Management System

A console-based Student Management System built using Python and PostgreSQL.

## Features

### Student Management
- Add Student
- View Students
- Update Student
- Delete Student
- Search Student by Name or Email

### Marks Management
- Add Marks
- View Marks
- Update Marks
- Delete Marks

## Tech Stack

- Python
- PostgreSQL
- psycopg2
- python-dotenv

## Project Structure

StudentManagementSystem/
│
├── database/
│   └── connection.py
│
├── services/
│   ├── student_services.py
│   └── marks_services.py
│
├── .env
├── .gitignore
├── main.py
├── requirements.txt
└── README.md

## Database

The project uses PostgreSQL with the following tables:

### Students
- student_id
- name
- email
- phone
- course
- year

### Marks
- mark_id
- student_id
- subject
- marks

## Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd StudentManagementSystem
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

#### Windows

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure environment variables

Create a `.env` file in the project root and add your PostgreSQL database credentials:

env
DB_HOST=localhost
DB_PORT=5433
DB_NAME=student_management
DB_USER=postgres
DB_PASSWORD=your_password

### 6. Run the application

```bash
python main.py
```

