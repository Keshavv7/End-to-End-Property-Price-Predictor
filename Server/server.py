from flask import Flask, request, jsonify
import util
app = Flask(__name__)


@app.route('/get_location')
def get_location():
    response = jsonify({
        'locations': util.get_location()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    sqft = float(request.form['sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])
    balcony = int(request.form['balcony'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location, sqft, bhk, bath, balcony)
    })

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == '__main__':
    print('Starting Python Flask Server for Real Estate Price Prediction...')
    util.load_artifacts()
    app.run()