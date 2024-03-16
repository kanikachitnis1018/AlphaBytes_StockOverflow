from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route("/login", methods=['GET','POST'])
def login():
    return render_template('login.html')

@app.route("/register", methods=['GET','POST'])
def register():
    return render_template('register.html')

@app.route("/livemarket", methods=['GET','POST'])
def livemarket():
    return render_template('livemarket.html')

@app.route("/chatbot", methods=['GET','POST'])
def chatbot():
    return render_template('chatbot.html')

@app.route("/analytics", methods=['GET','POST'])
def analytics():
    return render_template('analytics.html')

# @app.route("/llama", methods=['GET','POST'])
# def index():
#     # Make a request to the API
#     response = request.get("https://fingpt-fingpt-forecaster.hf.space/--replicas/pkzfm/")
    
#     # Check if the request was successful (status code 200)
#     if response.status_code == 200:
#         data = response.json()
#         # Pass the data to the template for rendering
#         print(data)
#     else:
#         # If the request was unsuccessful, return an error message
#         return "Error: Unable to fetch data from the API"

if __name__ == "__main__":
    app.run(debug=True)