import os
import shutil
import sys
import fnmatch
from pathlib import Path

# Validate the arguments

if len(sys.argv) < 4:    
	print("Usage: python3 script.py <source_dir> <dest_dir> <extention> ")    
	sys.exit(1)

source_dir = Path(sys.argv[1])
dest_dir = Path(sys.argv[2])
extension = sys.argv[3]

# Just in case the users passes 'txt' instead of '.txt'

if not extension.startswith('.'):    
	extension = '.' + extension

# Validate source is directory

if not source_dir.is_dir():
	print(f"Error: Source '{source_dir}' is not a directory")    
	sys.exit(1)

if not dest_dir.is_dir(): 
	print(f"Error: Destination '{dest_dir}' is not a directory")    
	sys.exit(1)

# Copy the files

count = 0
for root, dirs, files in os.walk(source_dir):
	file_match = fnmatch.filter(files, f'*{extension}')
	for file in files:
		if file.endswith(extension):
			source_path = os.path.join(root, file)
			dest_path = os.path.join(dest_dir, file)
			try:
				shutil.copy2(source_path, dest_path)
				print(f"Copied {file}")
				count+=1
			except Exception as e:
				print(f"Error while copying {file}: {e}")
		
print("Done")
