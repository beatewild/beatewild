"""
full_name = "beatewild"

def count_letters(full_name):
	letter_counts = {}
	for letter in full_name:
		if (letter not in letter_counts):
			letter_counts[letter] = 1
		else:
			letter_counts[letter] += 1
	return letter_counts
print count_letters(full_name)

#alternative Methode:

letter_counts = {}
for letter in full_name:
	letter_counts[letter] = letter_counts.get(letter, 0) + 1
print letter_counts

"""
#txt-file muss im gleichen Ordner gespeichert sein 
#open txt mit runden Klammern und in Anfuehrungsstrichen

my_file = open("one_fish_two_fish.txt")
poem = my_file.read()
my_file.close()

def count_letters(poem):
	letter_counts = {}
	for letter in poem:
		if (letter not in letter_counts):
			letter_counts[letter] = 1
		else:
			letter_counts[letter] += 1
	del letter_counts["?"], letter_counts["."], letter_counts[","], letter_counts["!"]
	return letter_counts
print count_letters(poem)


