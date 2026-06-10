import os
import shutil
import sys
import zipfile
import time
from pathlib import Path

path_to_folder = Path(sys.argv[1])
folder = path_to_folder.name
timestr = time.strftime("%Y%m%d")
zip_filename = f"{path_to_folder.name}_{timestr}.zip"


# Check if the path actually exists

if path_to_folder.is_dir():
	backup_zip = zipfile.ZipFile(zip_filename, 'w')
	for root, dirs, files in os.walk(path_to_folder):
		print(f"Adding files in folder {root}")
		
		for file in files:
			print(f"Adding file {files}")
			file_path = os.path.join(root, file)
			backup_zip.write(file_path)
	
	backup_zip.close()
	print("Done")

else: 
	print("Usage : ./zip_script.py <dir> <name>")
