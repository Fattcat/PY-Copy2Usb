import os
import shutil

def copy_files(source_folder, target_folder, extensions):
    for foldername, subfolders, filenames in os.walk(source_folder):
        for filename in filenames:
            if filename.endswith(tuple(extensions)):
                source_path = os.path.join(foldername, filename)
                target_path = os.path.join(target_folder, filename)
                shutil.copy2(source_path, target_path)
                print(f"Copied: {filename} from {source_path} to {target_folder}")

# Get the current user's home directory
user_home = os.path.expanduser('~')

# Specify the source directories including the desktop and Downloads folder
source_directories = [os.path.join(user_home, 'Desktop'), os.path.join(user_home, 'Downloads')]
# Specify the destination folder on your USB drive
target_directory = 'E:/CopyedFromPC'
os.makedirs(target_directory, exist_ok=True)
# List of file extensions to search for
file_extensions = [".txt", ".pdf", ".gif", ".jpg", ".png", ".jpeg", ".docs", ".dox", ".mp3", ".mp4", ".wav"]

# Iterate over each source directory
for source_directory in source_directories:
    copy_files(source_directory, target_directory, file_extensions)
