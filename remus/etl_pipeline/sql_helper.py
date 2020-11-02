"""SQL-python Helper"""


import yaml
import pandas as pd
from sqlalchemy import create_engine

class SqlHelper:
    """ Class para realizar tareas entre Python y SQL

    Cuenta con conexión, lectura y escritura de bases de datos  

    """

    def __init__(self, credentials, engine = 'MySQL'):
        self._engine = engine

        with open(credentials) as file:
            db_data = yaml.load(file)
        
        self.database_name = db_data['DBName']
        self._host         = db_data['Endpoint']
        self.__user        = db_data['user']
        self.__pass        = db_data['password']
        self.connected     = False
        self.sql_engine    = None
        self.connection    = None

    @property
    def engine(self):
        return self._engine

    def open_connection(self):

        global sql_engine, dbConnection
        if self._engine == 'MySQL':
            sql_engine = create_engine(
                'mysql+pymysql://' + self.__user + ':' + self.__pass + '@' + \
                 self._host + '/' + self.database_name, pool_recycle = 3600
            )
        dbConnection = sql_engine.connect()
        self.connected  = True
        self.sql_engine = sql_engine
        self.connection = dbConnection

    def sql_query(self, query):
        return pd.read_sql(query, dbConnection)
    
    def sql_loading(self, data, table, **kwargs):
        data.to_sql(table, **kwargs)

    def close_connection(self):
        if self.connected:
            dbConnection.close()
            self.connected = False
        else:
            raise ConnectionError('There is no open connection!')