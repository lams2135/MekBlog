import datetime
import mekblog

# mekblog.archive publisher register
publisher_obj = {'name':'mekblog.archive', 'description':'NULL'}
mekblog.notification.register_publisher('mekblog.archive', publisher_obj)

def list_all(query_obj):
	db = mekblog.db.db_connect.MekBlog.archive
	return db.find(query_obj).sort([('post-time', -1)])

def list_one(query_obj):
	db = mekblog.db.db_connect.MekBlog.archive
	return db.find_one(query_obj)

def post(inform):
	db = mekblog.db.db_connect.MekBlog.archive
	if db.find_one({'small-title': inform['small-title']}):
		return False, 'Same SMALL-TITLE already exists in another archive'
	archive = {
		'title': inform['title'],
		'small-title': mekblog.security.antiXSS(inform['small-title']),
		'content': inform['content'],
		'tag': [x.strip() for x in inform['tag'].split(',')],
		'post-time': datetime.datetime.utcnow().isoformat(),
		'last-edit-time': datetime.datetime.utcnow().isoformat()
	}
	db.insert(archive)
	mekblog.notification.publish('mekblog.archive',{
		'event':'post',
		'title':archive['title'],
		'time':archive['post-time']
	})
	return True, None

def update(inform):
	db = mekblog.db.db_connect.MekBlog.archive
	inform['small-title'] = mekblog.security.antiXSS(inform['small-title'])
	query_obj = {'small-title': inform['small-title']}
	if not db.find_one(query_obj):
		return False, 'SMALL-TITLE not found'
	update_obj = {
		'$set': {
			'title': inform['title'],
			'content': inform['content'],
			'tag': [x.strip() for x in inform['tag'].split(',')],
			'last-edit-time': datetime.datetime.utcnow().isoformat()
		}
	}
	db.update(query_obj, update_obj)
	mekblog.notification.publish('mekblog.archive', {
		'event':'update',
		'title':update_obj['title'],
		'time':update_obj['last-edit-time']
	})
	return True, None

def remove(query_obj):
	db = mekblog.db.db_connect.MekBlog.archive
	db.remove(query_obj)

