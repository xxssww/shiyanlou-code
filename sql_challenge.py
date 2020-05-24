#!/home/shiyanlou/anaconda3/bin/python

import os
import sqlite3
import pandas as pd
import numpy as np

def count(file,user_id):
    sql_conn=sqlite3.connect(file)
    sql_id=pd.read_sql('select user_id from data where user_id = %d' % user_id,sql_conn)
    if len(sql_id)==0:
        sql_conn.close()
        print(1)
        return 0
    else:
        sum_minute= pd.read_sql('select sum(minutes) from data where user_id = %d' % user_id,sql_conn)
        sql_conn.close()
        sum_minutes = int(sum_minute.ix[0].values)
        print(sum_minutes)
        return sum_minutes
count('users_data.sqlite',8490)

