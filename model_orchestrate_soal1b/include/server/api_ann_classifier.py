from flask import Flask, request, jsonify
#import mlflow.pyfunc
import numpy as np
import pickle

#mlflow.environment_variables.MLFLOW_DOWNLOAD_CHUNK_TIMEOUT=600
# Load the scaler
#scaler = pickle.load('scaler.pkl')
app = Flask(__name__)
#mlflow.set_tracking_uri("http://0.0.0.0:5005")
# Load the run_id from file
#with open("run_id.txt", "r") as f:
#    run_id = f.read().strip()

# Load the model using MLflow
#model_uri = f"runs:/{run_id}/model"  # Replace <run_id> with your actual run ID
#model = mlflow.pyfunc.load_model(model_uri)
with open('/opt/airflow/include/model/model.pkl','rb') as pickle_model:
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

        # Scale the features
        #features = scaler.transform(features)

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
    app.run(host='0.0.0.0', port=5001,debug=True)
