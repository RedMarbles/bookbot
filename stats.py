def count_words(string):
	"""Counts the number of words inside an input string"""
	words = string.split()
	return len(words)

def count_each_character(string):
	"""
	Takes the text from the book as a string
	returns the number of times each character, (including symbols and spaces), 
	appears in the string (upper and lowercase characters are considered the same)
	"""
	string = string.lower()
	char_counts = {}
	for c in string:
		if c in char_counts:
			char_counts[c] += 1
		else:
			char_counts[c] = 1
	return char_counts

def sort_char_counts(char_counts):
	char_list = [ {"char": c, "num": v} for c, v in char_counts.items() if c.isalpha() ]
	char_list.sort(reverse=True, key=lambda cv: cv["num"])
	return char_list
