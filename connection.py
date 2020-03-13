import psycopg2 as pg 
import pandas.io.sql as psql
import pandas as pd
# get connected to the database



def getProfessionals():
    conn = _openConnection()
    df = psql.read_sql('select * from profissionais', con=conn)
    conn.close()
    return df

def getProfessionalsCsv():
    df = pd.read_csv('profissionais.csv')
    return df