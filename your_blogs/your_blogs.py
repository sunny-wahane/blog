from flask import Flask, render_template, url_for, flash, redirect
from forms import RegisterForm, LoginForm
import os

app = Flask(__name__)

# To Do :
# replace the secret key
app.config['SECRET_KEY'] = '9c47844038dd8fe3543a9c0b080e8572'


# To Do ;
# replace dummy data with actual data using a database
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


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}", 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("Login Successful", 'success')
        return redirect(url_for('home'))
    return render_template('login.html', title='Login', form=form)