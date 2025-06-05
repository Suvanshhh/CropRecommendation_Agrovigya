from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route("/predict", methods=['POST'])
def predict():
    try:
        data = request.get_json()
        print("Received data:", data)

        N = float(data['Nitrogen'])
        P = float(data['Phosphorus'])  # Check spelling here
        K = float(data['Potassium'])
        temp = float(data['Temperature'])
        humidity = float(data['Humidity'])
        ph = float(data['pH'])
        rainfall = float(data['Rainfall'])

        feature_list = [N, P, K, temp, humidity, ph, rainfall]
        print("Feature list:", feature_list)

        return jsonify({'crop': 'Wheat'})  # Dummy response for now

    except Exception as e:
        print("Error:", str(e))
        return jsonify({'error': str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
