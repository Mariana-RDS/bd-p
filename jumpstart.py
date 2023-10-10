import pandas as pd
import sqlite3

#create the dataframe
data = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charles', 'David']
})

data

#create database and save the dataframe
conn = sqlite3.connect('mydatabase.db')

#use the to sql method to save the  Dataframe to a table in
data.to_sql('client', conn, if_exists='replace', index=False)

#close the database connection
conn.close()