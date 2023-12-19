import customtkinter as ctk

root = ctk.CTk()
root.title('Hospital Management System - Patient Registration')
root.geometry('1000x600')
root.resizable(False, False)
root.config(bg='lightblue')


heading = ctk.CTkLabel(master=root, text='Patient Registration', font=('Poppins', 40, 'bold'), bg_color='lightblue', width=1000, height=80).place(x=0, y=0)

l1 = ctk.CTkLabel(master=root, text='Full Name', font=('helvetica', 20, 'bold'), bg_color='lightblue').place(x=30, y=100)
input1 = ctk.CTkEntry(master=root, width=300, height=40, font=('helvetica', 20), corner_radius=30, bg_color='lightblue').place(x=30, y=130)

l2 = ctk.CTkLabel(master=root, text='Age', font=('helvetica', 20, 'bold'), bg_color='lightblue').place(x=360, y=100)
input2 = ctk.CTkEntry(master=root, width=300, height=40, font=('helvetica', 20), corner_radius=30, bg_color='lightblue').place(x=360, y=130)

l3 = ctk.CTkLabel(master=root, text='Date of Birth', font=('helvetica', 20, 'bold'), bg_color='lightblue').place(x=690, y=100)
input3 = ctk.CTkEntry(master=root, width=300, height=40, font=('helvetica', 20), corner_radius=30, bg_color='lightblue').place(x=690, y=130)

l4 = ctk.CTkLabel(master=root, text='Gender', font=('helvetica', 20, 'bold'), bg_color='lightblue').place(x=30, y=200)
check_1 = ctk.CTkCheckBox(master=root, width=300, height=40, font=('helvetica', 20), corner_radius=30, bg_color='lightblue', text='Male').place(x=30, y=230)
check_2 = ctk.CTkCheckBox(master=root, width=300, height=40, font=('helvetica', 20), corner_radius=30, bg_color='lightblue', text='Female').place(x=150, y=230)

l5 = ctk.CTkLabel(master=root, text='Mobile No.', font=('helvetica', 20, 'bold'), bg_color='lightblue').place(x=360, y=200)
input5 = ctk.CTkEntry(master=root, width=300, height=40, font=('helvetica', 20), corner_radius=30, bg_color='lightblue').place(x=360, y=230)

l6 = ctk.CTkLabel(master=root, text='Email Addresss', font=('helvetica', 20, 'bold'), bg_color='lightblue').place(x=690, y=200)
input6 = ctk.CTkEntry(master=root, width=300, height=40, font=('helvetica', 20), corner_radius=30, bg_color='lightblue').place(x=690, y=230)

l7 = ctk.CTkLabel(master=root, text='Residential Address', font=('helvetica', 20, 'bold'), bg_color='lightblue').place(x=30, y=300)
input7 = ctk.CTkEntry(master=root, width=300, height=40, font=('helvetica', 20), corner_radius=30, bg_color='lightblue').place(x=30, y=330)

l8 = ctk.CTkLabel(master=root, text='Blood Group', font=('helvetica', 20, 'bold'), bg_color='lightblue').place(x=360, y=300)
input8 = ctk.CTkEntry(master=root, width=300, height=40, font=('helvetica', 20), corner_radius=30, bg_color='lightblue').place(x=360, y=330)

l9 = ctk.CTkLabel(master=root, text='NA', font=('helvetica', 20, 'bold'), bg_color='lightblue').place(x=690, y=300)
input9 = ctk.CTkEntry(master=root, width=300, height=40, font=('helvetica', 20), corner_radius=30, bg_color='lightblue').place(x=690, y=330)

l10 = ctk.CTkLabel(master=root, text='NA', font=('helvetica', 20, 'bold'), bg_color='lightblue').place(x=30, y=400)
input10 = ctk.CTkEntry(master=root, width=300, height=40, font=('helvetica', 20), corner_radius=30, bg_color='lightblue').place(x=30, y=430)

submit = ctk.CTkButton(master=root, text="Save", width=300, height=40, font=('helvetica', 20), corner_radius=30, bg_color='lightblue', fg_color='green').place(x=30, y=500)

reset = ctk.CTkButton(master=root, text="Reset", width=300, height=40, font=('helvetica', 20), corner_radius=30, bg_color='lightblue').place(x=360, y=500)

close = ctk.CTkButton(master=root, text="Exit", width=300, height=40, font=('helvetica', 20), corner_radius=30, bg_color='lightblue', fg_color='red').place(x=690, y=500)

root.mainloop()