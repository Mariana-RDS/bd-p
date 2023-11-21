from functions.createtable import create_table
from functions.insert_row import insert_many_rows

create_table(
    database_name = 'tabeta2.db',
    table_name= 'nome',
    columns = """
        id_nome INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        id_idade INT
    """
)

create_table(
    database_name = 'tabela2.db',
    table_name= 'idade',
    columns = """
        id_idade INTEGER PRIMARY KEY,
        idade INTEGER NOT NULL,
        data DATE NOT NULL
    """
)

insert_many_rows(
    'tabela2.db', 'nome',
    'id_nome, nome, id_idade',
    [
        (1, "Marilia", 1),
        (2, "carla", 2),
        (3, "julia", 4),
        (4, "Mario", 7)
    ]
    
)

insert_many_rows(
    'tabela2.db', 'idade',
    'id_idade, idade', data',
    [
        (1, 24, "2008-01-06"),
        (2, 16, "2008-01-06"),
        (3, 4, "2008-01-06"),
        (4, 35, "2008-01-06"),
        (5, 7, "2008-01-06")
    ]
    
)