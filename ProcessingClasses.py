# ---------------------------------------------------------- #
# Title: ProcessingClasses.py - Assignment09
# Description: A module of multiple processing classes
# ChangeLog (Who,When,What):
# RRoot,1.1.2020,Created started script
# ASimpson, 03/21/2020, Modified for Assignment09
# ---------------------------------------------------------- #
if __name__ == "__main__":
    raise Exception("This file is not meant to ran by itself")


class FileProcessor:
    """Processes data to and from a file and a list of objects:

    methods:
        save_data_to_file(file_name,list_of_objects):

        read_data_from_file(file_name): -> (a list of objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        ASimpson, 03/21/2020, Modified for Assignment09
    """

    @staticmethod
    def save_data_to_file(file_name: str, list_of_objects: list):
        """ Write data to a file from a list of object rows

        :param file_name: (string) with name of file
        :param list_of_objects: (list) of objects data saved to file
        :return: (bool) with status of success status
        """
        success_status = False
        try:
            file = open(file_name, "w")
            for row in list_of_objects:
                file.write(row[0] + "," + row[1] + "," + row[2] + "\n")
            file.close()
            success_status = True
        except Exception as e:
            print("There was a general error!")
            print(e, e.__doc__, type(e), sep='\n')
        return success_status

    @staticmethod
    def read_data_from_file(file_name: str):
        """ Reads data from a file into a list of object rows

        :param file_name: (string) with name of file
        :return: (list) of object rows
        """
        list_of_rows = []
        try:
            file = open(file_name, "r")
            for line in file:
                empID, empFirstName, empLastName = line.split(",")
                row = [empID, empFirstName, empLastName.strip()]
                # Build Row here
                list_of_rows.append(row)
            file.close()
        except Exception as e:
            print("There was a general error!")
            print(e, e.__doc__, type(e), sep='\n')
        return list_of_rows


class DatabaseProcessor:

    # TODO: Add code to process to and from a database
    pass

