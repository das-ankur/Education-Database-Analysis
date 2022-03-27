import sqlite3
from sqlite3 import Error
import statistics
import numpy as np
import os

class Database:
    def __init__(self, log_file_path):
        self.log_file = open(log_file_path, "w")
        try:
            self.sqliteConnection = sqlite3.connect('educationDB.db')
            self.cursor = self.sqliteConnection.cursor()
            self.log_file.write("Database created and Successfully Connected to SQLite\n")
        except sqlite3.Error as error:
            self.log_file.write("Error while connecting to sqlite", error+"\n")

    def create_student_table(self):
        """"
        self.cursor.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='students' ''')
        if self.cursor.fetchone()[0] == 1:
            self.log_file.write("Student table already exists.")
        else:
        """
        try:
            create_student_table = """CREATE TABLE IF NOT EXISTS students (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    grade text NOT NULL,
                                    mobile int NOT NULL,
                                    address text NOT NULL,
                                    overall_score float NOT NULL,
                                    math_score float NOT NULL,
                                    phy_score float NOT NULL,
                                    chem_score float NOT NULL,
                                    comp_score float NOT NULL,
                                    course text NOT NULL
                                ); """
            self.cursor.execute(create_student_table)
            self.log_file.write("Student table is created successfully!\n")
        except Error as e:
            self.log_file.write(str(e)+"\n")

    def create_teacher_table(self):
        try:
            create_student_table = """CREATE TABLE IF NOT EXISTS teachers (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    mobile int NOT NULL,
                                    address text NOT NULL,
                                    courses_teaching text NOT nULL,
                                    overall_experience int NOT NULL
                                ); """
            self.cursor.execute(create_student_table)
            self.log_file.write("Teacher table is created successfully!\n")
        except Error as e:
            self.log_file.write(str(e)+"\n")

    def math_marks_distribution(self):
        statement = '''SELECT math_score from students;'''
        self.cursor.execute(statement)
        marks = self.cursor.fetchall()
        self.log_file.write("Math marks are fetched from student table.\n")
        marks = [mark[0] for mark in marks]
        output = {}
        output['min'] = min(marks)
        output['max'] = max(marks)
        output['median'] = statistics.median(marks)
        output['mean'] = np.mean(marks)
        self.log_file.write("Math marks distribution is generated successfully!\n")
        return output

    def phy_marks_distribution(self):
        statement = '''SELECT phy_score from students;'''
        self.cursor.execute(statement)
        marks = self.cursor.fetchall()
        self.log_file.write("Physics marks are fetched from student table.\n")
        marks = [mark[0] for mark in marks]
        output = {}
        output['min'] = min(marks)
        output['max'] = max(marks)
        output['median'] = statistics.median(marks)
        output['mean'] = np.mean(marks)
        self.log_file.write("Physics marks distribution is generated successfully!\n")
        return output

    def chem_marks_distribution(self):
        statement = '''SELECT chem_score from students;'''
        self.cursor.execute(statement)
        marks = self.cursor.fetchall()
        self.log_file.write("Chemistry marks are fetched from student table.\n")
        marks = [mark[0] for mark in marks]
        output = {}
        output['min'] = min(marks)
        output['max'] = max(marks)
        output['median'] = statistics.median(marks)
        output['mean'] = np.mean(marks)
        self.log_file.write("Chemistry marks distribution is generated successfully!\n")
        return output

    def comp_marks_distribution(self):
        statement = '''SELECT comp_score from students;'''
        self.cursor.execute(statement)
        marks = self.cursor.fetchall()
        self.log_file.write("Computer marks are fetched from student table.\n")
        marks = [mark[0] for mark in marks]
        output = {}
        output['min'] = min(marks)
        output['max'] = max(marks)
        output['median'] = statistics.median(marks)
        output['mean'] = np.mean(marks)
        self.log_file.write("Computer marks distribution is generated successfully!\n")
        return output

    def subject_in_order(self):
        sub_marks = {}
        statement = '''SELECT math_score, phy_score, chem_score, comp_score from students;'''
        self.log_file.write("All marks are fetched successfully!\n")
        self.cursor.execute(statement)
        marks = self.cursor.fetchall()
        math_list = []
        phy_list = []
        chem_list = []
        comp_list = []
        for row in marks:
            math_list.append(row[0])
            phy_list.append(row[1])
            chem_list.append(row[2])
            comp_list.append(row[3])
        sub_marks['Math'] = np.mean(math_list)
        sub_marks['Physics'] = np.mean(phy_list)
        sub_marks['Chemistry'] = np.mean(chem_list)
        sub_marks['Computer'] = np.mean(comp_list)
        res = dict(sorted(sub_marks.items(), key=lambda item: item[1]))
        self.log_file.write("Subject list is returned!\n")
        return res.keys()

    def course_distribution(self):
        course_marks = {}
        statement = '''SELECT overall_score, course from students;'''
        self.cursor.execute(statement)
        rows = self.cursor.fetchall()
        self.log_file.write("overall_score and course data is fetched successfully from student table!\n")
        for row in rows:
            if row[1] not in course_marks.keys():
                course_marks[row[1]] = [row[0]]
            else:
                course_marks[row[1]].append(row[0])
        res = {}
        for key in course_marks.keys():
            res[key] = [min(course_marks[key]), max(course_marks[key]), statistics.median(course_marks[key])]
        self.log_file.write("Course marks distribution is generated successfully!\n")
        return res

    def max_experienced(self):
        statement = '''SELECT name, max(overall_experience) from teachers;'''
        self.cursor.execute(statement)
        self.log_file.write("Teacher name with maximum experienced is fetched.\n")
        return self.cursor.fetchall()[0][0]

    def course_teachers(self):
        statement = '''SELECT name, courses_teaching from teachers;'''
        self.cursor.execute(statement)
        rows = self.cursor.fetchall()
        self.log_file.write("name and course are fetched successfully from teacher table.\n")
        res = {}
        for row in rows:
            courses = row[1].split(',')
            courses = [course.strip() for course in courses]
            for course in courses:
                if course not in res.keys():
                    res[course] = [row[0]]
                else:
                    res[course].append(row[0])
        self.log_file.write("Course  and corresponding teacher details is generated successfully.\n")
        return res

    def insert_student(self, student_val):
        # student_val is list of tuples
        for idx in range(len(student_val)):
            if len(student_val[idx]) != 11:
                self.log_file.write(str(student_val[idx])+" is invalid record\n")
                student_val.pop(idx)
        if len(student_val) == 0:
            self.log_file.write("All records are invalid!\n")
        else:
            try:
                sqlite_insert_query = """INSERT INTO students
                                    ('id', 'name', 'grade', 'mobile', 'address', 'overall_score',  'math_score', 'phy_score', 'chem_score', 'comp_score', 'course') 
                                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
                self.cursor.executemany(sqlite_insert_query, student_val)
                self.sqliteConnection.commit()
                self.log_file.write("Total "+str(self.cursor.rowcount)+" records inserted successfully into SqliteDb_developers table.\n")
                self.sqliteConnection.commit()
            except sqlite3.Error as error:
                self.log_file.write("Failed to insert multiple records into student table :" + str(error)+"\n")
            finally:
                self.log_file.write("Valid records are inserted in student table!\n")

    def delete_all_student(self):
        statement = "DELETE FROM students;"
        self.cursor.execute(statement)
        self.sqliteConnection.commit()
        self.log_file.write("All records from student table is deleted.\n")

    def delete_student_table(self):
        statement = "Drop table students;"
        self.cursor.execute(statement)
        self.sqliteConnection.commit()
        self.log_file.write("Students table is deleted.\n")

    def insert_teacher(self, teacher_val):
        # teacher_val is list of tuples
        for idx in range(len(teacher_val)):
            if len(teacher_val[idx]) != 6:
                self.log_file.write(str(teacher_val[idx]) + " is invalid record.\n")
                teacher_val.pop(idx)
        else:
            try:
                sqlite_insert_query = """INSERT INTO teachers
                                    ('id', 'name', 'mobile', 'address', 'courses_teaching', 'overall_experience') 
                                    VALUES (?, ?, ?, ?, ?, ?);"""
                self.cursor.executemany(sqlite_insert_query, teacher_val)
                self.sqliteConnection.commit()
                self.log_file.write("Total "+str(self.cursor.rowcount)+" records inserted successfully into SqliteDb_developers table.\n")
                self.sqliteConnection.commit()
            except sqlite3.Error as error:
                self.log_file.write("Failed to insert multiple records into teacher table" + str(error)+"\n")
            finally:
                self.log_file.write("Valid records are inserted in teacher table!\n")

    def delete_all_teacher(self):
        statement = "DELETE FROM teachers;"
        self.cursor.execute(statement)
        self.sqliteConnection.commit()
        self.log_file.write("All records from teachers table is deleted.\n")

    def delete_teacher_table(self):
        statement = "Drop table teachers;"
        self.cursor.execute(statement)
        self.sqliteConnection.commit()
        self.log_file.write("Teachers table is deleted.\n")

    def show_table_names(self):
        try:
            sql_query = """SELECT name FROM sqlite_master WHERE type='table';"""
            # executing our sql query
            self.cursor.execute(sql_query)
            self.log_file.write("List of table: ")
            # printing all tables list
            self.log_file.write(str(self.cursor.fetchall())+'\n')
        except sqlite3.Error as error:
            print("Failed to execute the above query", error+'\n')

    def search_teacher(self, teacher_name):
        statement = "SELECT * from teachers where name like '%"+teacher_name+"%';"
        self.cursor.execute(statement)
        rows = self.cursor.fetchall()
        self.log_file.write("All teachers details with name "+str(teacher_name)+" is fetched successfully.\n")
        return rows

    def search_student(self, student_name):
        statement = "SELECT * from students where name like '%"+student_name+"%';"
        self.cursor.execute(statement)
        rows = self.cursor.fetchall()
        self.log_file.write("All students details with name "+str(student_name)+" is fetched successfully.\n")
        return rows

    def print_student(self):
        statement = "SELECT * from students;"
        self.cursor.execute(statement)
        rows = self.cursor.fetchall()
        self.log_file.write("All  student details are fetched.\n")
        return rows

    def print_teacher(self):
        statement = "SELECT * from teachers;"
        self.cursor.execute(statement)
        rows = self.cursor.fetchall()
        self.log_file.write("All teacher details are fetched.\n")
        return rows

    def terminate(self):
        self.log_file.write("Connection with database is terminating.\n")
        self.log_file.close()
        self.sqliteConnection.close()

    def delete_database(self):
        self.sqliteConnection.close()
        os.remove('educationDB.db')
        self.log_file.write("Database is deleted!\n")