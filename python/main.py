import mysql.connector

connection = mysql.connector.connect(
    user = 'root', password = 'root', host = 'mysql', port = '3306', database = 'db')
print('DB CONNECTED')

#itens do armazem
cursor = connection.cursor()
cursor.execute('SELECT * FROM armazem')
armazem = cursor.fetchall()

#funcionarios na empresa
cursor.execute('SELECT * FROM funcionarios')
funcionarios = cursor.fetchall()


#servicos
cursor.execute('SELECT * FROM servicos')
servicos = cursor.fetchall()

connection.close()
print(armazem)
print(funcionarios)
print(servicos)
