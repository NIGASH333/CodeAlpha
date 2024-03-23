import os
import shutil

def organize_files(source_dir):
    
    extensions_mapping = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Documents': ['.doc', '.docx', '.pdf', '.txt', '.xls', '.xlsx', '.ppt', '.pptx'],
        'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.flv'],
        'Audios': ['.mp3', '.wav', '.ogg', '.flac'],
        'Archives': ['.zip', '.rar', '.tar', '.gz'],
        'Executables': ['.exe', '.msi'],
        'Scripts': ['.py', '.sh', '.bat'],
        'Others': []  # Default folder for files with unknown extensions
    }

    # Create directories if they don't exist
    for folder in extensions_mapping.keys():
        if not os.path.exists(os.path.join(source_dir, folder)):
            os.makedirs(os.path.join(source_dir, folder))

    # Iterate over files in source directory
    for filename in os.listdir(source_dir):
        if os.path.isfile(os.path.join(source_dir, filename)):
            # Get the file extension
            file_ext = os.path.splitext(filename)[1].lower()

            # Find the directory to move the file to
            destination_folder = 'Others'  # Default to 'Others' if extension not found
            for folder, extensions in extensions_mapping.items():
                if file_ext in extensions:
                    destination_folder = folder
                    break

            # Move the file to the corresponding directory
            source_file_path = os.path.join(source_dir, filename)
            destination_dir = os.path.join(source_dir, destination_folder)
            destination_file_path = os.path.join(destination_dir, filename)
            shutil.move(source_file_path, destination_file_path)
            print(f"Moved '{filename}' to '{destination_folder}' folder.")

if __name__ == "__main__":
    source_directory = input("Enter the directory path to organize files: ")
    organize_files(source_directory)
