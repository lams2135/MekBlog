import flask
import mekblog

# TODO: mainly write a render to build HTML+JS dynamically

# adminpanel_view = flask.Blueprint(__name__)

@adminpanel_view.route('/settings')
def adminpanel_view_main():
	return adminpanel_view('')

@adminpanel_view.route('/settings/<mod>')
def adminpanel_view_page(mod):
	if mod == '':
		# home
	else:
		# route extension
	pass

'''
def render_child_panel(router):
	# router is extension name or 'core' or ''
	# get extension information from mekblog.extension
	# put them into HTML+JS
	pass
'''

