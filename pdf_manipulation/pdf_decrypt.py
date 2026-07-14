import pypdf, os

password = input("Enter your password to decrypt :")

for filename in os.listdir('.'):
	if filename.endswith('_encrypted.pdf'):
		reader = pypdf.PdfReader(filename)
		writer = pypdf.PdfWriter()
		output_filename = f'{filename.replace("encrypted.pdf", "")}decrypted.pdf'
		try: 
			reader.decrypt(password).name
			writer.append(reader)
			with open(output_filename, 'wb') as file:
				writer.write(file)
			print(f"{filename} decrypted and saved as {output_filename}")
		except Exception as e:
			print(f"Could not perform decryption on {filename}: {e}")
