import os, pypdf
from pathlib import Path

wordlist = []


# We consider a wordlist that is located directly in the folder and we append the words to the list
with open(Path.cwd() / 'dictionary.txt', encoding='UTF-8') as f:
	for line in f:
		wordlist.append(line.strip())


# Finds the _encrypted.pdf, we could also use the is_encrypted function to autodetect
for filename in os.listdir('.'):
	if filename.endswith('_encrypted.pdf'):
		reader = pypdf.PdfReader(filename)
		output_filename = f'{filename.replace("encrypted.pdf", "")}bruteforced.pdf'
		
		found = False

		# Tries to bruteforce with the previous established wordlist
		for word in wordlist:
			try:
				result = reader.decrypt(word).name
				# print(f"Trying {word}")
				if result in ('OWNER_PASSWORD', 'USER_PASSWORD'):
					print(f"Match found : {word}")
					writer = pypdf.PdfWriter()
					writer.append(reader)

					with open(output_filename, 'wb') as file:
						writer.write(file)
					
					print(f"{filename}:{word} bruteforced and saved as {output_filename}")
					found = True
					break

			# Silently continue on failure 
			except Exception as e:
				continue

		if not found: 
			print("No match was found in the wordlist.")
