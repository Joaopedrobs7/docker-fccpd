import mysql.connector
from tabulate import tabulate

connection = mysql.connector.connect(
    user = 'root', password = 'root', host = 'mysql', port = '3306', database = 'db')
print('DB CONNECTED')

#itens do armazem
cursor = connection.cursor()
cursor.execute('SELECT * FROM armazem')
armazem = cursor.fetchall()
print("TABELA ITENS:")
#print(armazem)
colunas = [desc[0] for desc in cursor.description]
print(tabulate(armazem,headers= colunas,tablefmt="fancy_grid"))

#funcionarios na empresa
cursor.execute('SELECT * FROM funcionarios')
funcionarios = cursor.fetchall()
print("TABELA FUNCIONARIOS:")
#print(armazem)
colunas = [desc[0] for desc in cursor.description]
print(tabulate(funcionarios,headers= colunas,tablefmt="fancy_grid"))


#servicos
cursor.execute('SELECT * FROM servicos')
servicos = cursor.fetchall()
print("TABELA SERVICOS:")
#print(armazem)
colunas = [desc[0] for desc in cursor.description]
print(tabulate(servicos,headers= colunas,tablefmt="fancy_grid"))


#FAZER O MENU
while(1):
    print("1-VER SERVICOS\n2-CRIAR SERVICOS\n3-FINALIZAR SERVICOS\n4-FUNCIONARIO\n5-ITEMS\n6-SAIR")
    choice = int(input("Escolha: "))
    match choice:
        case 1:
            cursor.execute('SELECT * FROM servicos')
            s = cursor.fetchall()
            colunas = [desc[0] for desc in cursor.description]
            print(tabulate(s,headers= colunas,tablefmt="fancy_grid"))
        case 2:
            cliente = str(input("Nome Do cliente:"))
            descricao = str(input("Descricao do Servico:"))
            FuncionarioID = int(input("ID do funcionario:"))
            ItemID = int(input("ID do material:"))
            query = f'INSERT INTO servicos (cliente,descricao,FuncionarioID,ItemID) VALUES ("{cliente}","{descricao}",{FuncionarioID},{ItemID});'
            cursor.execute(query)
            connection.commit()
            
            # cursor.execute('SELECT * FROM servicos')
            # s = cursor.fetchall()
            # #print(s)

            #botar funcionario assignado para 1
            query = f'UPDATE funcionarios SET trabalhando = "1" WHERE ID = "{FuncionarioID}"'
            cursor.execute(query)
            connection.commit()
        case 3:
            id = int(input("ID do funcionario:"))
            #atualizar funcionario para 0
            query = f'UPDATE funcionarios SET trabalhando = "0" WHERE ID = {id};'
            cursor.execute(query)
            connection.commit()
            
            # cursor.execute('SELECT * FROM funcionarios')
            # s = cursor.fetchall()
            # print(s)

            #remover servico
            query = f'DELETE FROM servicos WHERE FuncionarioID = {id};'
            cursor.execute(query)
            connection.commit()

            # cursor.execute("SELECT * FROM servicos")
            # s = cursor.fetchall()
            # print(s)
        case 4:
            choice = int(input("1-Ver Funcionarios\n2-Adicionar Funcionario\n"))
            if (choice == 1):
                cursor.execute('SELECT * FROM funcionarios')
                s = cursor.fetchall()
                colunas = [desc[0] for desc in cursor.description]
                print(tabulate(s,headers= colunas,tablefmt="fancy_grid"))

            elif (choice == 2):
                nome_funcionario = str(input("Nome do Funcionario:"))
                query = f'INSERT INTO funcionarios (nome,trabalhando) VALUES ("{nome_funcionario}","0");'
                
                cursor.execute(query)
                connection.commit()

                cursor.execute('SELECT * FROM funcionarios')
                s = cursor.fetchall()
                # print(s)
                colunas = [desc[0] for desc in cursor.description]
                print(tabulate(s,headers= colunas,tablefmt="fancy_grid"))
        case 5:
            cursor.execute('SELECT * FROM armazem')
            s = cursor.fetchall()
            colunas = [desc[0] for desc in cursor.description]
            print(tabulate(s,headers= colunas,tablefmt="fancy_grid"))
            choice = int(input("1-Abastecer Estoque\n2-Remover Estoque\n"))
            
            if (choice == 1):
                #adicionar itens
                item = str(input("Item a ser abastecido:"))
                x = int(input("tamanho da remessa:"))
                query = f'UPDATE armazem SET estoque = estoque + {x} WHERE ItemID = {item};'
                
                cursor.execute(query)
                connection.commit()
                
                cursor.execute('SELECT * FROM armazem')
                s = cursor.fetchall()
                print(tabulate(s,headers= colunas,tablefmt="fancy_grid"))
            #remover itens
            elif (choice == 2):
                item = str(input("Item a ser removido:"))
                x = int(input("tamanho da remessa:"))
                query = f'UPDATE armazem SET estoque = estoque - {x} WHERE ItemID = {item};'
                
                cursor.execute(query)
                connection.commit()
                
                cursor.execute('SELECT * FROM armazem')
                s = cursor.fetchall()
                print(tabulate(s,headers= colunas,tablefmt="fancy_grid"))
        case 6:
            break



connection.close()