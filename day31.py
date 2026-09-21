#Merge two dictionaries.

def merge_dict(a,b):
	
	return a | b

if __name__ == '__main__':
	dict1 = {
    	"name": "Raul",
    	"age": 30,
    	"city": "Mexicali"
	}

	dict2 = {
    	"job": "Programmer",
    	"language": "Python",
    	"experience": 1
	}

	print(merge_dict(dict1, dict2))