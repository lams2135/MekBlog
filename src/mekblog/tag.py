import pymongo

import mekblog

collection = []
current = None

def update():
	global collection
	tmp = {}
	archives = mekblog.archive.list_all({})
	for x in archives:
		if 'tag' in x:
			for y in x['tag']:
				if y != '':
					if y in tmp:
						tmp[y] += 1
					else:
						tmp[y] = 1
	collection = []
	for x in tmp:
		collection.append({x:tmp[x]})
	collection.sort(cmp=lambda x,y:cmp(x.values()[0],y.values()[0]),reverse=True)

def suggestion_list():
	mekblog.tag.update()
	global collection
	return [{'tag':x.keys()[0],'count':x.values()[0]} for x in collection]

def save():
	db = mekblog.db.db_connect.Mekblog.piece
	update_obj = {
		'$set': {
			'word': mekblog.tag.current['word']
		}
	}
	db.update({'type':'tag'}, update_obj)

def load():
	global current
	db = mekblog.db.db_connect.MekBlog.piece
	current = db.find_one({'type':'tag'})
	if not current:
		current = {
			'type': 'tag',
			'word': []
		}
		db.insert(current)
	return current

def get_list():
	return mekblog.tag.current['word']

