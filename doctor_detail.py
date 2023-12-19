import tkinter as tk
from tkinter import ttk
import connect

def doctor_detail():
    WINDOW_HEIGHT = 700
    WINDOW_WIDTH = 1250
    
    X_COORDINATE = 100
    Y_COORDINATE = 70
    
    root = tk.Tk()
    root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{X_COORDINATE}+{Y_COORDINATE}")
    root.title("Hospital Mangement System")
    root.resizable(False, False)
    
    tk.Label(root, text="DOCTOR RECORDS", width=50, height=2, bg='#c36464', fg='#fff', font=('algerian', 30)).place(x=0, y=0)
    
    table = ttk.Treeview(root, columns=('f_name', 'l_name', 'gender', 'age', 'mobile_no', 'email', 'experience', 'education', 'specialization'), show='headings', height=27, xscrollcommand=True)
    
    verscrlbar = ttk.Scrollbar(root, orient ="vertical", command = table.yview).pack(side ='right', fill ='x')
    table.configure(xscrollcommand=verscrlbar)
    
    table.heading('f_name', text="First Name")
    table.heading('l_name', text='Last Name')
    table.heading('gender', text="Gender")
    table.heading('age', text="Age")
    table.heading('mobile_no', text="Mobile Number")
    table.heading('email', text="Email")
    table.heading('experience', text="Experience")
    table.heading('education', text="Education")
    table.heading('specialization', text="Specialization")

    column_widths = {'f_name': 150, 'l_name': 100, 'gender': 80, 'age': 80, 'mobile_no': 150, 'email': 200, 'experience': 150, 'education': 150, 'specialization': 150}
    for col, width in column_widths.items():
        table.column(col, width=width)
    
    for x in range(len(connect.doctors)):
        f_name = connect.doctors[x][0]
        l_name = connect.doctors[x][1]
        gender = connect.doctors[x][2]
        age = connect.doctors[x][3]
        mobile = connect.doctors[x][4]
        email = connect.doctors[x][5]
        experience = connect.doctors[x][6]
        education = connect.doctors[x][7]
        specialization = connect.doctors[x][8]
    
        values = (f_name, l_name, gender, age, mobile, email, experience, education, specialization)
    
        table.insert('', index=1, values=values)
    
    
    
    table.place(x=20, y=116)
    
    root.mainloop()