import re

score = 0

# Declaring regex expressions 
is_eight = re.compile(r'.{8,}')
is_low = re.compile(r'[a-z]')
is_up = re.compile(r'[A-Z]')
is_num = re.compile(r'\d')
is_special = re.compile(r'[!@#$%^&*()_+\-=\[\]{};:\'",.<>?/\\|`]')

password = input("Enter your password:")
suggestion = []

# Checking if each condition is met and adding one to the total score. Appending if not. 
if is_eight.search(password):
    score += 1
else:
    suggestion.append("Password must be 8 characters.\n")

if is_low.search(password):
    score += 1
else:
    suggestion.append("Password must include one lower character.\n")

if is_up.search(password):
    score += 1
else:
    suggestion.append("Password must include one upper character\n")

if is_num.search(password):
    score += 1
else:
    suggestion.append("Password must include one number\n")

if is_special.search(password):
    score += 1
else:
    suggestion.append("Password must include one special character\n")

# Prints the final score and each suggestion
print(f"\nYour password security score is : {score} /5")

if suggestion:
    print("\n Suggestions:")
    for s in suggestion:
        print(f"- {s}")
