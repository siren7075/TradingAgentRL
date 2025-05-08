from flask import Flask, jsonify, request, render_template
import requests

app = Flask(__name__)

API_BACKEND = "http://localhost:8080/predict/"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_prediction')
def run_prediction():
    ticker = request.args.get('ticker', '').upper()
    try:
        res = requests.get(API_BACKEND + ticker)
        res.raise_for_status()
        return jsonify(res.json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
