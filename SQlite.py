import sqlite3 as sq
# from employees import employee

# getinput = employee()

# name = getinput.name
# surname = getinput.surname
# age = getinput.age
# occupation = getinput.occupation 



conn = sq.connect("Employees.db")

c = conn.cursor()

# c.execute("""CREATE TABLE students (
#             name TEXT,
#             age INTEGER,
#             height REAL
#     )""")

# c.execute("""CREATE TABLE EmployeeInfo (
#     name TEXT,
#     surname TEXT,
#     age INTEGER,
#     occupation TEXT,
#     email TEXT
#     )""")

c.execute("INSERT INTO EmployeeInfo VALUES ('Justin', 'Maria', 5, 'Web Dev', 'email@gmail.com')")

conn.commit()

conn.close()