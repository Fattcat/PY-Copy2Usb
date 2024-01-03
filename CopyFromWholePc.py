import os
import shutil

def copy_files(source_folder, target_folder, extensions):
    for foldername, subfolders, filenames in os.walk(source_folder):
        for filename in filenames:
            if filename.endswith(tuple(extensions)):
                source_path = os.path.join(foldername, filename)
                target_path = os.path.join(target_folder, filename)
                shutil.copy2(source_path, target_path)
                print(f"Copied: {filename} to {target_folder}")

# Specify the source directory including the root
source_directory = 'C:/'
# Specify the destination folder on your USB drive
target_directory = 'E:/CopyedFromPC'
os.makedirs(target_directory, exist_ok=True)
# List of file extensions to search for
file_extensions = [".pdf", ".gif", ".jpg", ".png", ".jpeg", ".docs", ".dox", ".mp3", ".mp4", ".wav"]
