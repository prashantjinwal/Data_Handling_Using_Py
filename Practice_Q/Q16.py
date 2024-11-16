import csv
from tkinter import *

def submit_details():
    # Get the entered details
    roll_no = roll_no_entry.get()
    enrollment_no = enrollment_no_entry.get()
    name = name_entry.get()
    course = course_entry.get()
    semester = semester_entry.get()

    # Write the details to a CSV file
    with open('student_details_16.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([roll_no, enrollment_no, name, course, semester])

    # Clear the entries after submission
    roll_no_entry.delete(0, END)
    enrollment_no_entry.delete(0, END)
    name_entry.delete(0, END)
    course_entry.delete(0, END)
    semester_entry.delete(0, END)

    confirmation_label.config(text="Details submitted successfully!")

def main():
    global roll_no_entry, enrollment_no_entry, name_entry, course_entry, semester_entry, confirmation_label

    wind = Tk()
    wind.title('Student Details')
    wind.geometry('500x400')

    Label(wind, text="Roll No:").grid(row=0, column=0, padx=10, pady=5)
    Label(wind, text="Enrollment No:").grid(row=1, column=0, padx=10, pady=5)
    Label(wind, text="Name:").grid(row=2, column=0, padx=10, pady=5)
    Label(wind, text="Course:").grid(row=3, column=0, padx=10, pady=5)
    Label(wind, text="Semester:").grid(row=4, column=0, padx=10, pady=5)

    roll_no_entry = Entry(wind)
    roll_no_entry.grid(row=0, column=1, padx=10, pady=5)

    enrollment_no_entry = Entry(wind)
    enrollment_no_entry.grid(row=1, column=1, padx=10, pady=5)

    name_entry = Entry(wind)
    name_entry.grid(row=2, column=1, padx=10, pady=5)

    course_entry = Entry(wind)
    course_entry.grid(row=3, column=1, padx=10, pady=5)

    semester_entry = Entry(wind)
    semester_entry.grid(row=4, column=1, padx=10, pady=5)

    Button(wind, text='Submit', command=submit_details).grid(row=5, columnspan=2, pady=10)

    confirmation_label = Label(wind, text="")
    confirmation_label.grid(row=6, columnspan=2, pady=10)

    wind.mainloop()

if __name__ == "__main__":
    main()
