from flask import render_template, url_for, flash, redirect
from your_blogs import app
from your_blogs.models import User, Post
from your_blogs.forms import RegisterForm, LoginForm


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
