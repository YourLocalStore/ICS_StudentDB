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
          print("\nConnection to database successful!")

    def studentTable(self):
      """ Creates a query and table towards the database to get the dataset for the student """

      # We should connect to the database if we haven't already, in order to account 
      # for any premature calls of this function
      if not self.databaseIdentifier.is_connected():
          self.__init__()

      # Allow for the execution of SQL statements
      cursor = self.databaseIdentifier.cursor()

      # Create a 'student' table if it doesn't exist for one already
      self.studentData = "CREATE TABLE IF NOT EXISTS student(\
                          FIRST_NAME VARCHAR(100) NOT NULL, \
                          LAST_NAME VARCHAR(100), \
                          GRADE VARCHAR(15), \
                          COURSE VARCHAR(100), \
                          SECTION VARCHAR(100) \
                          )"

      try:
        # Execute the creation of the table then close the cursor when we finish
        cursor.execute(self.studentData)
        print("Query Succesful!")

        # Quickly checking to see if the table actually exists
        cursor.execute("SHOW TABLES")
        for x in cursor:
            print(x)

        cursor.close()
        return True

      except Exception as err:
        print(f"An error occured with your request! [{err}]")
        cursor.close()
        return False

    def fetchStudentData(self):
        """ Creates a query to to the database to get the data sent."""

        try:
            cursor = self.databaseIdentifier.cursor()
            # Inset the values from 'studentData' and then place it into the database
            cursor.execute("INSERT INTO studentData (FIRST_NAME, LAST_NAME, GRADE, COURSE, SECTION) VALUES (%s, %s, %s, %s, %s)") 

            # From the database, create a snapshot of this data that was inserted to save the changes
            self.databaseIdentifier.commit()
            cursor.close()

        except Exception as err:
            print(f"An error occured with your query! [{err}]") 

    def deleteStudentData(self):
        cursor = self.databaseIdentifier.cursor()
        self.databaseIdentifier.commit()

        cursor.close()

    def updateStudentData(self):
        cursor = self.databaseIdentifier.cursor()
        self.databaseIdentifier.commit()
        
        cursor.close()

    def closeConnection(self):

        if self.databaseIdentifier.is_connected():
            self.databaseIdentifier.close()
            print("Closing Connection...")
