import pymongo
import datetime

import mekblog.config

db_connect = None

def connect_db():
	global db_connect
	if 'db-host' not in mekblog.config.settings or 'db-port' not in mekblog.config.settings:
		conn = pymongo.Connection('0.0.0.0', 27017)
		raise ValueError('mekblog.config not load or missing keys')
	else:
		conn = pymongo.Connection(mekblog.config.settings['db-host'], mekblog.config.settings['db-port'])
	db_connect = conn.MekBlog.archive

def list_all(query_obj):
	return db_connect.find(query_obj).sort([('post-time', -1)])

def list_one(query_obj):
	return db_connect.find_one(query_obj)

def post(inform):
	if db_connect.find_one({'small-title': inform['small-title']}):
		return False, 'Same SMALL-TITLE already exists in another archive'
	archive = {
		'title': inform['title'],
		'small-title': inform['small-title'].replace(' ', '-'),
		'content': inform['content'],
		'tag': inform['tag'].split(','),
		'post-time': datetime.datetime.utcnow().isoformat(),
		'last-edit-time': datetime.datetime.utcnow().isoformat()
	}
	db_connect.insert(archive)
	return True, None

# TODO: add: edit & delete op
