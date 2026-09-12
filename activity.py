import os
import shutil

user_input = input("Enter the name of folder: ")

if not os.path.exists(user_input):
    print("Folder does not exist.")

