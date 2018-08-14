from flask import Flask,render_template,request,session,redirect,url_for,escape

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    user={'username':'liu','usersex':'男'}

    return render_template("user.html",title="hello",username=user['username'],usersex=user['usersex'])


@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # session['username'] = request.form['username']
        # print('index')
        return redirect(url_for('index'))
    print('hello')
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=text name=password>
            <p><input type=submit value=Login>
        </form>
    '''



if __name__ == '__main__':
    app.run(debug=True)
