import pickle
from tkinter import messagebox


class DataManager:
    def __init__(self, filepath):
        """
        Initialize the DataManager with the filepath of the data file.

        Args:
            filepath (str): The path to the file where records are stored.
        """
        self.filepath = filepath

    def add_record(self, record):
        """
        Add a record to the data file.

        Args:
            record: The record to be added.
        """
        try:
            with open(self.filepath, "ab") as file:  # Open the file in binary append mode
                pickle.dump(record, file)  # Serialize the record and write it to the file
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add record: {e}")  # Display error message if adding fails

    def get_all_records(self):
        """
        Retrieve all records from the data file.

        Returns:
            list: A list containing all records found in the data file.
        """
        records = []
        try:
            with open(self.filepath, "rb") as file:  # Open the file in binary read mode
                while True:
                    try:
                        records.append(pickle.load(file))  # Deserialize records and append them to the list
                    except EOFError:
                        break  # Break the loop when end of file is reached
        except FileNotFoundError:
            pass  # If file is not found, return empty list
        return records

    def delete_record(self, match_function):
        """
        Delete records from the data file based on a matching function.

        Args:
            match_function (function): A function that takes a record as input and returns True if the record should be deleted, False otherwise.
        """
        records = self.get_all_records()  # Get all records from the file
        updated_records = [record for record in records if
                           not match_function(record)]  # Filter records based on match function
        with open(self.filepath, 'wb') as file:  # Open the file in binary write mode
            for record in updated_records:
                pickle.dump(record, file)  # Serialize and write the updated records back to the file

    def modify_record(self, match_function, update_function):
        """
        Modify records in the data file based on a matching function and an update function.

        Args:
            match_function (function): A function that takes a record as input and returns True if the record should be modified, False otherwise.
            update_function (function): A function that takes a record as input and returns the updated record.
        """
        records = self.get_all_records()  # Get all records from the file
        updated_records = []  # Initialize list to store updated records
        for record in records:
            if match_function(record):  # Check if record matches the criteria for modification
                record = update_function(record)  # Apply update function to the record
            updated_records.append(record)  # Append updated record to the list
        with open(self.filepath, 'wb') as file:  # Open the file in binary write mode
            for record in updated_records:
                pickle.dump(record, file)  # Serialize and write the updated records back to the file

    def find_record(self, match_function):
        """
        Find a record in the data file based on a matching function.

        Args:
            match_function (function): A function that takes a record as input and returns True if the record matches the criteria, False otherwise.

        Returns:
            object: The first record that matches the criteria, or None if no matching record is found.
        """
        records = self.get_all_records()  # Get all records from the file
        for record in records:
            if match_function(record):  # Check if record matches the criteria
                return record  # Return the first matching record
        return None  # Return None if no matching record is found
