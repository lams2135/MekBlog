import pymongo

import mekblog

collection = []
db_connect = None

def connect():
	global db_connect
	db_connect = mekblog.db.db_connect.MekBlog.tag

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

def insert(inform):
	global collection
	tp = [x.strip() for x in inform.split(',')]
	for x in tp:
		for y in collection:
			if x in y:
				y[x] += 1
				break
		else:
			collection.append({x:1})

