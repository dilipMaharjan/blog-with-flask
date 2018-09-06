from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello Flask"


@app.route("/me")
def me():
    return '<h1>This is me </h1>'


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port='5000')
