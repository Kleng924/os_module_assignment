# Exploring Python's OS Module
# Objective: The goal of this assignment is to deepen your understanding of the OS module in Python.

# Task 1: Directory Inspector:

# Problem Statement: Create a Python script that lists all files and subdirectories in a given directory. 
# Your script should prompt the user for the directory path and then display the contents.


# List and print all files and subdirectories in the given path

import os

def list_directory_contents(path):
    try:
        if not os.path.isdir(path):
            print(f"The path {path} is not a valid directory.")
            return
        
        with os.scandir(path) as entries:
            for entry in entries:
                if entry.is_file():
                    print(f"File: {entry.name}")
                elif entry.is_dir():
                    print(f"Directory: {entry.name}")
    except PermissionError:
        print(f"Permission denied: {path}")
    except FileNotFoundError:
        print(f"File not found: {path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    directory_path = input("Enter the directory path: ")
    list_directory_contents(directory_path)

# Expected Outcome: The script should correctly list all files and subdirectories in the specified directory. 
# Handle exceptions for invalid paths or inaccessible directories.

