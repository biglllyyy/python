from flask import Flask
import confi


app = Flask(__name__)
app.config.from_object(confi)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route("/test/<id>")
def test(id):
    return "id 是 %s" % id


if __name__ == '__main__':
    app.run()
