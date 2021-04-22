import sqlite3
import datetime

conn = sqlite3.connect('bancodedados.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS course(
    course_id INTEGER PRIMARY KEY AUTOINCREMENT,
    coursename VARCHAR(50),
    studyarea VARCHAR(50)
);

''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS student(
    student_id INTEGER PRIMARY KEY AUTOINCREMENT, 
    course_id INTEGER,
    name VARCHAR(50),
    created DATETIME,
    age INTEGER,
    CPF VARCHAR(11)
);
''')

conn.commit()

def course(coursename,studyarea):
    acourse = ('INSERT INTO course'
              '(coursename, studyarea'
              'VALUES ?,?)')
    cursor.execute(acourse, (coursename,studyarea))
    course_id = cursor.lastrowid
    conn.commit
    print('The course id is:', course_id)

def student(name,created,age,cpf):
    astudent = ('INSERT INTO student'
                '(?,?,?,?)')
    cursor.execute(astudent, (name,created,age,cpf))
    student_id = cursor.lastrowid
    conn.commit
    print('The student id is: ', student_id)
        
def update_course(course_id,coursename,studyarea):
    ucourse = ('UPDATE course'
            'SET coursename = ?, studyarea = ?'
            'WHERE course_id = ?' )
    cursor.execute(ucourse(coursename,studyarea))
    conn.commit

def update_student(name,created,age,cpf):
    ustudent = ('UPDATE student'
            'SET name = ?, created = ?, age = ?, cpf = 9'
            'WHERE student_id = ?')
    cursor.execute(ustudent(name,created,age,cpf))
    conn.commit

def delete_course(course_id,coursename,studyarea):
    cursor.execute('DELETE FROM course WHERE course_id = ?', (course_id,))
    conn.commit()

def delete_student(name,created,age,cpf):
    cursor.execute('DELETE FROM student WHERE student_id = ?', (student_id,))
    conn.commit()
