from flask import Flask, request, jsonify
import numpy as np
import pickle

app = Flask(__name__)
with open('/Users/muhammadsaipulrohman/Documents/Kerja/source_code/mlops/mle_coding_assignment/model_api_flask_soal1c/model/model.pkl','rb') as pickle_model:
     model = pickle.load(pickle_model)

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({"error": "Model could not be loaded"}), 500

    # Get JSON data from the request
    data = request.json
    if not data or 'instances' not in data:
        return jsonify({"error": "No input data provided"}), 400

    instances = data['instances']

    # Prepare the list to store predictions
    predictions = []

    for instance in instances:
        try:
            features = np.array([
                instance['sepal_length'],
                instance['sepal_width'],
                instance['petal_length'],
                instance['petal_width']
            ]).reshape(1, -1)
        except KeyError:
            return jsonify({"error": "Missing or invalid feature keys"}), 400

        # Make prediction
        try:
            prediction = model.predict(features)
            prediction_proba = model.predict_proba(features).max()
            predictions.append({
                "prediction": int(prediction[0]),
                "probability": prediction_proba
            })
        except Exception as e:
            predictions.append({"error": str(e)})

    # Return the predictions as JSON
    return jsonify(predictions)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7001,debug=True)
