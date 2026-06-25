import sqlite3

# Connects to db and create tables if they don't exist.

conn = sqlite3.connect('food_db.db', isolation_level=None)
print('Creating the tables...')
conn.execute('CREATE TABLE IF NOT EXISTS meals (name TEXT) STRICT')
conn.execute('CREATE TABLE IF NOT EXISTS ingredients (name TEXT, meal_id INTEGER, FOREIGN KEY(meal_id) REFERENCES meals (rowid)) STRICT')

# Prompting for input 

while True:
	user_input = input('')
	
	if user_input.lower() == 'quit':
		break

	if ":" in user_input:
		meal_ingred = user_input.split(":")
		ingredients = meal_ingred[1].split(",")
		meal = meal_ingred[0]

		try:
			data_meal = [f"{meal}"]
			data_ingred = ingredients
			cursor = conn.cursor()
			cursor.execute('INSERT INTO meals VALUES (?)', data_meal)
			meal_id = cursor.lastrowid

			for ingredient in ingredients:
				ingredient = ingredient.strip()
				cursor.execute('INSERT INTO ingredients VALUES (?, ?)', [ingredient, meal_id])
			
			print(f"Meal added : {meal}")
		except sqlite3.IntegrityError as e:
			print(f"Integrity error : {e}")
		except sqlite3.Error as e:
			print(f"Erreur: {e}")

	# Input is either Ingredient / Meal or Nonsense 
	if ":" not in user_input:
		cursor = conn.cursor()

		# Retreives row_id (=meal_id in ingredients) passes it to query ingredients
		cursor.execute('SELECT rowid FROM meals WHERE name = ?', [user_input])
		row_id_raw = cursor.fetchone()

		if row_id_raw:
			row_id = row_id_raw[0]
			query = cursor.execute('SELECT ingredients.name FROM ingredients WHERE meal_id = ?', [row_id])
			ingredients = []
			for row in query.fetchall():    
				ingredients.append(row[0])
			print(f"Ingredients of {user_input} :")
			for ingredient in ingredients:
				print(f"{ingredient}")

		# Is it an ingredient ? If yes, retreives ingredients from meals
		cursor.execute('SELECT meal_id FROM ingredients WHERE name = ?', [user_input])
		ingredient_meals = cursor.fetchall()
		#print(ingredient_meals)
		
		if ingredient_meals:
			print(f"Meals that uses {user_input} :")
			for row_id_tuple in ingredient_meals:
				meals = []
				row_id = row_id_tuple[0]
				#print(row_id)
				query = cursor.execute('SELECT meals.name FROM meals WHERE rowid = ?', [row_id])
				for row in query.fetchall():
					meals.append(row[0])
					#print(row)
				for meal in meals:
					print(meal)
