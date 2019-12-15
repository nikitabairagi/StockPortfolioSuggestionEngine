import json
from flask import Flask, request, Response, render_template
import StockManager
from flask_cors import CORS, cross_origin


application = Flask(__name__)
CORS(application)
application.config['CORS_HEADERS'] = 'Content-Type'

# This backend service serves following purpose
# Serve front-end
# Sign up and Login functionality
# Allocate money in stocks


@application.route('/allocate', methods=['POST'])
@cross_origin(origin='*')
def allocate_stocks():

    amount = request.json['amount']
    if amount < 5000:
        return json.dumps({"error": "Amount should be more than $5000"}), 500

    strategies = request.json['strategies']
    if len(strategies) == 0:
        return json.dumps({"error": "Select at-least one strategy"}), 500
    if len(strategies) > 2:
        return json.dumps({"error": "Maximum two strategies can be selected together"}), 500

    allocations = StockManager.allocate_stocks(amount, strategies)

    return json.dumps(allocations), 200


@application.route("/")
def serve_template():
    return render_template('index.html')


if __name__ == "__main__":
    application.run(host='0.0.0.0', port=80)
