import pickle
import pandas as pd
import sys
sys.path.insert(0,'/opt/airflow/dags/script')
from utils.db import get_db_con
from datetime import datetime

TABLE_NAME_IRIS='iris'
TABLE_NAME_PREDICT='prediction'

current_time = datetime.now()

def get_conn():
    con = get_db_con()
    return con

def get_model():
     with open('/opt/airflow/include/model/model.pkl','rb') as pickle_model:
          model = pickle.load(pickle_model)
     return model

def insert_data_iris():
     con_db = get_conn()
     dataset_df = pd.read_csv('/opt/airflow/include/dataset/Iris.csv')
     dataset_df.to_sql(TABLE_NAME_IRIS,con=con_db, if_exists='replace',index=False)

def read_data_iris():
     con_db = get_conn()
     sql = '''
     SELECT iris."Id", iris."SepalLengthCm", iris."SepalWidthCm", iris."PetalLengthCm", iris."PetalWidthCm" FROM iris
     '''
     read_data_df = pd.read_sql(sql,con_db)
     print('Table Input')
     #print(read_data_df)
     return read_data_df

def write_prediction_result():
     model =  get_model()
     con_db = get_conn()
     data_iris = read_data_iris()
     sql_feature_column = '''
     SELECT iris."SepalLengthCm", iris."SepalWidthCm", iris."PetalLengthCm", iris."PetalWidthCm" FROM iris
     '''
     feature_column = pd.read_sql(sql_feature_column,con_db)
     prediction_result = model.predict(feature_column)
     results_df = pd.DataFrame({'Id': data_iris.iloc[feature_column.index]['Id'], 'Predicted_Species': prediction_result, 'executed_timed': current_time})
     print("table output")
     print(results_df)
     results_df.to_sql(TABLE_NAME_PREDICT,con=con_db, if_exists='replace',index=False)
