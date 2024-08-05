import os, shutil

# Set the path to the folder you want to sort
path = r"C:/Users/"

# List all the files in the folder
file_name = os.listdir(path)
print(file_name)

# Create a folder for each file type
folder_names = []
for file in file_name:
    if os.path.isfile(path + file):
        file_type = file.split(".")[-1]
        if file_type not in folder_names:
            folder_names.append(file_type)
            os.mkdir(path + file_type)
            print(f"Folder for {file_type} created")

# Move the files to their respective folders
for file in file_name:
    if os.path.isfile(path + file):
        file_type = file.split(".")[-1]
        shutil.move(path + file, path + file_type + "/" + file)
        print(f"{file} moved to {file_type} folder")
        print("All files sorted!")
