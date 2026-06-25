import sqlite3

# Creating the database

conn = sqlite3.connect('example.db', isolation_level=None)
print('Creating the tables...')
conn.execute('CREATE TABLE IF NOT EXISTS meals (name TEXT) STRICT')
conn.execute('CREATE TABLE IF NOT EXISTS ingredients (name TEXT, meal_id INTEGER, FOREIGN KEY(meal_id) REFERENCES meals (rowid)) STRICT')

# Prompts for the input, 

while True:
	user_input = input('')

  # Exits
	if user_input.lower() == 'quit':
		break

  # Case 1 : users enters Meal:Ingredient1,Ingredient2. 
	if ":" in user_input:
    # Parsing the input to get only Meal and Ingredients.
		meal_ingred = user_input.split(":")
		ingredients = meal_ingred[1].split(",")
		meal = meal_ingred[0]
		print(f"{ingredients}")

		try:
			data_meal = [f"{meal}"]
			data_ingred = ingredients
			cursor = conn.cursor()
			cursor.execute('INSERT INTO meals VALUES (?)', data_meal)
			meal_id = cursor.lastrowid

      # Adds the ingredients in the database 
			for ingredient in ingredients:
			  ingredient = ingredient.strip()
				cursor.execute('INSERT INTO ingredients VALUES (?, ?)', [ingredient, meal_id])
			
			print(f"Meal added : {meal}")
		except sqlite3.IntegrityError as e:
			print(f"Violation de contrainte: {e}")
		except sqlite3.Error as e:
			print(f"Erreur: {e}")
