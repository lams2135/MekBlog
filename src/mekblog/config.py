import json
import mekblog.db

settings = {}

def load(filename):
	global settings
	fp = open(filename, 'r')
	settings = json.load(fp)
	fp.close()
	mekblog.db.connect()
	return settings

# better not pass 'obj' as argument
def save(filename, obj=None):
	fp = open(filename, 'w')
	if obj != None:
		settings = obj
	json.dump(settings, fp, indent = 2)
	fp.close()