import mekblog.adminpanel
import mekblog.config
import mekblog.notification
import flask
import json

ext_lists = []

# interface to mekblog

def init():
	# load all extensions
	# disable all extensions
	pass

def load(ext):
	# get path and load extension.json
	# pkg = json.load()
	# name check
	# for x in ext_lists:
	# 	if x['name'] == pkg['name']
	# 		raise Error
	# put in config
	# if name not in conf.extension
	# 	conf.extension.name.set()
	# !! notice version differences
	# import module
	# register initial
	# register view
	# deal with template & static files
	pass

def enable(ext):
	pass

def disable(ext):
	pass

def unload(ext):
	pass

def run_initial():
	pass

# interface to extensions

def register_initial(func):
	pass

def register_view(obj):
	pass
