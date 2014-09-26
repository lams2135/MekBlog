import mekblog
import flask
import json

ext_list = []

# interface to mekblog

def init():
	# load all extensions
	# disable all extensions
	pass

def load(pathname): # repeated calling acts reload
	# get path and load extension.json
	fp = (mekblog.config.settings.core.extension.d + '/' + pathname)
	pkg = json.load(fp)
	for x in ext_list:
		if x['name'] == pkg['name']:
			return
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

def run_initial():
	pass

# interface to extensions

def register_initial(func):
	pass

def register_view(obj):
	pass
