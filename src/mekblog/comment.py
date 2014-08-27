import datetime
import mekblog

def list_by_archive(small_title):
	db = mekblog.db.db_connect.MekBlog.comment
	res =  db.find({'archive-st':small_title}).sort([('post-time', -1)])
	cmt_list = []
	for item in res:
		cmt_list.append({
			'name': item['name'],
			'content': item['content'],
			'post-time': item['post-time'],
			'reply-to': item['reply-to'],
			'_id': item['_id']
		})
	return cmt_list

def post(obj):
	if 'archive-st' not in obj:
		return {'result': False, 'code':400}
	if mekblog.archive.list_one({'small-title':obj['archive-st']}) == None:
		return {'result': False, 'code':404, 'msg': 'archive not found'}
	db = mekblog.db.db_connect.MekBlog.comment
	if db.find_one(obj):
		return {'result': False, 'code':406, 'msg': 'repeated comment'}
	db.insert({
		'name': obj['name'],
		'email': obj['email'],
		'content': obj['content'],
		'archive-st': obj['archive-st'],
		'reply-to': obj['reply-to'],
		'enable-notify': obj['enable-notify'],
		'post-time': datetime.datetime.utcnow().isoformat()
	})
	return {'result': True, 'code':201}

# EDIT method is not supported cause our design-philosopy
# - People should be RESPONSIBLE for their behavior

# REMOVE method is only accessable for admin
def remove(st):
	db = mekblog.db.db_connect.MekBlog.comment
	db.remove({'archive-st':st})
