import pymongo
import datetime

import mekblog

db_connect = None

def connect():
	global db_connect
	db_connect = mekblog.db.db_connect.MekBlog.archive

def list_all(query_obj):
	return db_connect.find(query_obj).sort([('post-time', -1)])

def list_one(query_obj):
	return db_connect.find_one(query_obj)

def post(inform):
	if db_connect.find_one({'small-title': inform['small-title']}):
		return False, 'Same SMALL-TITLE already exists in another archive'
	archive = {
		'title': inform['title'],
		'small-title': mekblog.security.antiXSS(inform['small-title']),
		'content': inform['content'],
		'tag': [x.strip() for x in inform['tag'].split(',')],
		'post-time': datetime.datetime.utcnow().isoformat(),
		'last-edit-time': datetime.datetime.utcnow().isoformat()
	}
	db_connect.insert(archive)
	return True, None

def update(inform):
	inform['small-title'] = mekblog.security.antiXSS(inform['small-title'])
	query_obj = {'small-title': inform['small-title']}
	if not db_connect.find_one(query_obj):
		return False, 'SMALL-TITLE not found'
	update_obj = {
		"$set": {
			'title': inform['title'],
			'content': inform['content'],
			'tag': [x.strip() for x in inform['tag'].split(',')],
			'last-edit-time': datetime.datetime.utcnow().isoformat()
		}
	}
	db_connect.update(query_obj, update_obj)
	return True, None

def remove(query_obj):
	db_connect.remove(query_obj)
# TODO: add: edit & delete op
