from flask import *
import pymongo
import json
import datetime
import os

app_config = __import__('app-config')

app = Flask(__name__)
app.secret_key = os.urandom(24)
blog_config = app_config.load('config.json')

# user access page

@app.route('/')
def index():
	# add tags
	return render_template('index.html')

@app.route('/archives')
def archive_index():
	if 'tag' in request.args:
		tag = request.args['tag']
	else:
		tag = 'none'
	# TODO : add tags
	conn = pymongo.Connection(blog_config['db-host'], blog_config['db-port'])
	archive_list = conn.MekBlog.archive.find().sort([('post-time',-1)]).limit(blog_config['archives-in-a-page'])
	return render_template('archive_index.html', archive_list=archive_list)

@app.route('/archives/<small_title>')
def read_archives(small_title):
	conn = pymongo.Connection(blog_config['db-host'], blog_config['db-port'])
	collection = conn.MekBlog.archive
	arch = collection.find_one({'small-title': small_title})
	if arch == None:
		abort(404)
	else:
		return render_template('archive.html', archive=arch)

# TODO : add review functions

# administrator access page

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'GET':
		if 'admin' in session:
			return redirect(url_for('admin'))
		else:
			return render_template('login.html')
	else:
		if 'username' in request.form and 'password' in request.form:
			if request.form['username'] == blog_config['root-user'] and request.form['password'] ==  blog_config['root-passwd']:
				session['admin'] = 'YES'
				return redirect(url_for('admin'))
			else:
				return render_template('error.html', error_msg="Wrong account or password")
		else:
			abort(404)

@app.route('/logout')
def logout():
	session['admin'] = 'NONE'
	session.pop('admin', None)
	return redirect(url_for('index'))

@app.route('/admin')
def admin():
	if 'admin' in session:
		return render_template('admin.html', root_user=blog_config['root-user'])
	else:
		abort(403)

@app.route('/new-archive', methods=['GET', 'POST'])
def new_archive():
	if 'admin' not in session:
		abort(403)
	if request.method == 'GET':
		return render_template('new-archive.html')
	else:
		# TODO: forward: check script
		conn = pymongo.Connection(blog_config['db-host'], blog_config['db-port'])
		collection = conn.MekBlog.archive
		if collection.find_one({'small-title':request.form['small-title']}):
			return render_template('error.html', error_msg='Same SMALL-TITLE already exists in another archive.')
		collection.insert({
			'title': request.form['title'],
			'small-title': request.form['small-title'],
			'content': request.form['content'],
			'tag': request.form['tag'].split(','),
			'post-time': datetime.datetime.utcnow().isoformat(),
			'last-edit-time': datetime.datetime.utcnow().isoformat()
		})
		# TODO: make error & alert page unified
		return redirect(url_for('index'))
	
# TODO: ajax access page

# run as __main__

if __name__ == '__main__':
	app.run(debug=True)
