from services.student_services import (
      add_student, 
      view_students,
      update_student,
      delete_student,
      search_student
)

from services.marks_services import (
    add_marks,
    view_marks,
    update_marks,
    delete_marks
)

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Add Marks")
    print("6. View Marks")
    print("7. Update Marks")
    print("8. Delete Marks")
    print("9. Search Student")
    print("10. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        add_student()

    elif choice == "2":
         view_students()
        

    elif choice == "3":
        update_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        add_marks()

    elif choice == "6":
        view_marks()

    elif choice == "7":
        update_marks()

    elif choice == "8":
        delete_marks()

    elif choice == "9":
        search_student()

    elif choice == "10":
        print("Thank you for using Student Management System! ")
        break
        
    else:
        print("Invalid choice! Please try again.")
        
        
