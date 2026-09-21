#Write a function to convert a list of words into a sentence.

def create_sentences(words):
	sentence = ""
	for word in words:
		if sentence == "":
			sentence += word
			continue
		sentence += " "
		sentence += word
	return sentence.strip()

if __name__ == '__main__':
	words = ["hola", "como", "estas"]
	print(create_sentences(words))