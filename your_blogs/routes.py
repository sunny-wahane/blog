from flask import render_template, url_for, flash, redirect, request
from your_blogs import app, bcrypt, db
from your_blogs.models import User, Post
from your_blogs.forms import RegisterForm, LoginForm
from flask_login import login_user, current_user, logout_user, login_required

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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username = form.username.data, password_hash= hashed_password, email = form.email.data)
        db.session.add(user)
        db.session.commit()
        flash(f"Account created for {form.username.data}", 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user and bcrypt.check_password_hash(user.password_hash, form.password.data):
            login_user(user, remember=form.remember.data)
            flash("Login Successful", 'success')
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsucessful. Please check your username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/account")
@login_required
def account():
    return render_template('account.html', title= 'Account')