def word_present(word_from_file, search_word):
	is_same_word = i.lower() == word.lower()
	is_sub_str = i.lower().find(word.lower()) != -1
	return (is_same_word or is_sub_str)

fname = input("Enter file name: ")
word = input("Enter word to be searched: ")
word_count = 0
 
with open(fname, 'r') as f:
    for line in f:
        words = line.split()
        for i in words:
        	if(word_present(i, word)):
        		word_count = word_count + 1
print("Occurrences of the word:")
print(word_count)
