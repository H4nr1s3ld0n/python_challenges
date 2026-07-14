import pypdf, os
from pathlib import Path

pdf_filenames = []
pdf_encrypted = []
password = input("Enter your password here : ")
is_decrypted = False

# Walks the directory and create a list of pdf filenames

for filename in os.listdir('.'):
	if filename.endswith('.pdf'):
		pdf_filenames.append(filename)

for filename in pdf_filenames:
		writer = pypdf.PdfWriter()
		reader = pypdf.PdfReader(filename)

		# Adds the pages to the writer for encryption

		for page in reader.pages:
			writer.add_page(page)

		# Performs encryption with the password provided and sets the output name

		writer.encrypt(f'{password}', algorithm='AES-256')
		
		output_filename = f'{filename.replace(".pdf", "")}_encrypted.pdf'

		# Write the encrypted file

		with open(output_filename, 'wb') as file:
			writer.write(file)
		
		print(f"Encrypted {filename} to {output_filename}")


# Checking that we can actually perform decryption.

for filename in os.listdir('.'):
	if filename.endswith('_encrypted.pdf'):
		pdf_encrypted.append(filename)

for filename in pdf_encrypted:
	reader = pypdf.PdfReader(filename)
	output = reader.decrypt(password).name
	
# Checks that the password is valid and performs decryption, sets the is_decrypted flag to true

if output in ('OWNER_PASSWORD' or 'USER_PASSWORD'):
	is_decrypted = True
	print(f"{filename} => Decryption completed.")
else:
	print(f"{filename} => Incorrect password.")
	
# If the program could decrypt the pdf performs deletion of the standard files

if is_decrypted:
	print("Files were successfully encrypted and decrypted.")
	
	for filename in pdf_filenames:
		try:
			os.remove(filename)
			print(f"Deleted {filename}")
		except Exception as e:
			print(f"Could not delete {filename}: {e}")

else:
	print("Decryption failed, original files not deleted !")
