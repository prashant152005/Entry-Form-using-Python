import tkinter as tk
from tkinter import Label, PhotoImage, messagebox
import re
#    Database Connectivity
import pymysql
mydb = pymysql.connect(
  host="localhost",
  user="root",
  password="",
  database="student"
)

root = tk.Tk()

root.title("Examination Registration Form")
root.geometry("450x700")

bgImage=PhotoImage(file='bg1.png')
bgLabel=Label(root,image=bgImage,bd=5,width=1500, height= 400 )
bgLabel.place(x=0,y=0)


frame = tk.Frame(root)

fname_label = tk.Label(frame, text="First Name:" ,)
fname_entry = tk.Entry(frame,width = '30')

lname_label = tk.Label(frame, text="Last Name:")
lname_entry = tk.Entry(frame,width = '30')

email_label = tk.Label(frame, text="Email:")
email_entry = tk.Entry(frame,width = '30')

phone_label = tk.Label(frame, text="Phone No:")
phone_entry = tk.Entry(frame,width = '30')

city_label = tk.Label(frame, text="City:")
city_entry = tk.Entry(frame,width = '30')

state_label = tk.Label(frame, text="State:")
state_entry = tk.Entry(frame,width = '30')

country_label = tk.Label(frame, text="Country:")
country_entry = tk.Entry(frame,width = '30')

pincode_label = tk.Label(frame, text="Pin Code:")
pincode_entry = tk.Entry(frame,width = '30')

aadhar_label = tk.Label(frame, text="Aadhar No:")
aadhar_entry = tk.Entry(frame,width = '30')

gender_type_label = tk.Label(frame, text="Gender:")
gender_type_var = tk.StringVar(value="Male")
gender_type_male = tk.Radiobutton(frame, text="Male", variable=gender_type_var, value="Male")
gender_type_female = tk.Radiobutton(frame, text="Female", variable=gender_type_var, value="Female")
gender_type_others = tk.Radiobutton(frame, text="Others", variable=gender_type_var, value="Others")

course_label = tk.Label(frame, text="Highest Qualification:")
course_entry = tk.Entry(frame,width = '30')

date_label = tk.Label(frame, text="Exam Date and Time:")
date_options = ["April 10, 9:00 AM", "April 10, 2:00 PM", "April 11, 9:00 AM", "April 11, 2:00 PM"]
date_var = tk.StringVar(value=date_options[0])
date_menu = tk.OptionMenu(frame, date_var, *date_options)

exam_type_label = tk.Label(frame, text="Exam Type:")
exam_type_var = tk.StringVar(value="Online")
exam_type_online = tk.Radiobutton(frame, text="Online", variable=exam_type_var, value="Online")
exam_type_inperson = tk.Radiobutton(frame, text="Offline", variable=exam_type_var, value="Offline")

password_label = tk.Label(frame, text="Set Password:")
password_entry = tk.Entry(frame, show="*")

confirm_password_label = tk.Label(frame, text="Confirm Password:")
confirm_password_entry = tk.Entry(frame, show="*")


fname_label.grid(row=0, column=0, padx=5, pady=5)
fname_entry.grid(row=0, column=1, padx=5, pady=5)

lname_label.grid(row=1, column=0, padx=5, pady=5)
lname_entry.grid(row=1, column=1, padx=5, pady=5)

email_label.grid(row=2, column=0, padx=5, pady=5)
email_entry.grid(row=2, column=1, padx=5, pady=5)

phone_label.grid(row=3, column=0, padx=5, pady=5)
phone_entry.grid(row=3, column=1, padx=5, pady=5)

city_label.grid(row=4, column=0, padx=5, pady=5)
city_entry.grid(row=4, column=1, padx=5, pady=5)

state_label.grid(row=5, column=0, padx=5, pady=5)
state_entry.grid(row=5, column=1, padx=5, pady=5)

country_label.grid(row=6, column=0, padx=5, pady=5)
country_entry.grid(row=6, column=1, padx=5, pady=5)

pincode_label.grid(row=7, column=0, padx=5, pady=5)
pincode_entry.grid(row=7, column=1, padx=5, pady=5)

aadhar_label.grid(row=8, column=0, padx=5, pady=5)
aadhar_entry.grid(row=8, column=1, padx=5, pady=5)

gender_type_label.grid(row=9, column=0, padx=5, pady=5)
gender_type_male.grid(row=9, column=1, padx=5, pady=5)
gender_type_female.grid(row=10, column=1, padx=5, pady=5)
gender_type_others.grid(row=11, column=1, padx=5, pady=5)

course_label.grid(row=12, column=0, padx=5, pady=5)
course_entry.grid(row=12, column=1, padx=5, pady=5)

date_label.grid(row=13, column=0, padx=5, pady=5)
date_menu.grid(row=13, column=1, padx=5, pady=5)

exam_type_label.grid(row=14, column=0, padx=5, pady=5)
exam_type_online.grid(row=15, column=0, padx=5, pady=5)
exam_type_inperson.grid(row=15, column=1, padx=5, pady=5)

password_label.grid(row=16, column=0, padx=5, pady=5)
password_entry.grid(row=16, column=1, padx=5, pady=5)

confirm_password_label.grid(row=17, column=0, padx=5, pady=5)
confirm_password_entry.grid(row=17, column=1, padx=5, pady=5)

terms_var = tk.BooleanVar()
terms_checkbox = tk.Checkbutton(frame, text="I agree to the Terms and Conditions", variable=terms_var)
terms_checkbox.grid(row=18, column=0, columnspan=2, padx=5, pady=5)

def validate_form():
    if not fname_entry.get() or not lname_entry.get() or not email_entry.get() or not phone_entry.get() or not city_entry.get() or not state_entry.get() or not country_entry.get() or not pincode_entry.get() or not aadhar_entry.get()  or not gender_type_var.get()  or not course_entry.get() or not password_entry.get() or not confirm_password_entry.get():
        messagebox.showerror("Error", "Please fill all the fields.")

    elif not re.match(r"[^@]+@[^@]+.[^@]+", email_entry.get()):
        messagebox.showerror("Error", "Invalid email address.")

    elif not re.match(r"[0-9]{10}", phone_entry.get()):
        messagebox.showerror("Error", "Invalid phone number.")

    elif not re.match(r"[0-9]{12}", aadhar_entry.get()):
        messagebox.showerror("Error", "Invalid Aadhar number.")

    elif password_entry.get() != confirm_password_entry.get():
        messagebox.showerror("Error", "Passwords do not match.")

    elif not terms_var.get():
        messagebox.showerror("Error", "Please agree to the Terms and Conditions.")

    else:
        cursor = mydb.cursor()
        cursor.execute("INSERT INTO users values('"+fname_entry.get()+"', '"+lname_entry.get()+"','"+email_entry.get()+"','"+phone_entry.get()+"', '"+city_entry.get()+"', '"+state_entry.get()+"', '"+country_entry.get()+"','"+pincode_entry.get()+"','"+aadhar_entry.get()+"','"+gender_type_var.get()+"', '"+course_entry.get()+"', '"+date_var.get()+"','"+exam_type_var.get()+"','"+password_entry.get()+"')" )
        mydb.commit()
        messagebox.showinfo("Success", "Form submitted successfully.")

        print("Name:", fname_entry.get(), lname_entry.get())
        print("Email:", email_entry.get())
        print("Phone:", phone_entry.get())
        print("Address:", city_entry.get(),",", state_entry.get(),",", country_entry.get(),"-",pincode_entry.get())
        print("Aadhar No:", aadhar_entry.get())
        print("Gender:", gender_type_var.get())
        print("Course:", course_entry.get())
        print("Exam Date and Time:", date_var.get())
        print("Exam Type:", exam_type_var.get())
        print("Password:", password_entry.get())

        fname_entry.delete(0, tk.END)
        lname_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        city_entry.delete(0, tk.END)
        state_entry.delete(0, tk.END)
        country_entry.delete(0, tk.END)
        aadhar_entry.delete(0, tk.END)
        pincode_entry.delete(0, tk.END)
        course_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        confirm_password_entry.delete(0, tk.END)


submit_button = tk.Button(frame, text="Submit", command=validate_form)
submit_button.grid(row=19, column=0, columnspan=2, padx=5, pady=5)

frame.pack(padx=20, pady=20)

root.mainloop()
