from Datbase import Database
import os

def main():
    flag = True
    log_file = open(os.path.join(os.getcwd(), "Logs", "Runtime_Details.txt"), 'w')
    database_log = os.path.join(os.getcwd(), "Logs", "Database_Operations.txt")
    db = Database(database_log)
    log_file.write("Database is created/found.\n")
    db.create_student_table()
    log_file.write("Student table is created/found.\n")
    db.create_teacher_table()
    log_file.write("Teacher table is created/found.\n")
    while flag:
        print("*****Educational Database*****")
        print("1. Insert Students")
        print("2. Insert Teachers")
        print("3. Marks Distribution of Subjects")
        print("4. Average marks of Subjects in Ascending Order")
        print("5. Marks Distribution of Courses")
        print("6. Most Experienced Teacher")
        print("7. Courses and Teachers")
        print("8. Delete Student Table")
        print("9. Delete Student Records")
        print("10. Delete Teacher Table")
        print("11. Delete Teacher Records")
        print("12. Display All Students")
        print("13. Display All Teachers")
        print("14. Search a Student")
        print("15. Search a Teacher")
        print("16: Delete Database")
        print("17. Exit")
        option = int(input("Enter you choice: "))
        log_file.write("Entered option "+str(option)+".\n")
        if option == 1:
            log_file.write("Inserting student details.\n")
            studentList = []
            insert = True
            while insert:
                print("Enter Details of the student: ")
                temp = []
                temp.append(int(input("Id: ")))
                temp.append(input("Name: "))
                temp.append(input("Grade: "))
                temp.append(int(input("Mobile No: ")))
                temp.append(input("Address: "))
                temp.append(float(input("Overall Score: ")))
                temp.append(float(input("Math Score: ")))
                temp.append(float(input("Physics Score: ")))
                temp.append(float(input("Chemistry Score: ")))
                temp.append(float(input("Computer Score: ")))
                temp.append(input("Course Name: "))
                temp = tuple(temp)
                studentList.append(temp)
                ch = input("Do you want to insert again?(Y/N)")
                if ch == 'N' or ch == 'n':
                    insert = False
            db.insert_student(studentList)
        elif option == 2:
            log_file.write("Inserting teacher details.\n")
            teacherList = []
            insert = True
            while insert:
                print("Enter Details of the teacher: ")
                temp = []
                temp.append(int(input("Id: ")))
                temp.append(input("Name: "))
                temp.append(int(input("Mobile No: ")))
                temp.append(input("Address: "))
                temp.append(input("Courses: "))
                temp.append(int(input("Experience: ")))
                temp = tuple(temp)
                teacherList.append(temp)
                ch = input("Do you want to insert again?(Y/N)")
                if ch == 'N' or ch == 'n':
                    insert = False
            db.insert_teacher(teacherList)
        elif option == 3:
            log_file.write("Extracting marks distribution.\n")
            temp = db.math_marks_distribution()
            print("Math Marks Distribution: ")
            for key in temp.keys():
                print(key, ": ", temp[key])
            temp = db.phy_marks_distribution()
            print("Physics Marks Distribution: ")
            for key in temp.keys():
                print(key, ": ", temp[key])
            temp = db.chem_marks_distribution()
            print("Chemistry Marks Distribution: ")
            for key in temp.keys():
                print(key, ": ", temp[key])
            temp = db.comp_marks_distribution()
            print("Computer Marks Distribution: ")
            for key in temp.keys():
                print(key, ": ", temp[key])
        elif option == 4:
            log_file.write("Extracting average of subjects in ascending order.\n")
            temp = db.subject_in_order()
            print("Average of all subjects in ascending order: ")
            for sub in temp:
                print(sub, end=" ")
            print()
        elif option == 5:
            log_file.write("Distribution of marks according to course.\n")
            temp = db.course_distribution()
            for course in temp.keys():
                print(course, ": ")
                print("Minimum: ", temp[course][0], "\tMaximum: ", temp[course][1], "\tMedian: ", temp[course][2])
        elif option == 6:
            log_file.write("Extracting most experienced teacher.\n")
            print("Most Experienced teacher: ", db.max_experienced())
        elif option == 7:
            log_file.write("Extracting teachers name of all courses.\n")
            temp = db.course_teachers()
            print("Courses and Teachers: ")
            for course in temp.keys():
                print(course, ":", end=' ')
                for teacher in temp[course]:
                    print(teacher, end=" ")
                print()
        elif option == 8:
            log_file.write("Deleting student table.\n")
            db.delete_student_table()
            print("Student table is deleted!")
        elif option == 9:
            log_file.write("Deleting all records of student table.\n")
            db.delete_all_student()
            print("All records of student table is deleted.")
        elif option == 10:
            log_file.write("Deleting teacher table.\n")
            db.delete_teacher_table()
            print("Teacher table is deleted.")
        elif option == 11:
            log_file.write("Deleting all records of teacher table.\n")
            db.delete_all_teacher()
            print("All records of teacher is deleted.")
        elif option == 12:
            log_file.write("Student details is displayed.\n")
            rows = db.print_student()
            for row in rows:
                print("Student Id ", row[0], ": ")
                print("Name: ", row[1])
                print("Grade: ", row[2])
                print("Mobile No: ", row[3])
                print("Address: ", row[4])
                print("Overall Score: ", row[5])
                print("Math Score: ", row[6])
                print("Physics Score: ", row[7])
                print("Chemistry Score: ", row[8])
                print("Computer Score: ", row[9])
                print("Course name: ", row[10])
        elif option == 13:
            log_file.write("Teacher details is displayed.\n")
            rows = db.print_teacher()
            for row in rows:
                print("Teacher Id ", row[0], ": ")
                print("Name: ", row[1])
                print("Mobile No: ", row[2])
                print("Address: ", row[3])
                print("All Courses: ", row[4])
                print("Overall Experience: ", row[5])
        elif option == 14:
            log_file.write("Searching student.\n")
            name = input("Enter student name: ")
            rows = db.search_student(name)
            print("All the students with this name: ")
            for row in rows:
                print("Student Id ", row[0], ": ")
                print("Name: ", row[1])
                print("Grade: ", row[2])
                print("Mobile No: ", row[3])
                print("Address: ", row[4])
                print("Overall Score: ", row[5])
                print("Math Score: ", row[6])
                print("Physics Score: ", row[7])
                print("Chemistry Score: ", row[8])
                print("Computer Score: ", row[9])
                print("Course name: ", row[10])
        elif option == 15:
            log_file.write("Searching teacher.\n")
            name = input("Enter teacher name: ")
            rows = db.search_teacher(name)
            print("All the teacher with this name: ")
            for row in rows:
                print("Teacher Id ", row[0], ": ")
                print("Name: ", row[1])
                print("Mobile No: ", row[2])
                print("Address: ", row[3])
                print("All Courses: ", row[4])
                print("Overall Experience: ", row[5])
        elif option == 16:
            log_file.write("Deleting database.\n")
            db.delete_database()
            print("Database deleted successfully!")
            print("Good Bye!")
            log_file.write("Program Terminated.\n")
            break
        elif option == 17:
            db.terminate()
            flag = False
            print("Good Bye!")
            log_file.write("Database Connection is Terminated.\n")
            log_file.write("Program Terminated.\n")
        else:
            print("Invalid Choice!")
            log_file.write("Invalid choice is given.")
    log_file.write("Closing runtime log file.\n")
    log_file.close()

if __name__ == '__main__':
    main()