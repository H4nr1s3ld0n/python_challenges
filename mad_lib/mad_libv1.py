from pathlib import Path
import os
import re

## Read a text file and establish regex rules

p = Path('example.txt')
content = p.read_text()
print(f"{content}")

adj_p = re.compile(r'ADJECTIVE')
noun_p = re.compile(r'NOUN')
verb_p = re.compile(r'VERB{1}')
adverb_p = re.compile(r'ADVERB{1}')

# Search for string, take the user input by each apparition, susititute the string with input

while noun_p.search(f'{content}'):
	noun_s = input("Enter a noun:\n")
	content = noun_p.sub(f'{noun_s}', f'{content}', count=1)

while adj_p.search(f'{content}'):
	adj_s = input("Enter an adjective:\n")
	content = adj_p.sub(f'{adj_s}', f'{content}', count=1)

while verb_p.search(f'{content}'):
	verb_s = input("Enter a verb:\n")
	content = verb_p.sub(f'{verb_s}', f'{content}', count=1)

while adverb_p.search(f'{content}'):
	adverb_s = input("Enter an adverb:\n")
	content = adverb_p.sub(f'{verb_s}', f'{content}', count=1)

# Returns the substitution

print(f"{content}")

# Write it to a new file

with open('example_result.txt', 'w', encoding='UTF-8') as file_obj:
	file_obj.write(f'{content}')
