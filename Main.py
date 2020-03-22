# ------------------------------------------------------------------------ #
# Title: Main.py - Assignment09
# Description: Working with Modules, this is where it all comes together
# ChangeLog (Who,When,What):
# RRoot,1.1.2030, Created started script
# RRoot,1.1.2030, Added pseudo-code to start assignment 9
# ASimpson, 03/21/2020, Modified code to complete assignment 9
# ------------------------------------------------------------------------ #
# TODO: Import Modules
if __name__ == "__main__":
    from DataClasses import Employee as Emp
    from ProcessingClasses import FileProcessor as Fp
    from ProcessingClasses import DatabaseProcessor as Dp  # <<setup for a future Database
    from IOClasses import EmployeeIO as Eio
    import sys
else:
    raise Exception("This file was not created to be imported")

# Global Variables -------------------------------------------------------------------- #
strFileName = "EmployeeData.txt"
lstTable = []  # A list that acts as a 'table' of rows
strChoice = ""  # Captures the user option selection

# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of employee objects when script starts
try:
    # Use this Processor function to read a text file and return a table of data
    lstTable = Fp.read_data_from_file(strFileName)  # read file data
    Eio.print_intro()  # print the script intro here
    while True:
        Eio.print_menu_items()  # print the menu here
        strChoice = Eio.input_menu_options()  # Get menu option
        # Process user's menu choice
        if strChoice.strip() == '1':  # Print the Employee Information
            Eio.print_current_list_items(lstTable)  # <<Print the list of employees here
            Eio.input_press_to_continue()  # send a message to the user
        elif strChoice == '2':  # Enter New Employee ID's and names
            while True:  # Use a While loop to allow for continued data entry
                # Use this Eio function to input a new Employee Id and Name Info
                strNewEmp = Eio.input_employee_data(lstTable)  # Input New Employee Info here
                strEmpInfo = str(strNewEmp)  # Took the returned Employee info and set to this string variable here
                empID, empFirstName, empLastName = strEmpInfo.split(",")  # Split out the various string pieces here
                # Print show the data for the new employee that was added
                print("New Employee Added: " + "ID: " + empID + " - " + empFirstName + " " + empLastName)
                # Evaluate the user choice and exit loop if "n" in response
                if "n" in Eio.input_yes_no_choice():
                    print()  # Add a line here for readability
                    # Exit the loop and go to the Main Menu
                    break
                else:
                    print()
        elif strChoice == '3':  # Save Data to File
            # Evaluate the user choice and exit loop if "y" in response
            if "y" in Eio.input_yes_no_choice("Save New Employee data to file? (y/n) - "):  # Use choice Eio function
                # If the user enters "y" get the filename and task list table and user the Processor function
                # to write to a text file
                Fp.save_data_to_file(strFileName, lstTable)
                strStatus = "Data Saved!!"  # Pass this message to the IO function below
                Eio.input_press_to_continue(strStatus)
            else:
                # In this step we're passing in a message instead of a variable for this function
                Eio.input_press_to_continue("Save Cancelled! Lo Siento!!  Data Lost...")
                break
            continue  # to show the menu
        elif strChoice == '4':  # Exit Program
            print("Goodbye!")
            break  # and Exit
        else:
            # Use a print statement to send a reminder to the user
            print('Please choose only 1, 2, 3, or 4!')
            print()
except Exception as e:
    # Print the following error handling statements
    print("There was a non-specific error!")
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')
    # Using the sys library here to get the line number of the line that failed
    exc_type, exc_obj, exc_tb = sys.exc_info()
    # print the line number here
    print("Line No: " + str(exc_tb.tb_lineno))


# Show user a menu of options
# Get user's menu option choice
    # Show user current data in the list of employee objects
    # Let user add data to the list of employee objects
    # let user save current data to file
    # Let user exit program

# Main Body of Script  ---------------------------------------------------- #
