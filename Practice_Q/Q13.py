from tkinter import *

def submit_form():
    global entry_name, entry_email,entry_phone
    name=entry_name.get()
    email=entry_email.get()
    phone=entry_phone.get()
    print(f" Name - {name} \n Email - {email} \n Phone - {phone}")

def main():
    global entry_name, entry_email,entry_phone
    wind=Tk()
    wind.geometry("500x500")
    wind.title("Event Registration Form")

    # form inputs label
    name_label=Label(wind,text="Name :").grid(row=1,column=1)
    email_label=Label(wind,text="Email :").grid(row=2,column=1)
    phone_label=Label(wind,text="Phone No :").grid(row=3,column=1)

    # form inputs 
    entry_name=Entry(wind)
    entry_name.grid(row=1,column=2,padx=10,pady=5)
    entry_email=Entry(wind)
    entry_email.grid(row=2,column=2,padx=10,pady=5)
    entry_phone=Entry(wind)
    entry_phone.grid(row=3,column=2,padx=10,pady=5)
    
    # Submit form button  
    Button(wind,text="Register", command=submit_form).grid(row=4,column=1,padx=10,pady=5)
    wind.mainloop()


if __name__=="__main__":
    main()
