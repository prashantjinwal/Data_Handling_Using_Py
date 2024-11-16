import csv 

def main():
    with open('Question_11.csv','w') as fh:
        writer=csv.writer(fh)
        writer.writerow(['RollNo', 'Enrollment_No', 'Name','Course','Semester'])  # Writing header
        stu_no=int(input("Enter no. of student"))
        print(f"Enter student specific details for {stu_no} students \n ")
        for i in range(stu_no):
            print(f"{i+1} Student details : - ")
            name=input("Enter Student name : ")
            course=input("Enter Course : ")
            semester=int(input("Enter Semester: "))
            roll_no=int(input("Enter Roll number: "))
            enroll_no=int(input("Enter Enrollment number : "))
            writer.writerow([roll_no,enroll_no,name,course, semester])

if __name__=="__main__":
    main()
