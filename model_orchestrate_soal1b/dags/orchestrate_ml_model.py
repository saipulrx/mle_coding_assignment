from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.postgres_operator import PostgresOperator
from airflow.operators.python_operator import PythonOperator
from script import call_model

default_args = {
    "owner": "saipul",
    "start_date": datetime(2024, 1, 28),
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "email": "msaipulrx@gmail.com",
    "retries": 1,
    "retry_delay": timedelta(minutes=5)
}

with DAG(dag_id="orchestrate_ml_model", schedule_interval="0 10 * * *", default_args=default_args, catchup=False) as dag:

    create_table_iris = PostgresOperator(
        task_id='createTable',
        postgres_conn_id='postgres_conn',
        sql='sql/create_table_iris.sql'
    )

    insert_data_iris = PythonOperator(
        task_id='insert_data_iris',
        python_callable=call_model.insert_data_iris
    )

    retrieve_data_iris = PythonOperator(
        task_id='retrieve_data_iris',
        python_callable=call_model.read_data_iris
    )

    prediction_result = PythonOperator(
        task_id='prediction_result',
        python_callable=call_model.write_prediction_result
    )

    create_table_iris >> insert_data_iris >> retrieve_data_iris >> prediction_result
