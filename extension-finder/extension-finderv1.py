import os
import shutil
import sys
import fnmatch
from pathlib import Path

# Validate the arguments

if len(sys.argv) < 3:    
	print("Usage: python3 script.py <source_dir> <dest_dir> <extention> ")    
	sys.exit(1)

path_to_folder = Path(sys.argv[1])
dest_folder = Path(sys.argv[2])
extention = Path(sys.argv[3])

# Just in case the users passes 'txt' instead of '.txt'

if not extention.startswith('.'):    
	extention = '.' + extention

# Validate source is directory

if not path_to_folder.is_dir():
	print(f"Error: Source '{path_to_folder}' is not a directory")    
	sys.exit(1)

if not dest_folder.is_dir(): 
	print(f"Error: Destination '{path_to_folder}' is not a directory")    
	sys.exit(1)

# Copy the files

for root, dirs, files in os.walk(path_to_folder):
	file_match = fnmatch.filter(files, f'*{extention}')
	for file in files:
		if file.endswith(extention):
			print(f"Found file {file} moving to {sys.argv[2]}")
			file_path = os.path.join(root, file)
			shutil.copy2(file_path, dest_folder)
		
print("Done")
