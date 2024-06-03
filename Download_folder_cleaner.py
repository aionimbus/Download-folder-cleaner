import os
import shutil
from pathlib import Path

# Define the base path to the Downloads folder
BASE_PATH = os.path.expanduser('~/Downloads')

# Define the target directories
directories = ['Audio', 'Compressed', 'Code', 'Documents', 'Images', 'Softwares', 'Videos','Fonts', 'Other']

# Create directories if they don't exist
for directory in directories:
    os.makedirs(os.path.join(BASE_PATH, directory), exist_ok=True)

# Define file types for each category
file_types = {
    'Audio': ['.aif', '.cda', '.mid', '.midi', '.mp3', '.mpa', '.ogg', '.wav', '.wma', '.m4a'],
    'Compressed': ['.7z', '.deb', '.pkg', '.rar', '.rpm', '.tar.gz', '.z', '.zip', '.dmg'],
    'Code': ['.js', '.jsp', '.html', '.ipynb', '.py', '.java', '.css', '.py', '.c', '.cpp'],
    'Documents': ['.ppt', '.pptx', '.pdf', '.xls', '.xlsx', '.doc', '.docx', '.txt', '.tex', '.epub'],
    'Images': ['.bmp', '.gif', '.ico', '.jpeg', '.jpg', '.png', '.jfif', '.svg', '.tif', '.tiff', '.arw', '.cr2', '.nef', '.raf', '.psd', '.webp', '.heic'],
    'Softwares': ['.apk', '.bat', '.bin', '.exe', '.jar', '.msi'],
    'Videos': ['.3gp', '.avi', '.flv', '.h264', '.mkv', '.mov', '.mp4', '.mpg', '.mpeg', '.wmv', '.mmv', '.m2t', '.m2ts', '.wmv'],
    'Fonts': ['.ttf', '.otf'],
}

# Function to get the category for a file
def get_category(file_name):
    for category, extensions in file_types.items():
        if file_name.lower().endswith(tuple(extensions)):
            return category
    return 'Other'

# Move files to their respective directories
for item in os.listdir(BASE_PATH):
    item_path = os.path.join(BASE_PATH, item)
    if os.path.isfile(item_path):
        category = get_category(item)
        destination_dir = os.path.join(BASE_PATH, category)
        dest_path = os.path.join(destination_dir, item)

        # Check if the destination file already exists
        if os.path.exists(dest_path):
            print(f"Skipping {item}, it already exists in the destination.")
        else:
            # Move the file
            shutil.move(item_path, destination_dir)
            print(f"Moved {item} to {destination_dir}")

print("Files have been organized successfully.")