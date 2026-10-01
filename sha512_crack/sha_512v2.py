## Simple dictionary attack tool for SHA-512 hashes
## Input your /etc/shadow and check if it is dictionary safe
## Try with a list like rockyou.txt from SecLists 

from passlib.hash import sha512_crypt
import sys
import os
import re

# Regex check according the SHA-512 format $6 + $ 16 chars (salt) + $ hash
def is_sha512_crypt(hash_string):
	pattern = r'^\$6\$[./a-zA-Z0-9]{1,16}\$[./a-zA-Z0-9]{86}$'

	if re.match(pattern, hash_string):
		return True    
	return False

# Uses a dictionary and checks every word to crack 
def dictionary_attack(target_hash, wordlist):    
	for word in wordlist:
		word = word.strip()     
		if sha512_crypt.verify(word, target_hash):            
			print(f"Password found: {word}")            
			return word   
	
	print("Password not found in wordlist")    
	return None

def main():
	# If no argument provided, provides the usage
	if len(sys.argv) != 3:
		print("Usage: python script.py <hash> <wordlist_path> ")        
		sys.exit(1)

	input_hash = sys.argv[1]
	wordlist_path = sys.argv[2]
	
	# Checking the hash input
	if not is_sha512_crypt(input_hash):
		print("Invalid hash, enter a valid sha-512 hash")
		sys.exit(1)

	# Checking the filename input
	if not os.path.isfile(wordlist_path):
		print('[-]' + wordlist_path + 'does not exist')
		sys.exit(1)

	if not os.access(wordlist_path, os.R_OK):
		print('[-]' + wordlist_path + 'access denied.')
		sys.exit(1)

	print("[+] Using the following wordlist : " + wordlist_path)

	try:
		with open(wordlist_path, 'r') as passFile:
			result = dictionary_attack(input_hash, passFile)
		if result:
			print(f"Password cracked.")
			return result
		else: 
			print("[-] Password not found in the wordlist")
			return None

	except KeyboardInterrupt:
		print("Ctrl + C interrupting...")
		sys.exit()
	except Exception as e:
		print(f"Error : {e}")
		sys.exit(1)

	except FileNotFoundError:
		print("Password not found in wordlist")
	return None


if __name__ == '__main__':
	main()
