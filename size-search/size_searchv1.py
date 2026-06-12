import os
import shutil
import sys
import fnmatch
from pathlib import Path

# Validate the arguments

if len(sys.argv) < 2:    
	print("Usage: python3 size.py <directory> <size_in_mb>")    
	sys.exit(1)

path = Path(sys.argv[1])
size_search = sys.argv[2]

# Check if 1st arg is directory

if not path.is_dir():
	print(f"Error: Source '{path}' is not a directory")    
	sys.exit(1)

# Check if 2ns argument is digit

if not size_search.isdigit():
	print("You must enter a digit")    
	sys.exit(1)

# Walks the directory to find files > size_search

for root, dirs, files in os.walk(path):
    for item in files + dirs:
        item_path = os.path.join(root, item)
        try:
            size_mb = os.path.getsize(item_path) / (1024 * 1024)
            size_search= int(size_search)
            if size_mb > size_search:
                print(f"Item larger than {size_search}Mb found: {item_path}")
                print(f"Size: {size_mb:.2f}MB\n")
        except OSError as e:
            print(f"Error: {e}")
