import tkinter as tk

from doctor_detail import doctor_detail
from doctor import doctor
from patient import patient
from patient_detail import patient_detail
from prescription import prescription

import mysql.connector as sql
from PIL import Image, ImageTk

def b1():
    patient()

def b2():
    patient_detail()

def b3():
    doctor()

def b4():
    doctor_detail()
    
def b5():
    prescription()

def get_total_patients():
    obj = sql.connect(host='localhost', user='root', password='password', database='Hospital_Management_System')
    cursor = obj.cursor()

    query = f"SELECT COUNT(email) AS total_patients FROM Patient;"
    cursor.execute(query)

    total_patients = cursor.fetchone()[0]

    return total_patients

def get_total_doctors():
    obj = sql.connect(host='localhost', user='root', password='password', database='Hospital_Management_System')
    cursor = obj.cursor()

    query = f"SELECT COUNT(email) AS total_patients FROM Doctor;"
    cursor.execute(query)

    total_doctors = cursor.fetchone()[0]

    return total_doctors

WINDOW_HEIGHT = 700
WINDOW_WIDTH = 1185

X_COORDINATE = 100
Y_COORDINATE = 70

root = tk.Tk()
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{X_COORDINATE}+{Y_COORDINATE}")
root.title("Hospital Mangement System")
root.resizable(False, False)
root.config(bg='#fff')

sidebar = tk.Frame(root, bg='#363062', width=238, height=700, borderwidth=2, relief=tk.SOLID).place(x=0, y=0)

heading = tk.Label(root, text="Hospital Management System", width=19, height=3, bg='#435585', fg='#fff', font=('comic sans ms', 15), wraplength=200).place(x=2, y=2)

button1 = tk.Button(root, text="Patients", width=17, height=2, font=('comic sans ms', 16), bg='#363062', fg='#F5E8C7', borderwidth=1, command=b1).place(x=2, y=92) 
button2 = tk.Button(root, text="Patients Records", width=17, height=2, font=('comic sans ms', 16), bg='#363062', fg='#F5E8C7', borderwidth=1, command=b2).place(x=2, y=170)

button3 = tk.Button(root, text="Doctors", width=17, height=2, font=('comic sans ms', 16), bg='#363062', fg='#F5E8C7', borderwidth=1, command=b3).place(x=2, y=248)
button4 = tk.Button(root, text="Doctors Records", width=17, height=2, font=('comic sans ms', 16), bg='#363062', fg='#F5E8C7', borderwidth=1, command=b4).place(x=2, y=326)

button5 = tk.Button(root, text="Prescription", width=17, height=2, font=('comic sans ms', 16), bg='#363062', fg='#F5E8C7', borderwidth=1, command=b5).place(x=2, y=404)

frame1 = tk.Frame(root, width=880, height=470, bg='lightgrey').place(x=270, y=25)

frame1_logo1 = Image.open('img/banner.png').resize((880, 470))
frame1_logo_img = ImageTk.PhotoImage(frame1_logo1)
frame1_label_img = tk.Label(root, image=frame1_logo_img, borderwidth=0).place(x=270, y=25)

frame2 = tk.Frame(root, width=400, height=150, bg='lightgrey').place(x=270, y=540)
frame2_label1 = tk.Label(root, text="Total Patients", font=('arial', 15), bg='lightgrey').place(x=440, y=570)
frame2_label2 = tk.Label(root, text=f"{get_total_patients()}", font=('arial', 45), bg='lightgrey').place(x=450, y=600) 

frame2_logo1 = Image.open('img/patient.jpg').resize((150, 100))
frame2_logo_img = ImageTk.PhotoImage(frame2_logo1)
frame2_label_img = tk.Label(root, image=frame2_logo_img, borderwidth=0).place(x=270, y=560)


frame3 = tk.Frame(root, width=400, height=150, bg='lightgrey').place(x=750, y=540)
frame3_label1 = tk.Label(root, text="Total Doctors", font=('arial', 15), bg='lightgrey').place(x=910, y=570)
frame3_label2 = tk.Label(root, text=f"{get_total_doctors()}", font=('arial', 45), bg='lightgrey').place(x=920, y=600) 

frame3_logo1 = Image.open('img/doctor.jpg').resize((150, 150))
frame3_logo_img = ImageTk.PhotoImage(frame3_logo1)
frame3_label_img = tk.Label(root, image=frame3_logo_img, borderwidth=0).place(x=750, y=540)


root.mainloop()

