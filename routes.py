from flask import render_template, flash, redirect, url_for, request
from app import app, db, bcrypt, login_manager
from models import User
from forms import LoginForm, RegisterForm, ArimaForm
import yfinance as yf
from statsmodels.tsa.arima.model import ARIMA

def get_historical_data(symbol, start_date, end_date):
    data = yf.download(symbol, start=start_date, end=end_date)
    return data

def train_arima(data):
    close_prices = data['Close'].values
    model = ARIMA(close_prices, order=(5,1,0)) # ARIMA(p,d,q) with p=5, d=1, q=0
    model_fit = model.fit()
    return model_fit

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
    if form.validate_on_submit():
        symbol = form.stock_code.data
        start_date = form.start_date.data
        end_date = form.end_date.data
        
        # Fetching historical data
        data = get_historical_data(symbol, start_date, end_date)
        
        # Training ARIMA model
        arima_model = train_arima(data)
        
        # Generating predictions using ARIMA
        arima_forecast = arima_model.forecast(steps=5)  # Forecasting next 5 days
        
        # Convert forecast to a list and jsonify it
        forecast_list = arima_forecast.tolist()
        
        return render_template('dashboard.html', forecast_list=forecast_list)
    
    return render_template('analytics.html', form=form)    

@app.route("/dashboard", methods=['GET', 'POST'])
def dashboard():
    sarima_forecast = request.args.get('sarima_forecast')  # Retrieve forecasted values from query parameter
    return render_template('dashboard.html', sarima_forecast=sarima_forecast)
