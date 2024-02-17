import mysql.connector

class DatabaseHelpers:

    def __init__(self):

        # Initialize and Connect with the mySQL Database
        self.databaseIdentifier = mysql.connector.connect(user='root', 
                                                          password='L)j2cK2to4q+^8NG.L*J',
                                                          host='localhost',
                                                          port='3306',
                                                          database='sms_database')
        
        if self.databaseIdentifier.is_connected():
            print("Connection to database successful!")
    
    def studentTable(self):
        """ Creates a query and table towards the database to get the dataset for the student """

        # We should connect to the database if we haven't already, in order to account for any premature calls of this function
        if not self.databaseIdentifier.is_connected():
            self.__init__()
        
        # Allow for the execution of SQL statements
        cursor = self.databaseIdentifier.cursor()

        # Create a 'student' table if it doesn't exist for one already
        self.studentData = """CREATE TABLE IF NOT EXISTS student(
                            FIRST_NAME VARCHAR(100) NOT NULL,
                            LAST_NAME VARCHAR(100),
                            GRADE VARCHAR(15),
                            COURSE VARCHAR(100),
                            SECTION VARCHAR(100)
                            )"""
         
        try:

            # Execute the creation of the table then close the cursor when we finish
            cursor.execute(self.studentData)
            cursor.close()

            print("Query Succesful!")
            return True

        except Exception as err:
            print(f"An error occured with your request! [{err}]")
            cursor.close()
            return False
    
    def fetchStudentData(self):
        """ Creates a query to to the database to get the data sent from the GUI."""

        try:
            cursor = self.databaseIdentifier.cursor()

            # Inset the values from 'studentData' and then place it into the database
            cursor.execute("INSERT INTO studentData (%s, %s, %s, %s %s) \
                            VALUES (FIRST_NAME, LAST_NAME, GRADE, COURSE, SECTION)") 

            # From the database, create a snapshot of this data that was inserted to save the changes
            self.databaseIdentifier.commit()
            cursor.close()

        except Exception as err:
            print(f"An error occured with your query! [{err}]") 

    def allStudentData(self):
        """ Allows for the ability to view all of the students in the database."""
        
        # Select all the entries in the student database and then order them by first name
        getAll = "SELECT * FROM studentData ORDER BY FIRST_NAME"
        cursor = self.databaseIdentifier.cursor()

        try:

            cursor.execute(getAll)
            data = cursor.fetchall()

            for all in data:
                data.insert("", all)

            self.databaseIdentifier.commit()
            cursor.close()

        except Exception as err:
            print(f"An error occured fetching all of the data! [{err}]")

        self.dbConnect.commit()
        cursor.close()

    def deleteStudentData(self):
        cursor = self.databaseIdentifier.cursor()

        self.databaseIdentifier.commit()
        cursor.close()
        pass

    def updateStudentData(self):
        cursor = self.databaseIdentifier.cursor()

        cursor.commit()
        cursor.close()
        pass
    
    def closeConnection(self):

        if self.studentDatabase.isconnected():
            self.studentDatabase.close()
            print("Closing Connection...")

sql = DatabaseHelpers()