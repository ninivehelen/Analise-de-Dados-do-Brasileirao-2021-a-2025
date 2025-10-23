import mysql.connector
from criar_tabelas import * 

def criar_conexao(): 
   try:
    conexao = mysql.connector.connect(
        host="localhost",  
        user="root",
        password="3623"
    )
    print("Conexão realizada com sucesso!")
    cursor = conexao.cursor()
    return cursor

   except mysql.connector.Error as err:
    print(f"Erro Mysql: {err}")

if __name__ == "__main__":
    cursor = criar_conexao()
    criar_banco_dados(cursor)
    #criar_tabela_club(cursor)
    criar_tabela_competicao(cursor)
    #criar_tabela_jogadores(cursor)
