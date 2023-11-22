Setup instructions for the database.
    1. go onto PgAdmin and create a newdatabase (you can also use the sql Terminal)
    2. open up SQL tool for that database
    3. run DDL.sql to create the schema then DML.sql to fill the database

Steps to compile and run your application.
    1. install library using "pip install psycopg[binary]"
    2. run the app using "python ./app.py" inside of the directory
    3. make sure the db_config.json has the correct values based on you're database, user account, and port


A brief explanation of each function in the application.
    - grabs databse connect info from json file 
    - getAllStudents(): Retrieves and displays all records from the students table.
    - addStudent(first_name, last_name, email, enrollment_date): Inserts a new student record into the students table.
    - updateStudentEmail(student_id, new_email): Updates the email address for a student with the specified student_id.
    - deleteStudent(student_id): Deletes the record of the student with the specified student_id.

Video Demo:
    https://youtu.be/5GiMNTMr9xQ
