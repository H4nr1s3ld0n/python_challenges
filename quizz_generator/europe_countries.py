import random

capitals = {
    'Albania': 'Tirana',
    'Andorra': 'Andorra la Vella',
    'Armenia': 'Yerevan',
    'Austria': 'Vienna',
    'Azerbaijan': 'Baku',
    'Belarus': 'Minsk',
    'Belgium': 'Brussels',
    'Bosnia and Herzegovina': 'Sarajevo',
    'Bulgaria': 'Sofia',
    'Croatia': 'Zagreb',
    'Cyprus': 'Nicosia',
    'Czechia': 'Prague',
    'Denmark': 'Copenhagen',
    'Estonia': 'Tallinn',
    'Finland': 'Helsinki',
    'France': 'Paris',
    'Georgia': 'Tbilisi',
    'Germany': 'Berlin',
    'Greece': 'Athens',
    'Hungary': 'Budapest',
    'Iceland': 'Reykjavik',
    'Ireland': 'Dublin',
    'Italy': 'Rome',
    'Kazakhstan': 'Astana',
    'Kosovo': 'Pristina',
    'Latvia': 'Riga',
    'Liechtenstein': 'Vaduz',
    'Lithuania': 'Vilnius',
    'Luxembourg': 'Luxembourg (city)',
    'Malta': 'Valletta',
    'Moldova': 'Chisinau',
    'Monaco': 'Monaco',
    'Montenegro': 'Podgorica',
    'Netherlands': 'Amsterdam',
    'North Macedonia': 'Skopje',
    'Norway': 'Oslo',
    'Poland': 'Warsaw',
    'Portugal': 'Lisbon',
    'Romania': 'Bucharest',
    'Russia': 'Moscow',
    'San Marino': 'San Marino',
    'Serbia': 'Belgrade',
    'Slovakia': 'Bratislava',
    'Slovenia': 'Ljubljana',
    'Spain': 'Madrid',
    'Sweden': 'Stockholm',
    'Switzerland': 'Bern',
    'Turkey': 'Ankara',
    'Ukraine': 'Kyiv (also known as Kiev)',
    'United Kingdom': 'London',
    'Vatican City': 'Vatican City'
}


# Generates 20 Quiz files
for quiz_num in range(20):
	quiz_file = open(f'capitalsquiz{quiz_num + 1}.txt', 'w', encoding ='UTF-8')
	answer_file = open(f'capitalquiz_answers{quiz_num + 1}.txt', 'w', encoding ='UTF-8')

	# Write the header in each quiz file
	quiz_file.write('Name:\n\nSurname:\n\nDate:\n\n')
	quiz_file.write((' ' * 20) + f'European Capitals Quiz {quiz_num + 1}')
	quiz_file.write('\n\n')

	# Shuffles the countries so they are not in alphabetical order
	countries = list(capitals.keys())
	random.shuffle(countries)

	# Loop through each of those 50 countries to create a question for each
	for num in range(50):

		# Creates correct answers by simply querying countries
		correct_answer = capitals[countries[num]]

		# Creates wrong answers by copying the original list, selecting one correct and adding 3 incorrect through sample()
		wrong_answers = list(capitals.values())
		del wrong_answers[wrong_answers.index(correct_answer)]
		wrong_answers = random.sample(wrong_answers, 3)
		answer_options = wrong_answers + [correct_answer]
		random.shuffle(answer_options)

		# Writes each one as a question
		quiz_file.write(f'{num + 1}. Capital of {countries[num]}:\n')
		for i in range(4):
			quiz_file.write(f"		{'ABCD'[i]}. { answer_options[i]}\n")
		quiz_file.write('\n')

		# Writes the answer in each file
		answer_file.write(f"{num +1}.{'ABCD'[answer_options.index(correct_answer)]}")
	quiz_file.close()
	answer_file.close()
