from flask import Flask, render_template, request, jsonify
from gradio_client import Client

app = Flask(__name__)

@app.route('/get_prediction', methods=['POST', 'GET'])
def get_prediction():
    if request.method == 'POST':
        # Get input data from the form
        ticker = request.form['ticker']
        date = request.form['date']
        n_weeks = request.form['n_weeks']
        use_latest_basic_financials = bool(request.form.get('use_latest_basic_financials'))
        
        # Make a prediction request to the API
        client = Client("https://fingpt-fingpt-forecaster.hf.space/--replicas/pkzfm/")
        result = client.predict(
            ticker,
            date,
            n_weeks,
            use_latest_basic_financials,
            api_name="/predict"
        )
        
        # Return the result as JSON response
        return jsonify(result)
    
    # Render the form template for GET requests
    return render_template('test.html')

if __name__ == "__main__":
    app.run(debug=True)
