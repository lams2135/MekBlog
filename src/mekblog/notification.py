# package notification

notify_list = {}

def init_event(event):
	notify_list[event] = {'publisher': [], 'subscriber': []}

def register_publisher(event, obj):
	if event not in notify_list:
		init_event(event)
	if [x for x in notify_list[event]['publisher'] if x['name'] == obj['name']] != []:
		return False, 'same publisher registered'
	notify_list[event]['publisher'].append(obj)
	return True, None

def remove_publisher(event, name):
	if event in notify_list:
		pb = [x for x in notify_list[event]['publisher'] if x['name'] == name]
		if pb != []:
			for y in pb:
				notify_list[event]['publisher'].remove(y)
			return True, None
	return  False, 'publisher/event not found'

def list_publisher(event):
	if event in notify_list:
		return notify_list[event]['publisher']
	else:
		return []

def register_subscriber(event, obj):
	if event not in notify_list:
		init_event(event)
	if [x for x in notify_list[event]['subscriber'] if x['name'] == obj['name']] != []:
		return False, 'same subscriber registered'
	notify_list[event]['subscriber'].append(obj)
	return True, None

def remove_subscriber(event, name):
	if event in notify_list:
		sb = [x for x in notify_list[event]['subscriber'] if x['name'] == name]
		if sb != []:
			for y in sb:
				notify_list[event]['subscriber'].remove(y)
			return True, None
	return False, 'subscriber/event not found'

def publish(event, obj):
	if event not in notify_list:
		return
	for x in notify_list[event]['subscriber']:
		try:
			x['response-method'](obj)
		except:
			print "EXCEPTION"

