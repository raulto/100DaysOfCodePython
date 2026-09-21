#Write a function to count the frequency of words in a sentence.

def split_sentences(sentence):
	words = sentence.split()
	#list_of_words = dict.fromkeys(set(words),0)
	list_words = {}
	#print(list_of_words)
	for word in words:
		if word in list_words:
			list_words[word] += 1
		else:
			list_words.update({word: 1})			

	for word, qty in list_words.items():
		print(f"{word} appears {qty} times")
	
	
if __name__ == '__main__':
	sentence = "python is easy and python is powerful"
	split_sentences(sentence)