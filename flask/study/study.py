from flask import Flask, session, redirect, url_for, escape, request
import os

app = Flask(__name__)


@app.route('/hello')
@app.route('/word')
def hello():
    return "hello"


@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        print('index')
        return redirect(url_for('index'))
    print('hello')
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

# set the secret key.  keep this really secret:
app.secret_key = os.urandom(24)
#
if __name__ == '__main__':
    # app.logger.error('An error occurred')
    # app.logger.warning('A warning occurred (%d apples)', 42)
    # app.logger.debug('A value for debugging')

    app.run(host='0.0.0.0')