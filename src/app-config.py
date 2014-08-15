import json

def load(filename):
	f = open(filename, 'r')
	k = json.load(f)
	f.close()
	return k

def save(obj, filename):
	f = open(filename, 'w')
	json.dump(obj, f, indent=2)
	f.close()

