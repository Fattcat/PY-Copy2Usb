import os
import shutil

# Specify the source directory on your PC
source_directory = "/path/to/source/directory"

# Specify the USB drive letter
usb_drive_letter = "D:"

# Specify the destination folder on the USB drive
destination_folder = "elezz"

# Create the destination folder on the USB drive if it doesn't exist
usb_destination_path = os.path.join(usb_drive_letter, destination_folder)
os.makedirs(usb_destination_path, exist_ok=True)

# Get a list of all .txt and .pdf files in the source directory
files_to_copy = [file for file in os.listdir(source_directory) if file.endswith(('.txt', '.pdf'))]

# Copy each file to the USB drive
for file_name in files_to_copy:
    source_path = os.path.join(source_directory, file_name)
    destination_path = os.path.join(usb_destination_path, file_name)
    shutil.copy2(source_path, destination_path)

print("Files copied successfully.")
