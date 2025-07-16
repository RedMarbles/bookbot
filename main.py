import sys
import stats

def get_book_text(filepath):
	with open(filepath) as f:
		file_contents = f.read()
	return file_contents

def process_book(filepath):
	raw_text = get_book_text(filepath)

	num_words = stats.count_words(raw_text)
	char_counts = stats.count_each_character(raw_text)
	sorted_char_counts = stats.sort_char_counts(char_counts)

	print( "============ BOOKBOT ============")
	print(f"Analyzing book found at {filepath}...")
	print( "----------- Word Count ----------")
	print(f"Found {num_words} total words")
	print( "--------- Character Count -------")
	for cv in sorted_char_counts:
		print(f"{cv["char"]}: {cv["num"]}")
	print( "============= END ===============")



def main():
	args = sys.argv
	if len(args) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	filepath = args[1]
	process_book(filepath)

if __name__ == "__main__":
	main()
