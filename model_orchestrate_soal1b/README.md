# mle_coding_assignment
This repository for coding assignment register ANN model Iris dataset question 1 point b for role Machine Learning Engineer at Efishery.

Notes : This code only tested on docker
## Prerequisite
- Already install docker and docker compose
- Familiar with Apache Airflow, Machine Learning, docker and create API with Flask

## How to Reproduce:
1. Git clone this repository to your local computer
2. Run docker compose
```
docker compose up -d
```
3. If airflow web server is already up with default port 8080 then go to http://localhost:8080. input username : airflow and password : airflow
4. Create new postgres DB connection in Airflow.
    - Click Admin --> Connection
    - Click New Record
    - Input required field with screenshot bellow
    ![postgres db conn airflow](https://github.com/saipulrx/mle_coding_assignment/blob/main/assets/postgres_conn_airflow.png) then click save
5. enable dag airflow orchestrate_ml_model
6. This dag airflow was scheduled everyday at 10.00 AM but if you want to test this job then click Run
7. After run, click dag airflow with task retrieve data and click logs.
it will display running table input in logs in screenshot bellow
![read table input](https://github.com/saipulrx/mle_coding_assignment/blob/main/assets/logs_table_input.png)

4. Click dag airflow task prediction_result and click logs. It will display running table output in logs in screenshot bellow
![write table output](https://github.com/saipulrx/mle_coding_assignment/blob/main/assets/logs_table_output.png)

5. Click Graph. Airflow dags graph will display bellow
![airflow dags graph](https://github.com/saipulrx/mle_coding_assignment/blob/main/assets/graph_dags_airflow.png)

6. All data of Iris table in postgresql database
![data in iris table](https://github.com/saipulrx/mle_coding_assignment/blob/main/assets/iris_table.png)

7. All data of Prediction result table in postgresql database
![data in prediction table](https://github.com/saipulrx/mle_coding_assignment/blob/main/assets/prediction_table.png)

    