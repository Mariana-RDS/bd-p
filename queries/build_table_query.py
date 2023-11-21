def build_table_query(table_name:str) -> str:
    """Build the query to retrieve the table

    Args:
        table_name(str): A table's name

    Returns:
        query(string)
    """
    query = f"""
        SELECT * 
        FROM {table_name}
    """
    return query