import os

def list_files_larger_than_1gb(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_size_gb = os.path.getsize(file_path) / (1024 * 1024 * 1024) # Convert bytes to GB
            if file_size_gb > 1:
                print(f"File: {file_path} ({file_size_gb:.2f} GB)")

# Replace 'directory' with the path to your folder
directory = r"E:\vid\learn\path"
list_files_larger_than_1gb(directory)



