from sqlalchemy import create_engine
from sqlalchemy.dialects import postgresql
from exception.exception import InvalidConnectionString

# Connect to engine db
def get_db_con():
    username = 'postgres'
    password = '12345'
    host = 'host.docker.internal'
    port = '5432'
    database = 'demo_intro_sql'

    CONN_STRING = f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}'
    if not CONN_STRING:
        raise InvalidConnectionString("Connection string not set")
    
    engine = create_engine(CONN_STRING)
    return engine

# Call this function for run query
def execute_sql(query: str):
    engine = get_db_con()
    with engine.connect() as con:
        con.execute(query)

# Upsert method
def pg_upsert(table, conn, keys, data):
    for row in data:
        row_dict = dict(zip(keys, row))
        stmt = postgresql.insert(table.table).values(**row_dict)
        upsert_stmt = stmt.on_conflict_do_update(
            index_elements=table.index, set_=row_dict
        )
        conn.execute(upsert_stmt)