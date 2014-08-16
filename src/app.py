from flask import *
import pymongo
import os
import mekblog
from mekblog.security import antiXSS


app = Flask(__name__)
app.secret_key = os.urandom(24)
mekblog.config.load('config.json')
mekblog.archive.connect_db()

# user access page

@app.route('/')
def index():
	# add tags
	return render_template('index.html')

@app.route('/archives')
def archive_index():
	if 'tag' in request.args:
		opt = {'tag': request.args['tag']}
	else:
		opt = {}
	archive_list = mekblog.archive.list_all(opt)
	return render_template('archive_index.html', archive_list=archive_list)

@app.route('/archives/<small_title>')
def read_archives(small_title):
	archive = mekblog.archive.list_one({'small-title': small_title})
	if archive == None:
		abort(404)
	else:
		return render_template('archive.html', archive=archive)

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
			if request.form['username'] == mekblog.config.settings['root-user'] and request.form['password'] ==  mekblog.config.settings['root-passwd']:
				session['admin'] = 'YES'
				return redirect(url_for('admin'))
			else:
				return render_template('error.html', error_msg="Wrong account or password")
		else:
			abort(404)

@app.route('/logout')
def logout():
	session['admin'] = 'None'
	session.pop('admin', None)
	return redirect(url_for('index'))

@app.route('/admin')
def admin():
	if 'admin' in session:
		return render_template('admin.html', root_user=mekblog.config.settings['root-user'])
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
		result, msg = mekblog.archive.post({
			'title': request.form['title'],
			'small-title': antiXSS(request.form['small-title']),
			'content': request.form['content'],
			'tag': request.form['tag'],
		})
		# TODO: make error & alert page unified
		if not result:
			return render_template('error.html', error_msg=msg)
		else:
			return redirect(url_for('index'))
	
# TODO: ajax access page

# run as __main__

if __name__ == '__main__':
	app.run(debug=True)
