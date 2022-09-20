# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 23:05:18 2022

@author: lango
"""

import pandas as pd
import sqlalchemy

file_path = r"C:/Users/lango/desktop/code/python/telecom/mccmnc data/Book1.xlsx"
file_df = pd.read_excel(file_path, sheet_name="Sheet1", header=0)

db_username = 'root'
db_password = 'mysqltonny123!'
db_ip = 'localhost'
db_name = 'telecoms'
db_connection = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.format(db_username, db_password, db_ip, db_name))
#from sqlalchemy import types
#file_df.to_sql(con=db_connection, name='telecoms_info', if_exists='replace')
#
#dtypes = {"MCCMNC":types.VARCHAR(6), "OPERATOR":types.VARCHAR(100),"COUNTRY NAME":types.TEXT(), "MGT":types.VARCHAR(10), "NGT":types.VARCHAR(100), "TAPCODE":types.VARCHAR(6)}
(41240,
 'AREEBAAF',
 'AFGHANISTAN',
 9377,
 nan,
 True,
 False,
 True,
 True,
 True,
 False,
 93,
 'AFGAR')