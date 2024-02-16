import mysql.connector

class DatabaseHelpers:

    def __init__(self):

        # Initialize and Connect with the mySQL Database
        self.studentDatabase = mysql.connector.connect(user="management_admin", 
                                        password="L)j2cK2to4q+^8NG.L*J",
                                        host="localhost",
                                        port="3306",
                                        database="SMS_Database")
    
    def studentTable(self):
        """ 
        Creates a query and table towards the database to get the dataset for the student
        """

        cursor = self.studentDatabase.cursor()
        self.dataTable = """CREATE TABLE IF NOT EXISTS student(
                            FIRST_NAME VARCHAR(100) NOT NULL,
                            LAST_NAME VARCHAR(100),
                            GRADE VARCHAR(15),
                            COURSE VARCHAR(100),
                            SECTION VARCHAR(100)
                            )"""
        
        try:
            cursor.execute(self.dataTable)
            cursor.close()
            return True

        except Exception as err:
            print(f"An error occured with your request! [{err}]")
            cursor.close()
            return False

    def sendStudentData(self):
        dbConnect = self.studentDatabase.connect()
        cursor = dbConnect.cursor()

        dbConnect.close()
        pass

    def fetchStudentData(self):
        dbConnect = self.studentDatabase.connect()
        cursor = dbConnect.cursor()

        dbConnect.commit()
        dbConnect.close()
        pass

    def deleteStudentData(self):
        dbConnect = self.studentDatabase.connect()
        cursor = dbConnect.cursor()

        dbConnect.commit()
        dbConnect.close()
        pass

    def updateStudentData(self):
        dbConnect = self.studentDatabase.connect()
        cursor = dbConnect.cursor()

        dbConnect.commit()
        dbConnect.close()
        pass
    
    def closeConnection(self):

        if self.studentDatabase.isconnected():
            self.studentDatabase.close()
            print("Closing Connection...")
