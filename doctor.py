import tkinter as tk


def doctor():
    def destroy():
        root.destroy()

    def clear():
        for data in inputs:
            data.delete(0, tk.END)
        input9.delete("1.0", tk.END)

    WINDOW_HEIGHT = 700
    WINDOW_WIDTH = 1250
    X_COORDINATE = 100
    Y_COORDINATE = 70
    root = tk.Tk()
    root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{X_COORDINATE}+{Y_COORDINATE}")
    root.title("Hospital Mangement System")
    root.resizable(False, False)
    root.config(bg='#06283D')

    tk.Label(root, text="DOCTER REGISTRATION", width=50, height=2, bg='#c36464', fg='#fff', font=('algerian', 30)).place(x=0, y=0)

    # Frame 1
    frame1 = tk.LabelFrame(root, text='Doctor\'s Details', font=20, bd=2, width=970, height=250, relief='groove', bg='#ededed', fg='#06283d').place(x=30, y=150)

    tk.Label(root, text="First Name", font=('arial', 17), bg='#ededed', fg='#06283d').place(x=60, y=180)
    input1 = tk.Entry(root, width=25, font=('arial', 15)).place(x=180, y=182)

    tk.Label(root, text="Last Name", font=('arial', 17), bg='#ededed', fg='#06283d').place(x=480, y=180)
    input2 = tk.Entry(root, width=25, font=('arial', 15)).place(x=620, y=182)

    tk.Label(root, text="Gender", font=('arial', 17), bg='#ededed', fg='#06283d').place(x=60, y=260)
    input3 = tk.Entry(root, width=25, font=('arial', 15)).place(x=180, y=262)

    tk.Label(root, text="Age", font=('arial', 17), bg='#ededed', fg='#06283d').place(x=480, y=260)
    input4 = tk.Entry(root, width=25, font=('arial', 15)).place(x=620, y=262)

    tk.Label(root, text="Mobile No", font=('arial', 17), bg='#ededed', fg='#06283d').place(x=60, y=340)
    input5 = tk.Entry(root, width=25, font=('arial', 15)).place(x=180, y=342)

    tk.Label(root, text="Email", font=('arial', 17), bg='#ededed', fg='#06283d').place(x=480, y=340)
    input6 = tk.Entry(root, width=25, font=('arial', 15)).place(x=620, y=342)

    # Frame 2
    frame2 = tk.LabelFrame(root, text='Doctor\'s Data', font=20, bd=2, width=970, height=250, relief='groove', bg='#ededed', fg='#06283d').place(x=30, y=420)

    tk.Label(root, text="Experience", font=('arial', 17), bg='#ededed', fg='#06283d').place(x=60, y=460)
    input7 = tk.Entry(root, width=25, font=('arial', 15)).place(x=180, y=462)

    tk.Label(root, text="Education", font=('arial', 17), bg='#ededed', fg='#06283d').place(x=480, y=460)
    input8 = tk.Entry(root, width=25, font=('arial', 15)).place(x=620, y=462)

    tk.Label(root, text="Certification/Specialization", font=('arial', 17), bg='#ededed', fg='#06283d').place(x=60, y=520)
    input9 = tk.Text(root, width=76, height=3, font=('arial', 15)).place(x=60, y=552)

    inputs = [input6, input1, input2, input3, input4, input5, input7, input8]

    # Sidebar

    tk.Button(root, text='Exit', width=20, height=2, font=('arial', 12, 'bold'), bg='lightpink', command=destroy).place(x=1022, y=450)

    tk.Button(root, text='Reset', width=20, height=2, font=('arial', 12, 'bold'), bg='lightblue', command=clear).place(x=1022, y=530)

    tk.Button(root, text='Submit', width=20, height=2, font=('arial', 12, 'bold'), bg='lightgreen', ).place(x=1022, y=610)

    root.mainloop()