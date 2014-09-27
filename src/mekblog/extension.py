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
	try:
		epath = mekblog.config.setting.core.extension.path.get() + '/' + pathname
		fp = open(epath+'/extension.json','r')
		pkg = json.load(fp)
		for x in ext_list:
			if x['name'] == pkg['name']:
				return
	except Exception, e:
		print 'ERROR in loading extension [%s]' % pathname
		return
	pkg['path'] = epath
	# put in config
	ext_list.append(pkg)
	# load config !! notice version differences
	# load adminpanel
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
