## Just a quick script to practice with passlib and crypto
## Takes a hash and performs a dictionary attack
## Change the dictionary.txt 

from passlib.hash import sha512_crypt
import os

# Hash for "SuperPass"
target_hash = "$6$L/d4Rgy5kVJyS6kb$mH.Rf7mJI3J3mhBFvv.FejkYlQI.4NAhGt9gpzNj3vgRoPJovl4WC/RFsN.sTD7aBhYfayAjxAbGhBut32J.b0"

# Uses the verify function (bool) 
def dictionary_attack(target_hash, wordlist):    
	for word in wordlist:
		word = word.strip()     
		if sha512_crypt.verify(word, target_hash):            
			print(f"Password found: {word}")            
			return word   
	
	print("Password not found in wordlist")    
	return None

def main():
	try:
    # The wordlist is in the same directory
		with open('dictionary.txt', 'r') as passFile:
			result = dictionary_attack(target_hash, passFile)
		if result:
			print(f"Password cracked : {result}")
			return result
		
	except FileNotFoundError:
		print("Password not found in wordlist")
	return None


if __name__ == '__main__':
	main()
