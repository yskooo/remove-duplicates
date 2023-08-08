from tkinter import Tk
from tkinter.filedialog import askdirectory
import os
import hashlib 
from pathlib import Path
import shutil

def remove_duplicates(path):
    unique = dict()

    for file in os.listdir(path):
        file_name = Path(os.path.join(path, file))
        if file_name.is_file():
            file_hash = hashlib.sha256(open(file_name, 'rb').read()).hexdigest()
            if file_hash not in unique:
                unique[file_hash] = file_name
            else:
                print(f"Duplicate found: {file_name}")
                user_input = input("Do you want to delete this file? (y/n): ")
                if user_input.lower() == 'y':
                    os.remove(file_name)
                    print(f"Deleted: {file_name}")
        else:
            print(f"Not a file: {file_name}")

if __name__ == "__main__":
    Tk().withdraw()
    selected_path = askdirectory(title='Select Folder')
    remove_duplicates(selected_path)