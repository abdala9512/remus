#import mysql.connector
from sqlalchemy import create_engine
import pandas as pd
import pymysql



# https://www.youtube.com/watch?v=Ng_zi11N4_c&t=543s
sqlEngine       = create_engine('mysql+pymysql://admin:Con2020aws*@dbremus.cauel5sbqmly.us-east-1.rds.amazonaws.com/BDeholamundo', 
pool_recycle=3600)
dbConnection    = sqlEngine.connect()
frame           = pd.read_sql( "select * from baseholamundo", dbConnection)













connection = mysql.connector.connect(user = 'admin', password = "Con2020aws" ,
 host = "dbremus.cauel5sbqmly.us-east-1.rds.amazonaws.com",
 database = "BDeholamundo")

 cursor = connection.cursor()