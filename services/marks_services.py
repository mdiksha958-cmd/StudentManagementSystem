from database.connection import get_connection

def add_marks():
    
    subject = input("Enter subject: ").strip()
     
    if not subject:
        print("Subject cannot be empty!")
        return
    while True:
     marks_input = input("Enter marks: ").strip()

     if not marks_input.isdigit():
        print("Invalid marks! Please enter a number.")
        continue

     marks = int(marks_input)

     if marks < 0 or marks > 100:
        print("Marks must be between 0 and 100.")
        continue

     break 

    student_id = int(input("Enter student ID: "))

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        INSERT INTO marks (student_id, subject, marks)
        VALUES (%s, %s, %s)
    """

    cursor.execute(query, (student_id, subject, marks))

    connection.commit()

    cursor.close()
    connection.close()

    print("Marks added successfully!")
 


def view_marks():
    connection = get_connection()
    cursor = connection.cursor()

    query = """
        SELECT
            marks.mark_id,
            students.name,
            marks.subject,
            marks.marks
        FROM marks
        JOIN students
        ON marks.student_id = students.student_id
    """

    cursor.execute(query)
    records = cursor.fetchall()

    print("\n------ Marks Details ------")

    for record in records:
        print(f"Mark ID    : {record[0]}")
        print(f"Name       : {record[1]}")
        print(f"Subject    : {record[2]}")
        print(f"Marks      : {record[3]}")
        print("---------------------------")

    cursor.close()
    connection.close()

def update_marks():
    connection = get_connection()
    cursor = connection.cursor()

    mark_id_input = input("Enter mark ID: ").strip()

    if not mark_id_input.isdigit():
        print("Invalid mark ID! Please enter a number.")
        cursor.close()
        connection.close()
        return

    mark_id = int(mark_id_input)

    marks_input = input("Enter new marks: ").strip()

    if not marks_input.isdigit():
        print("Invalid marks! Please enter a number.")
        cursor.close()
        connection.close()
        return

    marks = int(marks_input)

    if marks < 0 or marks > 100:
        print("Marks must be between 0 and 100.")
        cursor.close()
        connection.close()
        return

    query = """
        UPDATE marks
        SET marks = %s
        WHERE mark_id = %s
    """

    cursor.execute(query, (marks, mark_id))

    if cursor.rowcount == 0:
        print("Mark record not found!")
    else:
        connection.commit()
        print("Marks updated successfully!")

    cursor.close()
    connection.close()

def delete_marks():
    connection = get_connection()
    cursor = connection.cursor()

    mark_id_input = input("Enter mark ID: ").strip()

    if not mark_id_input.isdigit():
        print("Invalid mark ID! Please enter a number.")
        cursor.close()
        connection.close()
        return

    mark_id = int(mark_id_input)

    query = """
        DELETE FROM marks
        WHERE mark_id = %s
    """

    cursor.execute(query, (mark_id,))

    if cursor.rowcount == 0:
        print("Mark record not found!")
    else:
        connection.commit()
        print("Marks deleted successfully!")

    cursor.close()
    connection.close()