import mekblog

def list_by_archive(small_title):
	db = mekblog.db.db_connect.MekBlog.comment
	res =  db.find({'archive-st':small_title}).sort([('post-time', -1)])
	cmt_list = []
	for item in res:
		ret.append({
			'name': item['name'],
			'content': item['content'],
			'post-time': item['post-time'],
			'rev-father': item['rev-father'],
			'_id': item['_id']
		})
	return cmt_list

def post(obj):
	if mekblog.archive.list_one({'small-title':obj['archive-st']}) == None:
		return False, 'archive not found'
	db = mekblog.db.db_connect.MekBlog.comment
	db.insert(obj)
	return True, None

# EDIT method is not supported cause our design-philosopy
# - People should be RESPONSIBLE for their behavior

# REMOVE method is only accessable for admin
