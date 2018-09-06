from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        'author': 'Dilip',
        'title': 'blog 1',
        'content': 'This is a blog post'
    },
    {
        'author': 'John',
        'title': 'blog 2',
        'content': 'This is a blog post'
    },
    {
        'author': 'Matthew',
        'title': 'blog 3',
        'content': 'This is a blog post'
    }
]


@app.route("/")
def hello():
    return "Hello Flask"


@app.route('/home')
def home():
    return render_template('home.html', posts=posts, title="home")


@app.route("/me")
def me():
    return '<h1>This is me </h1>'


@app.route('/about')
def about():
    return render_template('about.html', title='about')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port='5000')
