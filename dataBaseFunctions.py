import json
import psycopg #library for PostgreSQL


"""
    Reads database configuration parameters (used in connect) from a JSON file. 
    
    Parameters:
    - filename (str): The name of the JSON file containing the database configuration.
                     Default value is 'db_config.json'.

    Returns:
    - dict: A dictionary containing the database configuration parameters.

    Raises:
    - FileNotFoundError: If the specified file is not found.
    - json.JSONDecodeError: If there is an error decoding the JSON content.
"""
def read_db_config(filename='db_config.json'):
    with open(filename, 'r') as file:
        config = json.load(file)
    return config


 
"""
    Retrieves and displays all records from the 'students' table in the database.

    Raises:
    - psycopg.Error: If there is an error while interacting with the PostgreSQL database.
"""
def getAllStudents():

    try:
        db_params = read_db_config()
        
        # using "with" will make sure to close them and free their resources at the end of the block 
        # conninfo – The connection string (a postgresql:// url or a list of key=value pairs) to specify where and how to connect.
        with psycopg.connect(**db_params) as conn: # Connect to an existing database

            # Open a cursor to perform database operations
            with conn.cursor() as cur:
                
                cur.execute( # with Cursor send commands to the database using methods such as execute() and executemany(),
                    "SELECT * FROM students"
                )
                query = cur.fetchall()  # retrieve data from the database, iterating on the cursor or using methods such as fetchone(), fetchmany(), fetchall().

                print("(student_ID, first_name, last_name, email, enrollment_date)")
                for item in query:
                    print(item)
                print()

    except psycopg.Error as e:
        print("Error:",e)



"""
    Inserts a new student record into the 'students' table in the database.

    Parameters:
    - first_name (str): The first name of the new student.
    - last_name (str): The last name of the new student.
    - email (str): The email address of the new student.
    - enrollment_date (str): The enrollment date of the new student (format: 'YYYY-MM-DD').

    Raises:
    - psycopg.Error: If there is an error while interacting with the PostgreSQL database.
"""
def addStudent(first_name, last_name, email, enrollment_date):
    try:
        db_params = read_db_config()
        with psycopg.connect(**db_params) as conn:
            with conn.cursor() as cur:
                
                cur.execute( 
                    "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)",
                    (first_name, last_name, email, enrollment_date,)
                )

            conn.commit()     # Make the changes to the database persistent
        print()

    except psycopg.Error as e:
        print("Error:",e)



"""
    Updates the email address for a student with the specified student_id in the database.

    Parameters:
    - student_id (int): The unique identifier of the student whose email is to be updated.
    - new_email (str): The new email address to be set for the student.

    Raises:
    - psycopg.Error: If there is an error while interacting with the PostgreSQL database.
"""
# Updates the email address for a student with the specified student_id.
def updateStudentEmail(student_id, new_email): 
    try:
        db_params = read_db_config()
        with psycopg.connect(**db_params) as conn:
            with conn.cursor() as cur:
                
                cur.execute( "SELECT * FROM students WHERE student_id=%s", (student_id,) )
                oldQuery = cur.fetchone()

                if(oldQuery != None):
                    oldQuery = oldQuery
                    
                    #update
                    cur.execute( "UPDATE students SET email=%s WHERE student_id=%s",(new_email, student_id,) )

                    cur.execute( "SELECT * FROM students WHERE student_id=%s", (student_id,) )
                    new_query = cur.fetchone()

                    print("Updated:", oldQuery, "->", new_query);
                else:
                    print("No student was found with that ID")

            conn.commit() 
        print()


    except psycopg.Error as e:
        print("Error:",e)



"""
    Deletes the record of the student with the specified student_id from the database.

    Parameters:
    - student_id (int): The unique identifier of the student to be deleted.

    Raises:
    - psycopg.Error: If there is an error while interacting with the PostgreSQL database.
"""
def deleteStudent(student_id):
    try:
        db_params = read_db_config()
        with psycopg.connect(**db_params) as conn:
            with conn.cursor() as cur:
                
                cur.execute("SELECT * FROM students WHERE student_id=%s", (student_id,) )
                student = cur.fetchall()

                if (student != []):
                    student = student[0]
                    print("Deleting:", student)

                    cur.execute( 
                        "DELETE FROM students WHERE student_id=%s",
                        (student_id,)
                    )
                else:
                    print("No student was found with that ID")
            

            conn.commit() 
        print()


    except psycopg.Error as e:
        print("Error:",e)
