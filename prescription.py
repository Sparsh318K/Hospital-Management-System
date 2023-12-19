import tkinter as tk
from tkinter import ttk
import mysql.connector as sql

import connect

def prescription():
    def destroy():
        root.destroy()

    def clear():
        input1.set('Select a option')
        for data in inputs:
            data.delete(0, tk.END)

    def submit():
        prescription = []
        data = []

        for x, y in enumerate(inputs):
            if x == 0:
                new = y.get()
                new = new[0 : new.find(" ")]
                data.append(new)
            else:
                data.append(y.get())

        prescription.append(data)
        print(prescription)
        
        obj = sql.connect(host='localhost', user='root', password='password', database='Hospital_Management_System')

        cursor = obj.cursor()

        query = f"INSERT INTO Prescription (patient, blood_group, disease, cure, medicine, dose_days, issue_date, expiry_date, side_effect, daily_dose) VALUES ('{prescription[0][0]}', '{prescription[0][1]}', '{prescription[0][2]}', '{prescription[0][3]}', '{prescription[0][4]}', {prescription[0][5]}, '{prescription[0][6]}', '{prescription[0][7]}', '{prescription[0][8]}', '{prescription[0][9]}');"

        cursor.execute(query)

        obj.commit()
        cursor.close()
        obj.close()
        clear()

    def get_all_patient():
        patient = connect.patients
        global options
        options = []

        for x in patient:
            options.append([x[0], x[1]])
        
        options = tuple(options)
        return options

    
    WINDOW_HEIGHT = 700
    WINDOW_WIDTH = 1250
    
    X_COORDINATE = 100
    Y_COORDINATE = 70
    
    root = tk.Tk()
    root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{X_COORDINATE}+{Y_COORDINATE}")
    root.title("Hospital Mangement System")
    root.resizable(False, False)
    root.config(bg='#06283D')
    
    tk.Label(root, text="PRESCRIPTION", width=50, height=2, bg='#c36464', fg='#fff', font=('algerian', 30)).place(x=0, y=0)
    
    # Frame 1
    frame1 = tk.LabelFrame(root, text='Prescription', font=20, bd=2, width=970, height=510, relief='groove', bg='#ededed', fg='#06283d').place(x=30, y=150)
    
    tk.Label(root, text="Patient", font=('arial', 17), bg='#ededed', fg='#06283d').place(x=60, y=180)
    input1 = ttk.Combobox(root, textvariable=tk.StringVar, width=37, font=('arial', 10))
    input1['values'] = get_all_patient()
    input1.set('Select a option')
    input1['state'] = 'readonly'
    input1.place(x=170, y=184)
    
    tk.Label(root, text="Blood Group", font=('arial', 17), bg='#ededed', fg='#06283d').place(x=480, y=180)
    input2 = tk.Entry(root, width=25, font=('arial', 15))
    input2.place(x=620, y=182)
    
    tk.Label(root, text="Disease", font=('arial', 17), bg='#ededed', fg='#06283d').place(x=60, y=260)
    input3 = tk.Entry(root, width=25, font=('arial', 15))
    input3.place(x=170, y=262)
    
    tk.Label(root, text="Cure", font=('arial', 17), bg='#ededed', fg='#06283d').place(x=480, y=260)
    input4 = tk.Entry(root, width=25, font=('arial', 15))
    input4.place(x=620, y=262)

    tk.Label(root, text="Medicine", font=('arial', 17), bg='#ededed', fg='#06283d').place(x=60, y=340)
    input5 = tk.Entry(root, width=25, font=('arial', 15))
    input5.place(x=170, y=342)

    tk.Label(root, text="Dose (days)", font=('arial', 17), bg='#ededed', fg='#06283d').place(x=480, y=340)
    input6 = tk.Entry(root, width=25, font=('arial', 15))
    input6.place(x=620, y=342)
    
    tk.Label(root, text="Issue Date", font=('arial', 17), bg='#ededed', fg='#06283d').place(x=55, y=420)
    input7 = tk.Entry(root, width=25, font=('arial', 15))
    input7.place(x=170, y=422)

    tk.Label(root, text="Exp. Date", font=('arial', 17), bg='#ededed', fg='#06283d').place(x=480, y=420)
    input8 = tk.Entry(root, width=25, font=('arial', 15))
    input8.place(x=620, y=422)
    
    tk.Label(root, text="Side Effect", font=('arial', 17), bg='#ededed', fg='#06283d').place(x=55, y=500)
    input9 = tk.Entry(root, width=25, font=('arial', 15))
    input9.place(x=170, y=502)

    tk.Label(root, text="Daily Dose", font=('arial', 17), bg='#ededed', fg='#06283d').place(x=480, y=500)
    input10 = tk.Entry(root, width=25, font=('arial', 15))
    input10.place(x=620, y=502)
    # Sidebar

    inputs = [input1, input2, input3, input4, input5, input6, input7, input8, input9, input10]
    
    # Sidebar
    
    tk.Button(root, text='Exit', width=20, height=2, font=('arial', 12, 'bold'), bg='lightpink', command=destroy).place(x=1022, y=450)  
    tk.Button(root, text='Reset', width=20, height=2, font=('arial', 12, 'bold'), bg='lightblue', command=clear).place(x=1022, y=530)
    tk.Button(root, text='Submit', width=20, height=2, font=('arial', 12, 'bold'), bg='lightgreen', command=submit).place(x=1022, y=610)
    
    root.mainloop()