import mysql.connector as sql

obj = sql.connect(host='localhost', user='root', password='password', database='Hospital_Management_System')
cursor = obj.cursor()

query1 = 'select * from Patient'

cursor.execute(query1)
data = cursor.fetchall()

patients = []

for i in data:
    i = list(i)
    patients.append(i)

query2 = 'select * from Doctor'
cursor.execute(query2)
data = cursor.fetchall()

doctors = []

for i in data:
    i = list(i)
    doctors.append(i)



obj.close()