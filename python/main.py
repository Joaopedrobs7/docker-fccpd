import mysql.connector
from tabulate import tabulate

def main():
    connection = mysql.connector.connect(
        user = 'root', password = 'root', host = 'mysql', port = '3306', database = 'db')
    print('DB CONNECTED')

    cursor = connection.cursor()
    
    #itens do armazem
    printar(cursor,"armazem")

    #funcionarios na empresa
    printar(cursor,"funcionarios")
    
    #servicos
    printar(cursor,"servicos")
    
    #FAZER O MENU
    while(1):
        print("1-VER SERVICOS\n2-CRIAR SERVICOS\n3-FINALIZAR SERVICOS\n4-FUNCIONARIOS\n5-ITEMS\n6-SAIR")
        choice = int(input("Escolha: "))
        match choice:
            case 1:
                printar(cursor,"servicos")
            case 2:
                cliente = str(input("Nome Do cliente:"))
                descricao = str(input("Descricao do Servico:"))
                FuncionarioID = int(input("ID do funcionario:"))
                ItemID = int(input("ID do material:"))
                query = f'INSERT INTO servicos (cliente,descricao,FuncionarioID,ItemID) VALUES ("{cliente}","{descricao}",{FuncionarioID},{ItemID});'
                cursor.execute(query)
                connection.commit()
                

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

                #remover servico
                query = f'DELETE FROM servicos WHERE FuncionarioID = {id};'
                cursor.execute(query)
                connection.commit()
            case 4:
                choice = int(input("1-Ver Funcionarios\n2-Adicionar Funcionario\n"))
                if (choice == 1):
                    printar(cursor,"funcionarios")

                elif (choice == 2):
                    nome_funcionario = str(input("Nome do Funcionario:"))
                    query = f'INSERT INTO funcionarios (nome,trabalhando) VALUES ("{nome_funcionario}","0");'
                    
                    cursor.execute(query)
                    connection.commit()

                    printar(cursor,"funcionarios")
            case 5:
                printar(cursor,"armazem")
                choice = int(input("1-Abastecer Estoque\n2-Remover Estoque\n"))
                if (choice == 1):
                    #adicionar itens
                    item = str(input("ID do Item a ser abastecido:"))
                    x = int(input("tamanho da remessa:"))
                    query = f'UPDATE armazem SET estoque = estoque + {x} WHERE ItemID = {item};'
                    
                    cursor.execute(query)
                    connection.commit()
                    
                    printar(cursor,"armazem")
                #remover itens
                elif (choice == 2):
                    item = str(input("ID do Item a ser removido:"))
                    x = int(input("tamanho da remessa:"))
                    query = f'UPDATE armazem SET estoque = estoque - {x} WHERE ItemID = {item};'
                    
                    cursor.execute(query)
                    connection.commit()
                    
                    printar(cursor,"armazem")
            case 6:
                break

    connection.close()

def printar(cursor,tabela):
    cursor.execute(f'SELECT * FROM {tabela}')
    armazem = cursor.fetchall()
    print("TABELA ITENS:")
    #print(armazem)
    colunas = [desc[0] for desc in cursor.description]
    print(tabulate(armazem,headers= colunas,tablefmt="fancy_grid"))

main()