from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'author': 'sunny',
        'title': 'blog post 1',
        'body': 'first post ever',
        'date': 'April 2, 2021'
    },
    {
        'author': 'wahane',
        'title': 'dummy post',
        'body': 'second post ever',
        'date': 'April 3, 2021'
    }
]


@app.route("/")
def home():
    return render_template('home_page.html', posts=posts)


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register')
def register():
    return "hello world"