import mekblog

def list_by_archive(small_title):
	db = mekblog.db.db_connect.MekBlog.review
	return db.find({'archive-st':small_title}).sort([('post-time', 1)])

def post(obj):
	if mekblog.archive.list_one({'small-title':obj['archive-st']}) == None:
		return False, 'archive not found'
	db = mekblog.db.db_connect.MekBlog.review
	db.insert(obj)

# EDIT method is not supported cause our design-philosopy
# - People should be RESPONSIBLE for their behavior
