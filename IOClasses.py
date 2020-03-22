# ---------------------------------------------------------- #
# Title: IOClasses.py - Assignment09
# Description: A module of IO classes
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# ASimpson, 03/21/2020, Modified this script for Assignment09
# ---------------------------------------------------------- #
if __name__ == "__main__":
    raise Exception("This file is not meant to ran by itself")
else: 
    import DataClasses as DC


class EmployeeIO:
    """  A class for performing Employee Input and Output

    methods:
        print_menu_items():

        print_current_list_items(list_of_rows):

        input_employee_data():

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class:
        ASimpson, 03/21/2020, Modified this script for Assignment09
    """

    @staticmethod
    def print_intro():
        """  Display a menu of choices to the user

        :return: nothing
        """
        # Introduction, print script name, demonstrate print() statement formatting here
        print("""\t\t\t <<<<<<  Employee Information Application  >>>>>>
        Hello, this is a simple Employee Information Tracker Script that uses the python
        object data to test and set values.  Please enter a menu option below.  
        """)

    @staticmethod
    def print_menu_items():
        """ Print a menu of choices to the user  """
        print('''
        Menu of Options
        1) Show current employee data
        2) Add new employee data.
        3) Save employee data to File
        4) Exit program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_options():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_list_items(list_of_rows: list):
        """ Print the current items in the list of Employee rows

        :param list_of_rows: (list) of rows you want to display
        """
        print("******* The Current Employee Database Information is: *******")
        for row in list_of_rows:
            print(str("ID: " + row[0] + " - " + row[1] + " " + row[2]))
        print("*******************************************")

    @staticmethod
    def input_employee_data(list_of_rows):
        """ Gets data for an employee object

        :param: list_of_rows: (list) List of Employee Information
        :return: (employee) object with input data
        """
        try:
            employee_id = (input("What is the employee Id? - ").strip())
            first_name = str(input("What is the employee First Name? - ").strip())
            last_name = str(input("What is the employee Last Name? - ").strip())
            print()  # Add an extra line for looks
            emp = DC.Employee(employee_id, first_name, last_name)
            strEmpInfo = str(emp)
            empID, empFirstName, empLastName = strEmpInfo.split(",")
            row = [empID, empFirstName, empLastName.strip()]
            list_of_rows.append(row)
        except Exception as e:
            print(e)
        return emp

    @staticmethod
    def input_yes_no_choice(optional_message="Add another Employee?(Y/N): "):
        """ Gets a yes or no choice from the user, pass in an optional message
        :param optional_message: Pass in a Yes/No Question message
        :return: string
        """
        # Use the Default Message or pass in an optional message, strip white spaces, and make lower case
        return str(input(optional_message)).strip().lower()

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)  # Print optional messages here otherwise print ''
        input('Press the [Enter] key to continue.')
