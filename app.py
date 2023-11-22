from dataBaseFunctions import *


def main():

    print("Welcome to StudentDataBase")


    while(True):
        while(True):
            print("|--------Options--------|")
            print("|getAllStudents:     (1)|")
            print("|addStudent:         (2)|")
            print("|updateStudentEmail: (3)|")
            print("|DeleteStudent:      (4)|")
            print("|Quit:               (0)|")
            print("|-----------------------|")
            user_input = input("Enter a number: ")
            print()

            if(user_input.isnumeric()): 
                user_input = int(user_input)
                break
            else:
                print("Not a valid input")




        match user_input:
            case 1:
                print("Retrieving All Students")
                print()
                getAllStudents()

            case 2:
                print("Selection: Add Student")
                print()
                first_name = input("Enter first name of student: ") 
                last_name = input("Enter last name of student: ")
                email = input("Enter email name of student: ")
                enrollment_date = input("Enter enroll date of student: ") #needs to be a date????
                addStudent(first_name, last_name, email, enrollment_date)


            case 3:
                print("Updating email of student")
                print()
                while(True):
                    student_id = input("Enter id of student: ")
                    if(student_id.isnumeric()): 
                        student_id = int(student_id)
                        break
                    else:
                        print("Not a valid input")
                
                new_email = input("Enter new email of student: ")
                
                updateStudentEmail(student_id, new_email)


            case 4:
                print("Selection: Delete Student")
                print()
                while(True):
                    student_id = input("Enter id of student: ")
                    if(student_id.isnumeric()): 
                        student_id = int(student_id)
                        break
                    else:
                        print("Not a valid input")
                
                deleteStudent(student_id)

            case 0:
                print("Exiting StudentDataBase") 
                exit(1)
            
            case _:
                print("Not a valid input")




main()