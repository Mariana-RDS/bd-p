from functions.delete_rows import delete_rows

delete_rows(
    database_name = 'test.db',
    table_name = 'tabela',
    query = 'age = 24'
)