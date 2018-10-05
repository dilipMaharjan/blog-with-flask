from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World'


@app.route('/hi')
def hi():
    return 'Hi'


@app.route('/hi/<username>')
def hi_user(username):
    return 'hi {}'.format(username)


@app.route('/post/<int:post_id>')
def post(post_id):
    return 'Post Id %d' % post_id


if __name__ == '__main__':
    app.debug = True
    app.run(port=9090)
