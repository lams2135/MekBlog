from flask import *
import json
import os
import mekblog


# initial
app = Flask(__name__)
app.secret_key = os.urandom(24)
mekblog.config.load('config.json')
mekblog.db.connect()
mekblog.tag.update()
mekblog.tag.load()

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
	tag_list = mekblog.tag.get_list()
	return render_template('archive-index.html', archive_list=archive_list, tag_list=tag_list, session=session)

@app.route('/archives/<small_title>')
def read_archive(small_title):
	archive = mekblog.archive.list_one({'small-title': small_title})
	if archive == None:
		abort(404)
	else:
		tag_list = mekblog.tag.get_list()
		return render_template('archive.html', archive=archive, tag_list=tag_list, session=session)

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
			if request.form['username'] == mekblog.config.setting.core.root.uid.get():
				if request.form['password'] ==  mekblog.config.setting.core.root.passwd.get():
					session['admin'] = mekblog.config.setting.core.root.uid.get()
					return redirect(url_for('admin'))
			return render_template('info.html', msg="Wrong account or password")
		else:
			abort(400)

@app.route('/logout')
def logout():
	session['admin'] = 'None'
	session.pop('admin', None)
	return redirect(url_for('index'))

@app.route('/admin')
def admin():
	if 'admin' in session:
		return render_template('admin.html', root_user=mekblog.config.setting.core.root.uid.get())
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
		# TODO: forward: rich-text editor
		result, msg = mekblog.archive.post({
			'title': request.form['title'],
			'small-title': request.form['small-title'],
			'content': request.form['content'],
			'tag': request.form['tag']
		})
		# TODO: make error & alert page unified
		if not result:
			return render_template('info.html', msg=msg)
		else:
			return redirect(url_for('archive_index'))

@app.route('/edit-archive', methods=['GET', 'POST'])
def edit_archive():
	if 'admin' not in session:
		abort(403)
	if request.method == 'GET':
		if 'st' not in request.args:
			abort(404)
		archive = mekblog.archive.list_one({'small-title': request.args['st']})
		if archive == None:
			abort(404)
		return render_template('edit-archive.html', archive=archive)
	if request.method == 'POST':
		result, msg = mekblog.archive.update({
			'title': request.form['title'],
			'small-title': request.form['small-title'],
			'content': request.form['content'],
			'tag': request.form['tag']
		})
		if not result:
			return render_template('info.html', msg=msg)
		else:
			# TODO: improve tag function
			return redirect(url_for('read_archive', small_title=request.form['small-title']))

@app.route('/remove-archive')
def remove_archive():
	if 'admin' not in session:
		abort(403)
	if 'st' not in request.args:
		abort(404)
	mekblog.archive.remove({'small-title': request.args['st']})
#	mekblog.comment.remove(request.args['st'])
	return redirect(url_for('archive_index'))

# TODO: ajax access page

@app.route('/comment/post', methods=['POST'])
def post_comment():
	indata = request.json
	msg = mekblog.comment.post(indata)
	return jsonify(msg), msg['code']

@app.route('/comment/list')
def get_comment():
	if 'st'not in request.args:
		abort(400)
	cmt = mekblog.comment.list_by_archive(request.args['st'])
	return render_template('comment.piece.html', cmt_list=cmt)

@app.route("/settings", methods=["GET","POST"])
def adminpanel():
	if "admin" not in session:
		abort(403)
	if request.method == "GET":
		data = dict(mekblog.config.setting.core.root.get().items() + mekblog.config.setting.archive.get().items() + mekblog.config.setting.email.get().items())
		return render_template("adminpanel.html", data=data)
	else:
		f = mekblog.config.setting.core.root
		form = dict(request.form)
		# return str(form)
		# TODO: config object's views function
		for i in f.get().items():
			f.cd(i[0]).set(form[i[0]][0])
		f = mekblog.config.setting.archive
		for i in f.get().items():
			f.cd(i[0]).set(form[i[0]][0])
		f = mekblog.config.setting.email
		for i in f.get().items():
			f.cd(i[0]).set(form[i[0]][0])
		mekblog.config.save("config.json")
		data = dict(mekblog.config.setting.core.root.get().items() + mekblog.config.setting.archive.get().items() + mekblog.config.setting.email.get().items())
		signal = {"after-post":1}
		return render_template("adminpanel.html", data=data, signal=signal)
		# json
		

# run as __main__

if __name__ == '__main__':
	app.run(debug=True,host='0.0.0.0',port=8080)
