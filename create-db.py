import sqlite3

# Conectar ao banco de dados (criará um novo arquivo se não existir)
conn = sqlite3.connect('data.db', check_same_thread=False)
cursor = conn.cursor()

# Script para criar a tabela temperatura
create_table_query = '''
    CREATE TABLE IF NOT EXISTS temperatura (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        temperatura REAL,
        timestamp DATETIME
    );
'''

cursor.execute(create_table_query)
conn.commit()

# Fechar a conexão com o banco de dados
conn.close()


