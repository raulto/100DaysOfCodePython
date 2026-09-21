#Create a dictionary of words and their frequencies.
def create_dict(sentence):
	list_words = sentence.split()
	dict_words = dict.fromkeys(list_words	,0)
	for word in list_words:
		if word in dict_words:
			dict_words[word] += 1
	print(dict_words)		

if __name__ == '__main__':
	sentence  = "python is easy and python is powerful and python is popular"
	create_dict(sentence)