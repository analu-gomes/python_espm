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
              '(coursename, studyarea)'
              'VALUES (?,?)')
    cursor.execute(acourse,(coursename,studyarea))
    course_id = cursor.lastrowid
    conn.commit()
    print('The course id is:', course_id)

def student (name,created,age,cpf):
    astudent = ('INSERT INTO student'
                '(name, created, age, cpf)'
                'VALUES (?,?,?,?)')
    cursor.execute (astudent,(name,created,age,cpf))
    student_id = cursor.lastrowid
    conn.commit()
    print('The student id is: ', student_id)
        
def update_course(course_id,coursename,studyarea):
    ucourse = ('UPDATE course '
            'SET coursename = ?, studyarea = ? '
            'WHERE course_id = ?')
    cursor.execute(ucourse,(coursename,studyarea,course_id))
    conn.commit()

def update_student(name,created,age,cpf,student_id):
    ustudent = ('UPDATE student '
            'SET name = ?, created = ?, age = ?, cpf = ? '
            'WHERE student_id = ?')
    cursor.execute(ustudent,(name,created,age,cpf,student_id))
    conn.commit()

def delete_course(course_id):
    cursor.execute('DELETE FROM course WHERE course_id = ?', (course_id,))
    conn.commit()

def delete_student(student_id):
    cursor.execute('DELETE FROM student WHERE student_id = ?', (student_id,))
    conn.commit()

coursename = input('Insira o nome do curso: ')
studyarea = input('Insira a área do curso: ')
course(coursename,studyarea)


name = input('Nome do estudante: ')
created = input('Data de matrícula: ')
created = datetime.datetime.strptime(created,'%d/%m/%Y').date()
age = int(input('Idade: '))
cpf = int(input('CPF: '))
student(name,created,age,cpf)

all_students = cursor.execute('''SELECT *
            FROM student''')
st = cursor.fetchall()
all_courses = cursor.execute('''SELECT *
            FROM course''')
co = cursor.fetchall() 
for s in st:
    print(s)
for c in co:
    print(c)

course_id = int(input('Insira o código do curso: '))
coursename = input('Insira o nome do curso: ')
studyarea = input('Insira área de estudo: ')
update_course(course_id,coursename,studyarea) 


student_id = int(input('Insira o id do estudante: '))
name = input('Nome do estudante: ')
created = input('Data de matrícula: ')
created = datetime.datetime.strptime(created,'%d/%m/%Y').date()
age = int(input('Idade: '))
cpf = int(input('CPF: '))
update_student(name,created,age,cpf,student_id)

course_id = int(input('Insira o código do curso'))
delete_course(course_id)

student_id= int(input('Insira o código do estudante'))
delete_student(student_id)

conn.close()
