
import sqlite3

Student = '''CREATE TABLE Student(
             StudentID NUMBER(10) NOT NULL,
             Name      VARCHAR2(30),
             Address   VARCHAR2(30),
             GradYear  NUMBER(4),

            CONSTRAINT S_PK
            Primary Key(StudentID) );'''

Course = '''CREATE TABLE Course(
            CName      VARCHAR2(25),
            Department VARCHAR2(20),
            Credits    NUMBER(2),

            CONSTRAINT C_PK
            Primary Key(CName));'''

Grade = '''CREATE TABLE Grade(
           CName        VARCHAR2(25) NOT NULL,
           StudentID    NUMBER(10) NOT NULL,
           CGrade       NUMBER(3,2),

           CONSTRAINT G_PK
           Primary Key(CName, StudentID),

           CONSTRAINT G_FK1
           FOREIGN KEY(StudentID)
           REFERENCES Student(StudentID),
           CONSTRAINT G_FK2
           FOREIGN KEY(CName)
           REFERENCES Course(CName));'''

conn = sqlite3.connect('Midterm.db')
cursor = conn.cursor()
cursor.execute('DROP TABLE IF EXISTS Student')
cursor.execute('DROP TABLE IF EXISTS Course')
cursor.execute('DROP TABLE IF EXISTS Grade')

cursor.execute(Student)
cursor.execute(Course)
cursor.execute(Grade)

studentTable = ["INSERT INTO  Student VALUES(9891213001, 'Yakama Hochiba', 'Chicago', 2020);",
                "INSERT INTO  Student VALUES(9891213002, 'Mazaki Ohitaki', 'California', 2019);",
                "INSERT INTO  Student VALUES(9891213003, 'Satona Kabayai', 'New York', 2010);",
                "INSERT INTO  Student VALUES(9891213004, 'Kayama Jochiban', 'Washington', 2012);",
                "INSERT INTO  Student VALUES(9891213005, 'Zazaki Itabishi', 'Chicago', 2020);"]

courseTable = ["INSERT INTO  Course VALUES('Database', 'Computer Science', 4);",
               "INSERT INTO  Course VALUES('Data Structure', 'Computer Science', 4);",
               "INSERT INTO  Course VALUES('Big Data Technologies', 'Computer Science', 4);",
               "INSERT INTO  Course VALUES('Calculus III', 'Mathematics', 4);",
               "INSERT INTO  Course VALUES('Music', 'Drama', 4);"]

gradeTable = ["INSERT INTO  Grade VALUES('Database', 9891213002, 4.00);",
              "INSERT INTO  Grade VALUES('Database', 9891213003, 4.00);",
              "INSERT INTO  Grade VALUES('Big Data Technologies', 9891213002, 4.00);",
              "INSERT INTO  Grade VALUES('Big Data Technologies', 9891213004, 3.75);",
              "INSERT INTO  Grade VALUES('Big Data Technologies', 9891213005, 4.00);",
              "INSERT INTO  Grade VALUES('Calculus III', 9891213002, 3.50);",
              "INSERT INTO  Grade VALUES('Calculus III', 9891213003, 3.50);",
              "INSERT INTO  Grade VALUES('Calculus III', 9891213004, 4.00);",
              "INSERT INTO  Grade VALUES('Calculus III', 9891213005, 3.50);",
              "INSERT INTO  Grade VALUES('Music', 9891213002, 4.00);"]

for row in studentTable:
    cursor.execute(row)
for row in courseTable:
    cursor.execute(row)
for row in gradeTable:
    cursor.execute(row)

preJoin = '''CREATE VIEW Student_View AS
             SELECT StudentID, Name, Address, Gradyear,
                    Cname, Department, Credits,
                    Cgrade
             FROM   Student
                    NATURAL LEFT OUTER JOIN Grade
                    NATURAL LEFT OUTER JOIN Course
             UNION ALL
             SELECT StudentID, Name, Address, Gradyear,
                    Cname, Department, Credits,
                    Cgrade
             FROM   Course
                    NATURAL LEFT OUTER JOIN Grade
                    NATURAL LEFT OUTER JOIN Student
              WHERE StudentID IS NULL;'''

cursor.execute('DROP VIEW IF EXISTS Student_View')
cursor.execute(preJoin)
conn.commit()

with open('Midterm_Part4B.txt', 'wb') as outfile:

    res = cursor.execute('SELECT * FROM Student_View;')
    res2 = res.fetchall()

    for rows in res2:
        row = ','.join([str(i) for i in rows]) + '\n'
        outfile.write(row.encode())

conn.close()


