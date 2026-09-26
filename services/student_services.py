from database.connection import get_connection

def add_student():
    name = input("Enter student name: ").strip()
    email = input("Enter email: ").strip()
    phone = input("Enter phone: ").strip()
    course = input("Enter course: ").strip()

    while True:
        try:
            year = int(input("Enter year: "))
            if year < 1 or year > 4:
                print("Year must be between 1 and 4.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        INSERT INTO students (name, email, phone, course, year)
        VALUES (%s, %s, %s, %s, %s)
    """

    cursor.execute(query, (name, email, phone, course, year))

    connection.commit()

    cursor.close()
    connection.close()

    print("Student added successfully!")

def view_students():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    print("\n========== ALL STUDENTS ==========")

    for student in students:
        print(f"ID     : {student[0]}")
        print(f"Name   : {student[1]}")
        print(f"Email  : {student[2]}")
        print(f"Phone  : {student[3]}")
        print(f"Course : {student[4]}")
        print(f"Year   : {student[5]}")
        print("----------------------------------")

    cursor.close()
    connection.close()

def update_student():
     connection = get_connection()
     cursor = connection.cursor()

     try:
         student_id = int(input("Enter student ID: "))
     except ValueError:
         print("Invalid student ID! Please enter a number.")
         cursor.close()
         connection.close()
         return
     email = input("Enter new email: ")
     phone = input("Enter new phone: ")
     course = input("Enter new course: ")
     try:
         year = int(input("Enter new year: "))
     except ValueError:
         print("Invalid year! Please enter a number.")
         cursor.close()
         connection.close()
         return

     if year<= 0:
         print("Invalid year! Year must be greater than 0.")
         cursor.close()
         connection.close()
         return

     query = """
        UPDATE students
        SET email = %s,
            phone = %s,
            course = %s,
            year = %s
        WHERE student_id = %s
    """
     cursor.execute(query, (email, phone, course, year, student_id))

     if cursor.rowcount== 0:
        print("Student not found!")
     else:
       connection.commit()
       print("student updated successfully!")

     cursor.close()
     connection.close()


def delete_student():
    connection = get_connection()
    cursor = connection.cursor()

    student_id = int(input("Enter student ID: "))

    query = """
        DELETE FROM students
        WHERE student_id = %s
    """

    cursor.execute(query, (student_id,))

    if cursor.rowcount == 0:
        print("Student not found!")
    else:
        connection.commit()
        print("Student deleted successfully!")

    cursor.close()
    connection.close()

def search_student():
    connection = get_connection()
    cursor = connection.cursor()

    search = input("Enter student name or email: ").strip()

    query = """
        SELECT *
        FROM students
        WHERE name ILIKE %s
           OR email ILIKE %s
    """

    search_pattern = f"%{search}%"

    cursor.execute(query, (search_pattern, search_pattern))
    students = cursor.fetchall()

    if not students:
        print("\nNo student found!")
    else:
        print("\n------ Search Results ------")

        for student in students:
            print(f"ID     : {student[0]}")
            print(f"Name   : {student[1]}")
            print(f"Email  : {student[2]}")
            print(f"Phone  : {student[3]}")
            print(f"Course : {student[4]}")
            print(f"Year   : {student[5]}")
            print("----------------------------")

    cursor.close()
    connection.close()
  