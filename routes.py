from flask import Flask, render_template, url_for, request
import os

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
# ...
app = Flask('app', template_folder=tmpl_dir)

app = Flask(__name__)


@app.route('/')
def home():
	return render_template('home.html')


@app.route('/user/<username>')
def show_user_profile(username):
	return 'User: %s ' % (username)


@app.route('/post/<int:post_id>')
def show_post(post_id):
	return 'POST: %d' % (post_id)


@app.route('/about')
def about():
	return render_template('about.html')


@app.route('/show_url')
def show_url_for():
	return url_for('show_user_profile', username='Malik')


@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		return "username %s logged in" % request.form['username']
	return render_template('login.html')


'''
@app.route('/login', methods=['GET','POST'])
def login():
	if request.method == 'POST' :
		return 'username is %s' % request.values['username']
	else:
		return '<form method="post" action="/login"><input type = "text" name="username"/><p><button type ="submit">Submit</button>'

'''

if __name__ == '__main__':
	app.debug = True
	app.run()
