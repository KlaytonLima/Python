import sqlite3

cidades = [('Sarandi', 'PR'), ('Cuiabá', 'MT'), ('São Paulo', 'SP')]
pessoas = [('Klayton', 'Lima', 'klaytonlenara@gmail.com', 1, 2023-03-26),
           ('Flaviano', 'Queiroz', 'klaytonlenara@gmail.com', 2, 2023-03-26),
           ('Hellyandra', 'Guesso', 'klaytonlenara@gmail.com', 3, 2023-03-26)]

#Criando a conexão com banco de dados

conn = sqlite3.connect('cadastro.db')

#Criando o cursor

cursor = conn.cursor()
cursor.executemany('''INSERT INTO cidades (cidade, uf) VALUES(?,?)''', cidades)
cursor.executemany('''INSERT INTO pessoas (nome, sobrenome, email, cidade_id, criado_em) 
                    VALUES(?,?,?,?,?)''', pessoas)
conn.commit()

#Fechando a conexão com banco de dados e cursor

cursor.close()
conn.close()
