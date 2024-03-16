from stocks import app, db
from flask import render_template
from stocks.models import Item, User
from stocks.forms import RegisterForm, LoginForm, PurchaseItemForm, SellItemForm
from flask import redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from sqlalchemy.exc import IntegrityError

from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            flash(f'Success! You are logged in as: {attempted_user.username}', category='success')
            return redirect(url_for('market_page'))
        else:
            flash('Username and Password do not match, try again', category='danger')
    return render_template('login.html', form=form)


@app.route("/register", methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email=form.email.data,
                              password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(f"Account created, you are now logged in as {{ user_to_create.username }}", category="success")
        return redirect(url_for('market_page')) 
    
    if form.errors != {}: #If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')  
        
    return render_template('register.html', form=form)

@app.route("/livemarket", methods=['GET','POST'])
def livemarket():
    return render_template('livemarket.html')

@app.route("/chatbot", methods=['GET','POST'])
def chatbot():
    return render_template('chatbot.html')

@app.route("/analytics", methods=['GET','POST'])
def analytics():
    return render_template('analytics.html')


if __name__ == "__main__":
    app.run(debug=True)