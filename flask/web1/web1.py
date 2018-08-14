from flask import Flask,url_for,render_template

app = Flask(__name__)


@app.route('/')
def login():
    return render_template('login.html')

# @app.route('/test')




if __name__ == '__main__':
    app.run(debug=True)
