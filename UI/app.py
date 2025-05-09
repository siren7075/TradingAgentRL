from flask import Flask, jsonify, request, render_template

 app = Flask(__name__)
 
API_BACKEND = "http://localhost:8080/predict/"

# Mock data structure for stock predictions
MOCK_DATA = [
    {
        "ticker": "AAPL",
        "action": "BUY",
        "comments": "Apple Inc. continues to demonstrate strong fundamentals and robust revenue growth. Given the positive market sentiment and innovative product pipeline, a buy recommendation is warranted with high confidence.",
        "confidence": 0.77,
        "suggested_shares": 834,
        "models": [
            {
                "name": "PPO_Risk",
                "accuracy_90d": 0.70,
                "annualized_return": 0.15,
                "sharpe_ratio": 1.30,
                "max_drawdown": -0.10,
                "volatility": 0.20
            },
            {
                "name": "TD3_Safe",
                "accuracy_90d": 0.75,
                "annualized_return": 0.12,
                "sharpe_ratio": 1.50,
                "max_drawdown": -0.08,
                "volatility": 0.15
            },
            {
                "name": "CPPO_Smart",
                "accuracy_90d": 0.78,
                "annualized_return": 0.18,
                "sharpe_ratio": 1.40,
                "max_drawdown": -0.09,
                "volatility": 0.18
            }
        ]
    },
    {
        "ticker": "AMZN",
        "action": "SELL",
        "comments": "Amazon is currently facing significant challenges due to increased competition and slowing growth in its core e-commerce business. A sell recommendation is advised with high confidence.",
        "confidence": 0.67,
        "suggested_shares": 500,
        "models": [
            {
                "name": "PPO_Risk",
                "accuracy_90d": 0.65,
                "annualized_return": 0.10,
                "sharpe_ratio": 1.20,
                "max_drawdown": -0.15,
                "volatility": 0.25
            },
            {
                "name": "TD3_Safe",
                "accuracy_90d": 0.70,
                "annualized_return": 0.08,
                "sharpe_ratio": 1.10,
                "max_drawdown": -0.12,
                "volatility": 0.20
            },
            {
                "name": "CPPO_Smart",
                "accuracy_90d": 0.72,
                "annualized_return": 0.09,
                "sharpe_ratio": 1.15,
                "max_drawdown": -0.13,
                "volatility": 0.22
            }
        ]
    },
    {
        "ticker": "TSLA",
        "action": "SELL",
        "comments": "Tesla's stock is under pressure due to concerns about demand in key markets and increased competition in the electric vehicle sector. A cautious sell is recommended with moderate confidence.",
        "confidence": 0.34,
        "suggested_shares": 300,
        "models": [
            {
                "name": "PPO_Risk",
                "accuracy_90d": 0.68,
                "annualized_return": 0.11,
                "sharpe_ratio": 1.25,
                "max_drawdown": -0.14,
                "volatility": 0.22
            },
            {
                "name": "TD3_Safe",
                "accuracy_90d": 0.72,
                "annualized_return": 0.09,
                "sharpe_ratio": 1.20,
                "max_drawdown": -0.10,
                "volatility": 0.18
            },
            {
                "name": "CPPO_Smart",
                "accuracy_90d": 0.74,
                "annualized_return": 0.12,
                "sharpe_ratio": 1.30,
                "max_drawdown": -0.11,
                "volatility": 0.20
            }
        ]
    },
    {
        "ticker": "WDAY",
        "action": "SELL",
        "comments": "Workday Inc. is experiencing slowing growth in enterprise software adoption, and market sentiment is currently negative. A sell recommendation is advised with moderate confidence.",
        "confidence": 0.3,
        "suggested_shares": 200,
        "models": [
            {
                "name": "PPO_Risk",
                "accuracy_90d": 0.67,
                "annualized_return": 0.09,
                "sharpe_ratio": 1.15,
                "max_drawdown": -0.13,
                "volatility": 0.21
            },
            {
                "name": "TD3_Safe",
                "accuracy_90d": 0.71,
                "annualized_return": 0.07,
                "sharpe_ratio": 1.10,
                "max_drawdown": -0.09,
                "volatility": 0.17
            },
            {
                "name": "CPPO_Smart",
                "accuracy_90d": 0.73,
                "annualized_return": 0.10,
                "sharpe_ratio": 1.20,
                "max_drawdown": -0.10,
                "volatility": 0.19
            }
        ]
    },
    {
        "ticker": "NVDA",
        "action": "BUY",
        "comments": "NVIDIA is benefiting from strong demand for AI chips and robust growth in gaming and data center markets. A strong buy recommendation is warranted with high confidence.",
        "confidence": 0.78,
        "suggested_shares": 400,
        "models": [
            {
                "name": "PPO_Risk",
                "accuracy_90d": 0.80,
                "annualized_return": 0.20,
                "sharpe_ratio": 1.50,
                "max_drawdown": -0.08,
                "volatility": 0.15
            },
            {
                "name": "TD3_Safe",
                "accuracy_90d": 0.85,
                "annualized_return": 0.18,
                "sharpe_ratio": 1.60,
                "max_drawdown": -0.06,
                "volatility": 0.12
            },
            {
                "name": "CPPO_Smart",
                "accuracy_90d": 0.88,
                "annualized_return": 0.22,
                "sharpe_ratio": 1.55,
                "max_drawdown": -0.07,
                "volatility": 0.14
            }
        ]
    }
]

# Default response if ticker is not found
DEFAULT_RESPONSE = {
    "action": "N/A",
    "comments": "Check More Details",
    "confidence": "N/A",
    "suggested_shares": "N/A",
    "models": [
        {
            "name": "PPO_Risk",
            "accuracy_90d": 0.80,
            "annualized_return": 0.20,
            "sharpe_ratio": 1.50,
            "max_drawdown": -0.08,
            "volatility": 0.15
        },
        {
            "name": "TD3_Safe",
            "accuracy_90d": 0.85,
            "annualized_return": 0.18,
            "sharpe_ratio": 1.60,
            "max_drawdown": -0.06,
            "volatility": 0.12
        },
        {
            "name": "CPPO_Smart",
            "accuracy_90d": 0.88,
            "annualized_return": 0.22,
            "sharpe_ratio": 1.55,
            "max_drawdown": -0.07,
            "volatility": 0.14
        }
    ]
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_prediction')
def run_prediction():
    ticker = request.args.get('ticker', '').upper()
    # Search for the ticker in the mock data
    for stock in MOCK_DATA:
        if stock["ticker"] == ticker:
            return jsonify(stock)
    # Return default response if ticker is not found
    return jsonify(DEFAULT_RESPONSE)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
