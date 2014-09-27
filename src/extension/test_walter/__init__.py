import mekblog

def mekblogArchiveEventHandler(obj):
	mekblog.notification.publish('email.sendmail', {
		'title':'MekBlog Archive Mail',
		'to_addr':'lams2135@gmail.com',
		'content':'test mekblog.archive event received. post or update.'
	})
	pass

def onload():
	publisher_obj = {'name':'test_walter','description':'NULL'}
	subscriber_obj = {'name':'test_walter', 'response-method':mekblogArchiveEventHandler}
	# register publisher service
	mekblog.notification.register_publisher('email.sendmail', publisher_obj)
	# register listener to mekblog.archive
	mekblog.notification.register_subscriber('mekblog.archive', subscriber_obj)

def unload():
	# implement interface
	pass

