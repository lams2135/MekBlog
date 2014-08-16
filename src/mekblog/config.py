import json

settings = {}
ready = False

def load(filename):
	global settings
	global ready
	fp = open(filename, 'r')
	settings = json.load(fp)
	ready = True
	fp.close()
	return settings

# better not pass 'obj' as argument
def save(filename, obj=None):
	fp = open(filename, 'w')
	if obj != None:
		settings = obj
	json.dump(settings, fp, indent = 2)
	fp.close()
