from functions.delete_rows import delete_rows

delete_rows(
    database_name = 'test.db',
    table_name = 'tabela',
    query = 'age = 24'
)

##############################################################

from functions.insert_row import insert_many_rows

insert_many_rows(
    'test.db', 'tabela',
    'id, name, age',
    [(13, "Marta", 10)]
)