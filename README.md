# Automatic_sorter
This Python script organizes files in a specified directory into subdirectories based on their file extensions. The script scans a target directory, identifies files (excluding directories), and groups them into subdirectories corresponding to their respective file extensions. 

Requirements:

Python 3.x
os module (standard library)
shutil module (standard library)

Usage:

Replace the file_path variable with the path to the directory containing the files you want to organize.
Run the script using Python.
Functionality:

The script uses the os and shutil modules to interact with the file system and move files between directories.
It retrieves a list of files in the specified directory using os.listdir() and filters out directories using os.path.isfile() and os.path.join().
For each file, it extracts the file extension using str.split('.')[-1].
It maintains a dictionary, filetype_dict, to keep track of the subdirectories and their respective file extensions.
If a subdirectory for a file extension doesn't exist, the script creates one using os.mkdir().
The script then moves each file to its corresponding subdirectory using shutil.move().
The process is logged with print statements, indicating which files are moved to which subdirectories.
Note:

The script uses negative indexing (e.g., str.split('.')[-1]) to access the last element of the split result. This assumes that the file names contain a single dot and have an extension. If some files don't have extensions or have multiple dots in their names, consider updating the script accordingly.
This Python script can be useful for organizing files in a directory and maintaining a clean file structure. It can be easily adapted or extended to handle different file organization needs based on specific criteria.
