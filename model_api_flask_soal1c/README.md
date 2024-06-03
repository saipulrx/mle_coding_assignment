# mle_coding_assignment
This repository for coding assignment register ANN model Iris dataset question 1 point c for role Machine Learning Engineer at Efishery.

Notes : This code both tested virtualenv and docker but i will explain how to reproduce with use virtualenv
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
2. Run code api_ann_classifier.py. Default port is 5000 but you can change to other port at code bellow
```
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7001,debug=True)
```
3. After run, it will display running flask app on ip 127.0.0.1 and other ip randomly
![debug flask app](https://github.com/saipulrx/mle_coding_assignment/blob/main/assets/debug_flask_app.png)

4. Open new terminal and test the API with run command bellow
```
curl -X POST http://192.168.1.3:7001/predict \
    -H "Content-Type: application/json" \
    -d '{
          "instances": [
            {"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2},
            {"sepal_length": 6.2, "sepal_width": 3.4, "petal_length": 5.4, "petal_width": 2.3},
            {"sepal_length": 5.2, "sepal_width": 3.3, "petal_length": 2.4, "petal_width": 1.3}
          ]
        }'
```

5. The result prediction will display bellow
![mlflow UI Experiment](https://github.com/saipulrx/mle_coding_assignment/blob/main/assets/prediction_result_api.png)

    