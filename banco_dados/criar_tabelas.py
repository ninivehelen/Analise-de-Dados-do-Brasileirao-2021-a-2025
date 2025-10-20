import mysql.connector

def criar_banco_dados(cursor):
 try:
    nome_do_banco = "Campeonato_Brasileiro"
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {nome_do_banco}")
    print(f"Banco de dados '{nome_do_banco}' criado com sucesso!")
    cursor.execute("USE Campeonato_Brasileiro")

 except mysql.connector.Error as err:
    print(f"Erro ao criar banco de dados: {err}")
     
def criar_tabela_club(cursor):
    try:
        criar_tabela_clube = """
        CREATE TABLE IF NOT EXISTS Clubes (
            id_clube INT  PRIMARY KEY,
            nome_clube_official VARCHAR(100),
            pais VARCHAR(100),
            imagem VARCHAR(100),
            estadio VARCHAR(200),
            valor_mercado FLOAT,
            numero_jogadores INT,
            numero_jogadores_estrangeiros INT
        );
        """
        cursor.execute(criar_tabela_clube)
        print("Tabela clubes criada com sucesso!.")
    except mysql.connector.Error as e:
        print(f"Error creating table: {e}")

def criar_tabela_competicao(cursor):
    try:
        criar_tabela_competicao = """
        CREATE TABLE IF NOT EXISTS Competicao (
            id_competicao INT  PRIMARY KEY,
            nome_competicao VARCHAR(200),
            id_clube INT,
            ano INT,
            FOREIGN KEY (id_clube) REFERENCES  Clubes(id_clube)
        );
        """
        cursor.execute(criar_tabela_competicao)
        print("Tabela competição criada com sucesso!.")
    except mysql.connector.Error as e:
        print(f"Error creating table: {e}")

def criar_tabela_jogadores(cursor):
    try:
        criar_tabela_jogadores = """
        CREATE TABLE IF NOT EXISTS Jogadores(
            id_jogador INT AUTO_INCREMENT PRIMARY KEY,
            id_clube INT,
            nome_jogador VARCHAR(200),
            posicao VARCHAR(200),
            idade INT,
            nacionalidade VARCHAR(200),
            altura VARCHAR(200),
            pe VARCHAR(200),
            valor FLOAT,
            FOREIGN KEY (id_clube) REFERENCES Clubes(id_clube)
        );
        """
        cursor.execute(criar_tabela_jogadores)
        print("Tabela jogadores criada com sucesso!.")
    except mysql.connector.Error as e:
        print(f"Error creating table: {e}")