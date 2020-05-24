#!/home/shiyanlou/anaconda3/bin/python
import pandas as pd

def convert(file):
    df = pd.read_json(file)
    df1 =df.head(1000)
    return df1.to_hdf('user_study.h5',key='data')

convert('users_data.json')
