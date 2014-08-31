import mekblog.adminpanel
import mekblog.config
import mekblog.notification
import flask
import json

# interface to mekblog

def init():
	# load all extensions
	# exec all initial operation
	pass

def load(ext):
	# name check
	# load extension.json
	# put in config
	# register in adminpanel
	# import module
	# register initial	 
	# register view
	# deal with template & static files
	pass


# interface to extensions

def register_initial(func):
	pass

def register_view(obj):
	pass
