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


print("TABELA ITENS:")
print(armazem)
print("TABELA FUNCIONARIOS:")
print(funcionarios)
print("TABELA SERVICOS:")
print(servicos)


#FAZER O MENU
print("1-VER SERVICOS\n2-CRIAR SERVICOS\n3-FINALIZAR SERVICOS\n4-ADICIONAR FUNCIONARIO\n5-ITEMS")
choice = int(input("Escolha: "))
match choice:
    case 1:
        cursor.execute('SELECT * FROM servicos')
        s = cursor.fetchall()
        print(s)
    case 2:
        nome = str(input("Nome Do cliente:"))
        descricao = str(input("Descricao do Servico:"))
        funcionario = str(input("Funcionario Responsavel:"))
        query = f'INSERT INTO servicos (cliente,descricao,nome) VALUES ("{nome}","{descricao}","{funcionario}");'
        
        
        cursor.execute(query)
        connection.commit()
        
        cursor.execute('SELECT * FROM servicos')
        s = cursor.fetchall()
        print(s)

        #botar funcionario assignado para 1
    case 3:
        nome = str(input("Nome pra remover:"))
        #atualizar funcionario para 0
        query = f'UPDATE funcionarios SET trabalhando = "0" WHERE nome = "{nome}";'
        cursor.execute(query)
        connection.commit()
        
        cursor.execute('SELECT * FROM funcionarios')
        s = cursor.fetchall()
        print(s)

        #remover servico
        query = f'DELETE FROM servicos WHERE nome = "{nome}";'
        cursor.execute(query)
        connection.commit()

        cursor.execute("SELECT * FROM servicos")
        s = cursor.fetchall()
        print(s)
    case 4:
        nome_funcionario = str(input("Nome do Funcionario:"))
        query = f'INSERT INTO funcionarios (nome,trabalhando) VALUES ("{nome_funcionario}","0");'
        
        cursor.execute(query)
        connection.commit()

        cursor.execute('SELECT * FROM funcionarios')
        s = cursor.fetchall()
        print(s)
    case 5:
        choice = int(input("1-Abastecer Estoque\n2-Remover Estoque\n"))
        
        if (choice == 1):
            #adicionar itens
            item = str(input("Item a ser abastecido:"))
            x = int(input("tamanho da remessa:"))
            query = f'UPDATE armazem SET estoque = estoque + {x} WHERE Item = "{item}";'
            
            cursor.execute(query)
            connection.commit()
            
            cursor.execute('SELECT * FROM armazem')
            s = cursor.fetchall()
            print(s)
        #remover itens
        elif (choice == 2):
            item = str(input("Item a ser removido:"))
            x = int(input("tamanho da remessa:"))
            query = f'UPDATE armazem SET estoque = estoque - {x} WHERE Item = "{item}";'
            
            cursor.execute(query)
            connection.commit()
            
            cursor.execute('SELECT * FROM armazem')
            s = cursor.fetchall()
            print(s)



connection.close()