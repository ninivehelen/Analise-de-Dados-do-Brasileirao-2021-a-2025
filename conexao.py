import mysql.connector


def criar_conexao(): 
   try:
    conexao = mysql.connector.connect(
        host="localhost",  
        user="",
        password=""
    )
    print("Conexão realizada com sucesso!")
    cursor = conexao.cursor()
    cursor.execute("USE Campeonato_Brasileiro")
    return cursor

   except mysql.connector.Error as err:
    print(f"Erro Mysql: {err}")

def criar_banco_dados(cursor):
 try:
    nome_do_banco = "Campeonato_Brasileiro"
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {nome_do_banco}")
    print(f"Banco de dados '{nome_do_banco}' criado com sucesso!")

 except mysql.connector.Error as err:
    print(f"Erro ao criar banco de dados: {err}")
     
def criar_tabela_club(cursor):
    try:
        criar_tabela_clube = """
        CREATE TABLE IF NOT EXISTS Clubes (
            id_clube INT  PRIMARY KEY,
            nome VARCHAR(200),
            pais VARCHAR(200),
            imagem VARCHAR(200),
            estadio VARCHAR(200),
            valor_mercado INT,
            numero_jogadores INT,
            numero_jogadores_estrangeiros INT
        );
        """
        cursor.execute(criar_tabela_clube)
        print("Tabela clubes criada com sucesso!.")
    except mysql.connector.Error as e:
        print(f"Error creating table: {e}")

if __name__ == "__main__":
    cursor = criar_conexao()
    criar_banco_dados(cursor)
    criar_tabela_club(cursor)
