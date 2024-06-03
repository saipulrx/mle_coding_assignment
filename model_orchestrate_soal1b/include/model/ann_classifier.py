import mlflow
from mlflow.models import infer_signature
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn import datasets

# Load the Iris dataset
X, y = datasets.load_iris(return_X_y=True)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Define the model hyperparameters
params = {
    "solver": "lbfgs",
    "max_iter": 1000,
    "random_state": 1
}

# Train the model
ann = MLPClassifier(**params)
ann.fit(X_train, y_train)

# Predict on the test set
y_pred = ann.predict(X_test)

# Calculate metrics
accuracy = accuracy_score(y_test, y_pred)

# Set our tracking server uri for logging
mlflow.set_tracking_uri(uri="http://0.0.0.0:5005")

# Create a new MLflow Experiment
mlflow.set_experiment("MLflow, flask and airflow example")

# Start an MLflow run
with mlflow.start_run() as run:
    # Log the hyperparameters
    mlflow.log_params(params)

    # Log the loss metric
    mlflow.log_metric("accuracy", accuracy)

    # Set a tag that we can use to remind ourselves what this run was for
    mlflow.set_tag("Training Info", "Basic ANN model for iris data")

    # Infer the model signature
    signature = infer_signature(X_train, ann.predict(X_train))

    # Log the model
    model_info = mlflow.sklearn.log_model(
        sk_model=ann,
        artifact_path="iris_ann_model",
        signature=signature,
        input_example=X_train,
        registered_model_name="ann_model",
    )

    print("Run ID: {}".format(run.info.run_id))
    # Save run_id to a file
    with open("run_id.txt", "w") as f:
        f.write(run.info.run_id)
        print("Run ID : {}".format(run.info.run_id) + " successfully saved to run_id.txt")

# Load the model back for predictions as a generic Python Function model
loaded_model = mlflow.pyfunc.load_model(model_info.model_uri)
predictions = loaded_model.predict(X_test)
iris_feature_names = datasets.load_iris().feature_names
result = pd.DataFrame(X_test, columns=iris_feature_names)
result["actual_class"] = y_test
result["predicted_class"] = predictions
print(result[:4])