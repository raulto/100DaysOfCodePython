#Reverse words in a sentence.

def reverse_sentence(sentence):
	list_words = sentence.split();
	print(list_words[::-1])
	new_sentence = ""
	for word in list_words:
		if new_sentence:
			new_sentence += " "
		new_sentence += word[::-1]
	#print(new_sentence)


if __name__ == '__main__':
	sentence = "python is easy and python is powerful"

	reverse_sentence(sentence)