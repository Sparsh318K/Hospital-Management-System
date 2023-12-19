import tkinter as tk
from tkinter import ttk
import connect

def patient_detail():
        
    WINDOW_HEIGHT = 700
    WINDOW_WIDTH = 1250
    
    X_COORDINATE = 100
    Y_COORDINATE = 70
    
    root = tk.Tk()
    root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{X_COORDINATE}+{Y_COORDINATE}")
    root.title("Hospital Mangement System")
    root.resizable(False, False)
    
    tk.Label(root, text="PATIENT RECORDS", width=50, height=2, bg='#c36464', fg='#fff', font=('algerian', 30)).place(x=0, y=0)
    
    table = ttk.Treeview(root, columns=('name', 'dob', 'gender', 'age', 'mobile_no', 'email', 'condition', 'surgeries', 'medication'), show='headings', height=27, xscrollcommand=True)
    
    verscrlbar = ttk.Scrollbar(root, orient ="vertical", command = table.yview).pack(side ='right', fill ='x')
    table.configure(xscrollcommand=verscrlbar)
    
    table.heading('name', text="Full Name")
    table.heading('dob', text='Date of Birth')
    table.heading('gender', text="Gender")
    table.heading('age', text="Age")
    table.heading('mobile_no', text="Mobile Number")
    table.heading('email', text="Email")
    table.heading('condition', text="Condition")
    table.heading('surgeries', text="Surgeries")
    table.heading('medication', text="Medication (if any)")

    column_widths = {'name': 150, 'dob': 100, 'gender': 80, 'age': 80, 'mobile_no': 150, 'email': 200, 'condition': 150, 'surgeries': 150, 'medication': 150}
    for col, width in column_widths.items():
        table.column(col, width=width)
    
    for x in range(len(connect.patients)):
        email = connect.patients[x][0]
        name = connect.patients[x][1]
        dob = connect.patients[x][2]
        gender = connect.patients[x][3]
        age = connect.patients[x][4]
        mobile = connect.patients[x][5]
        condition = connect.patients[x][6]
        surgeries = connect.patients[x][7]
        medication = connect.patients[x][8]
    
        values = (name, dob, gender, age, mobile, email, condition, surgeries, medication)
    
        table.insert('', index=1, values=values)
    
    
    
    table.place(x=20, y=116)
    
    root.mainloop()