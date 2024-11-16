from tkinter import *
from datetime import datetime

def Age_Calculator():
    # Get the entered date, month, and year
    day = date_entry.get()
    month = month_entry.get()
    year = year_entry.get()

    try:
        # Convert the entered values to integers
        birth_date = datetime(int(year), int(month), int(day))
        today = datetime.now()
        
        # Calculate the age
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        
        # Display the age
        result_label.config(text=f"Your age is: {age} years")
    except ValueError:
        result_label.config(text="Invalid date entered. Please try again.")

def main():
    global date_entry, month_entry, year_entry, result_label
    wind = Tk()
    wind.title('Age Calculator')
    wind.geometry('500x400')

    Label(wind, text="Enter Date:").grid(row=0, column=0, padx=10, pady=5)
    Label(wind, text="Enter Month:").grid(row=1, column=0, padx=10, pady=5)
    Label(wind, text="Enter Year:").grid(row=2, column=0, padx=10, pady=5)

    date_entry = Entry(wind)
    date_entry.grid(row=0, column=1, padx=10, pady=5)

    month_entry = Entry(wind)
    month_entry.grid(row=1, column=1, padx=10, pady=5)

    year_entry = Entry(wind)
    year_entry.grid(row=2, column=1, padx=10, pady=5)

    Button(wind, text='Submit', command=Age_Calculator).grid(row=3, columnspan=2, pady=10)

    result_label = Label(wind, text="")
    result_label.grid(row=4, columnspan=2, pady=10)

    wind.mainloop()

if __name__ == "__main__":
    main()
