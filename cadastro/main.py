import mysql.connector


conexao = mysql.connector.connect(

    host="localhost",
    port="3306",
    user="root",
    password="121116",
    database="cadastro"

)

cursor = conexao.cursor()

cursor.execute('''
INSERT INTO cidades(nome_cidade, uf)
VALUES ("Sarandi", "PR"),
       ("Cuaibá", "MT"),
       ("São Paulo", "SP") ''')

cursor.execute('''
INSERT INTO pessoas(nome_pessoa, sobrenome, email, id_cidade, criado_em)
VALUES ("Klayton", "Souza Lima", "klaytonlenara@gmail.com", 1, "2023-03-27"),
       ("Hellyandra", "Guesso", "helly@gmail.com", 2, "2023-03-27"),
       ("Heloise", "Martins", "martins@gmail.com", 3, "2023-03-27"),''')

conexao.commit()

validacao = cursor.lastrowid

cursor.close()
conexao.close()

print("Cadastrado com sucesso", validacao)


