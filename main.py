# from dbhelpers import DatabaseHelpers
from mysql import *
import mysql.connector

from dbhelpers import DatabaseHelpers

import pyfiglet
from pyfiglet import Figlet

import sys

running = True

# ----------------------------------- STUDENT FUNCTIONS ----------------------------------- #
# ----------------------------------------------------------------------------------------- #

class AddStudent:

    # Intialization 
    def __init__(self):
      try:

        # ----- General Credentials ----- #
        self.firstName = input("Enter the first name: ")
        self.lastName = input("Enter the last name: ")
        self.studentGrade = input("Enter the student's grade: ")

        # ----- Credentials About Courses ----- #
        self.studentCourse = int(input("What course are they in? (Enter the corresponding number): "))
        self.studentCourseSection = input("Enter the course section: ")

      except Exception as err:
        print(f"Something went wrong! {err}")

    def addStudentData(self):
      dbClass = DatabaseHelpers()

      # TODO: Pass the instantiated values into the instance methods of dbClass.
      
      try:
        getData = dbClass.studentTable()
        fetchData = dbClass.fetchStudentData()

      except Exception as err:
        print(f"Something went wrong with your request! {err}")

class RemoveStudent:

  def __init__(self):
    pass

  def removeStudentData(self):
    pass

class EditStudentInformation:

  def __init__(self):
    pass

  def editInfo(self):
    pass

class CheckClassList:

  def __init__(self):
    pass

  def checkAll(self):
    pass

# ----------------------------------- MENUS ----------------------------------- #
# ----------------------------------------------------------------------------- #
def userMenu():
  global running

  try:

    # First selection menu
    selections = {
      "1": ("Log-in", userLogin),
      "2": ("Exit Program", main)
    }

    # Get all key, value pairs and print them out
    for k, v in selections.items():
      options = (f"{str(k)} > {str(v[0])}")
      print(f"{options:^80}")

    # Ask the user which menu option they want to select
    userSelect = input("\nSelect an option from the menu above: ")
    print(f"[{selections[userSelect][0]}] Selected.")

    # Check if the input is in the menu
    if userSelect in selections:
      if userSelect == "2":
        print("\nThanks for using the Student Management System!")
        sys.exit()

      # According to the index of the dictionary, call its corresponding function
      selections[userSelect][1]()

  except Exception as err:
    print(f"An exception occurred! {err}")

def loggedMenu(username):
  while True:
    try:

      menu = (f"""

      ==============================================

                STUDENT MANAGEMENT MENU

                  Welcome, {username}!

      ==============================================
      """)

      print(f"{menu:^62}")

      selections = ({
        "1": ("Add a Student", AddStudent.addStudentData),
        "2": ("Remove a Student", RemoveStudent.removeStudentData),                  
        "3": ("Edit Student Information", EditStudentInformation.editInfo),
        "4": ("Check Class List", CheckClassList.checkAll),
        "5": ("Log-Out", main)
      })

      # Get all key, value pairs and print them out
      for k, v in selections.items():
        options = (f"{str(k)} > {str(v[0])}")
        print(f"{options:^56}")

      while (selections != "5"):
        testInput = input("\nSelect your Option: ")
        selections[testInput][1](AddStudent())

      else:
        main()
        return False


    except Exception as err:
      print(err)

# ----------------------------------- MENU FUNCTIONS ----------------------------------- #
# -------------------------------------------------------------------------------------- #
def userLogin():
  while True:
    try:

      usernameLog = input("\nEnter your Username: ").lower()
      passwordLog = input("Enter your Password: ").lower()

      with open("user_credentials.txt", "r") as loginCredentials:
        try:
          for data in loginCredentials.readlines():
            userdata = data.split()

            # Strip whitespace just to make sure that the strings will match
            username = userdata[0].strip("").lower()
            password = userdata[1].strip("").lower()

            if (username == usernameLog) and (password == passwordLog):
              print("Login Successful! \n")
              loginCredentials.close()

              loggedMenu(username)
              return True, username

            else:
              print("Login Unsuccessful! \n")
              return False

        except Exception as err:
          print(f"An exception occurred with the file! {err}")
          continue

    except Exception as err:
      print(f"An exception occured! {err}")

# Main loop
def main():

  while running:
    txt_banner = (pyfiglet.figlet_format("Student Management System", justify="center", font="small"))
    print(txt_banner)

    menu_select = userMenu()
    if (menu_select == "2"):
      return False

if __name__ == "__main__":
    # Main Method
    main()


