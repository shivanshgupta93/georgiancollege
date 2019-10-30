"""
Using Python and SQLite (or SQL server if you desire) create a groups database
Create two tables one that contains the names and IDs of your group members and one that contains course names and course IDs
Create a one to many relationship between the two tables that show which students are in each course
"""

##We have created a database Data_Programming in SQL server and connecting to that

import pyodbc

con = pyodbc.connect("Driver={SQL Server Native Client 11.0};" "Server=localhost;" "Database=Data_Programming;" "Trusted_Connection=yes;")

cur = con.cursor()

students = []
courses = []

student_count = int(input("Total number of students are: "))

while student_count > 0:
    studentid = input("Enter Student Id: ")
    studentname = input("Enter Student Name: ")
    
    students.append((studentid, studentname))
    
    student_count -= 1
    
course_count = int(input("Total number of courses available: "))

while course_count > 0:
    courseid = input("Enter Course Id: ")
    coursename = input("Enter Course Name: ")
    coursestudentid = input("Enter Students taking this course (seprate by comma): ")
    courselst = coursestudentid.split(",")
    
    for row in courselst:
        print(row)
        courses.append((courseid, coursename, row))
        
    course_count -= 1

count_qry = "SELECT COUNT(1) FROM Data_Programming.INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME ='Students'"
cur.execute(count_qry)
count = cur.fetchone()

if count[0] == 1:
    drop_qry = 'DROP TABLE Students'
    cur.execute(drop_qry)

create_qry = 'CREATE TABLE Students (StudentId Varchar(50), StudentName Varchar(100))'
cur.execute(create_qry)

count_qry = "SELECT COUNT(1) FROM Data_Programming.INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME ='Courses'"
cur.execute(count_qry)
count = cur.fetchone()

if count[0] == 1:
    drop_qry = 'DROP TABLE Courses'
    cur.execute(drop_qry)

create_qry = 'CREATE TABLE Courses (CourseId Varchar(50), CourseName Varchar(100), StudentId Varchar(50))'
cur.execute(create_qry)

insert_qry = "INSERT INTO Students VALUES (?,?)"
cur.executemany(insert_qry, students)

insert_qry = "INSERT INTO Courses VALUES (?,?,?)"
cur.executemany(insert_qry, courses)

con.commit()

select_qry = "SELECT S.STUDENTID, S.STUDENTNAME, C.COURSEID, C.COURSENAME FROM STUDENTS S JOIN COURSES C ON S.STUDENTID = C.STUDENTID"
cur.execute(select_qry)
select_rs = cur.fetchall()

print(select_rs)