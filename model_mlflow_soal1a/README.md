# mle_coding_assignment
This repository for coding assignment register ANN model Iris dataset question 1 point a for role Machine Learning Engineer at Efishery.

Notes : This code only tested use local virtualenv
## How to Reproduce:
1. Install using pip and virtual environments.
   - Create a new venv
   ```
    python -m venv .venv              # create the environment
   ```
   - Activate that same virtual environment each time you create a shell window or session:
    ```
    source .venv/bin/activate         # activate the environment for Mac and Linux OR
dbt-env\Scripts\activate            # activate the environment for Windows
    ```
    - Install python libraries in requirements.txt
    ```
    pip install -r requirements.txt
    ```
2. Run MLFlow UI in terminal. Default port is 5000, if you want to use other port then use parameter --port
```
mlflow ui --port 6001
```
3. Run code model_ann_iris_v1.py
```
python3 model_ann_iris_v1.py
```

4. Open mlflow ui at http//:127.0.0.1:5000(default)
![mlflow UI](https://github.com/saipulrx/mle_coding_assignment/blob/main/assets/mlflow_ui.png)
5. Click experiment name. It will display history run code and also ml model versioning at tab Models
![mlflow UI Experiment](https://github.com/saipulrx/mle_coding_assignment/blob/main/assets/mlflow_experiment_name.png)

MLFlow Models detail
![mlflow UI Experiment](https://github.com/saipulrx/mle_coding_assignment/blob/main/assets/mlflow_model.png)

    