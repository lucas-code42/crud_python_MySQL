
import mysql.connector
from mysql.connector import Error


def partition():
    print('-' * 42)
    return


print('\nBem vindo ao CRUD Python x MySQL (@localhost).')
partition()

# Show databases;
try:
    connection = mysql.connector.connect(host='localhost',
                                        database='sys',
                                        user='your_username',
                                        password='your_password')

    sql_selct_query = 'SHOW DATABASES;'
    cursor = connection.cursor()
    cursor.execute(sql_selct_query)
    records = cursor.fetchall()
    print('Banco de dados no @localhost:')

    for db in records:
        print(db)

    partition()

except mysql.connector.Error as e:
    print('Erro de conexão com MySQL', e)


choose_db = str(input('Digite em qual banco de dados deseja executar uma ação: '))

# made a connection with database that was choose for the user
try:
    connection = mysql.connector.connect(host='localhost',
                                         database=choose_db,
                                         user='your_username',
                                         password='your_password')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Conectado ao MySQL versão ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("Você está concectado ao banco de dados: ", record)

        partition()

except Error as e:
    print("Erro ao conectar com MySQL", e)


if connection.is_connected():

    choose_act = int(input("""Qual ação deseja executar?
        1. Criar uma tabela
        2. Deletar tabela
        Insira o número: """))

    if choose_act == 1:
        try:
            connection = mysql.connector.connect(host='localhost',
                                                    database=choose_db,
                                                    user='your_username',
                                                    password='your_password')

            tb_name = str(input('Nome da tabela a ser criada: '))
            mySql_Create_Table_Query = f"""CREATE TABLE {tb_name} ( 
                                        Id int(11) NOT NULL,
                                        PRIMARY KEY (Id))"""

            cursor = connection.cursor()
            result = cursor.execute(mySql_Create_Table_Query)
            print(result)
            print(f"Tabela {tb_name} criada com sucesso!")

        except mysql.connector.Error as error:
            print("Erro de conexão com MySQLFailed to create table in MySQL: {}".format(error))
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")


if choose_act == 2:
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database=choose_db,
                                            user='your_username',
                                            password='your_password')

        sql_selct_query = 'SHOW TABLES;'
        cursor = connection.cursor()
        cursor.execute(sql_selct_query)
        records = cursor.fetchall()
        print(f'Você está no banco de dados {choose_db}:')
        print('Escolha uma das tabelas abaixo para ser excluida.')
        for tb in records:
            print(tb)

        partition()

        choose_tb = str(input('Digite a tabela escolhida: '))
        sql_delete_table = f'DROP TABLE {choose_tb};'
        cursor.execute(sql_delete_table)
        print(f'Tabela {choose_tb} foi deletada com sucesso!')

    except mysql.connector.Error as e:
        print('Erro de conexão com MySQL', e)