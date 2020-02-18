def word_present(word_from_file, search_word):
	return word_from_file.lower().find(search_word.lower()) != -1

file_name = input("Enter file name: ")
word_to_be_searched = input("Enter word to be searched: ")
word_count = 0
 
with open(file_name, 'r') as file:
    for line in file:
        words = line.split()
        for file_word in words:
        	if(word_present(file_word, word_to_be_searched)):
        		word_count = word_count + 1
print("Occurrences of the word:")
print(word_count)
