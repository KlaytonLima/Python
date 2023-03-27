import sqlite3

#Criando a conexão com o banco de dados

conn = sqlite3.connect('cadastro.db')

#Criando o cursor

cursor = conn.cursor()

#Criando a tabela Cidades

cursor.execute('''
CREATE TABLE IF NOT EXISTS cidades (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    cidade TEXT NOT NULL,
    );
    ''')


#Criando a tabela Pessoa

cursor.execute('''
CREATE TABLE IF NOT EXISTS pessoas (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    sobrenome TEXT NOT NULL,
    email TEXT,
    cidade_id INTEGER NOT NULL,
    criado_em TIMESTAMP,
    CONSTRAINT fk_PessoaCidade FOREIGN KEY(cidade_id) REFERENCES cidade (id)
);
''')

#Fechando a conexão com o banco de dados e cursor

cursor.close()
conn.close()

