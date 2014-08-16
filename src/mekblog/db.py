import pymongo

import mekblog.config

db_connect = None

def connect():
	global db_connect
	global ready
	if 'db-host' not in mekblog.config.settings or 'db-port' not in mekblog.config.settings:
		conn = pymongo.Connection('0.0.0.0', 27017)
		raise ValueError('mekblog.config not load or missing keys')
	else:
		conn = pymongo.Connection(mekblog.config.settings['db-host'], mekblog.config.settings['db-port'])
	db_connect = conn
