from flask import render_template, flash, redirect, url_for, request
from app import app, db, bcrypt, login_manager
from models import User
from forms import LoginForm, RegisterForm, ArimaForm

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user:
            flash(f'Success! You are logged in as: {attempted_user.username}', category='success')
            return redirect(url_for('index'))
        else:
            flash('Login unsuccessful. Please check your credentials and try again.', category='danger')
    return render_template('login.html', form=form)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST':
        user_to_create = User(username=form.username.data,
                              email=form.email.data,
                              password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        flash(f"Account created, you are now logged in as {user_to_create.username}", category="success")
        return redirect(url_for('index'))
    return render_template('register.html', form=form)

@app.route("/livemarket", methods=['GET', 'POST'])
def livemarket():
    return render_template('livemarket.html')

@app.route("/analytics", methods=['GET', 'POST'])
def analytics():
    form = ArimaForm()
    if request.method == 'POST':
        return redirect(url_for('dashboard'))
    return render_template('analytics.html', form=form)

@app.route("/dashboard", methods=['GET', 'POST'])
def dashboard():
    return render_template('dashboard.html')
