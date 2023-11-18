import os
import json

# Define the path to the directory containing the folders
directory_path = '.'  # Change this to the path of your directory

# Function to remove the first element from the dialogue list in a file
def remove_first_element(file_path):
    # Open the file and load the data
    with open(file_path, 'r', encoding='utf-8') as file:
        dialogue_list = json.load(file)

    # Remove the first element
    if dialogue_list:  # Check if the list is not empty
        dialogue_list.pop(0)

    # Write the modified list back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(dialogue_list, file, ensure_ascii=False, indent=4)

# Loop through each folder in the directory
for folder_name in os.listdir(directory_path):
    folder_path = os.path.join(directory_path, folder_name)
    # Check if it's a folder
    if os.path.isdir(folder_path):
        # Define the path to the dialogue.txt file within the folder
        file_path = os.path.join(folder_path, 'dialogue.txt')
        # Check if the file exists
        if os.path.isfile(file_path):
            # Call the function to remove the first element
            remove_first_element(file_path)

# This script assumes that the provided directory path is correct and that each subfolder contains a dialogue.txt file.
# It removes the first element from the dialogue list in each dialogue.txt file.
