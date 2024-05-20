import os

def list_files_larger_than_min_size(directory, min_size_gb):
    count = 0
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_size_gb = os.path.getsize(file_path) / (1024 * 1024 * 1024) # Convert bytes to GB
            if file_size_gb > min_size_gb:
                count += 1
                print(f"{count}. File: {file_path} ({file_size_gb:.2f} GB)")

def main():
    directory = input("Enter the directory path: ")
    min_size_gb = float(input("Enter the minimum file size (in GB): "))
    print(f"Files larger than {min_size_gb} GB in directory '{directory}':")
    list_files_larger_than_min_size(directory, min_size_gb)

if __name__ == "__main__":
    main()

