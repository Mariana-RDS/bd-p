import sqlite3
import pandas as pd
from queries.build_table_query import build_table_query

def get_table(
        database_name:str,
        table_name:str
) -> pd.DataFrame:
    """Retrieve 

    Args:
        database_name (str): created database name
        table_name (str): table name

    Returns:
        pd.DataFrame: A dataframe from a table in database
    """

    conn = sqlite3.connect(database_name)
    query = build_table_query(table_name)

    df = pd.read_sql_query(query,conn)

    return df 