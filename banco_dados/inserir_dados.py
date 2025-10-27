import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:3623@localhost:3306/campeonato_brasileiro")

def inserir_dados_clubes():
    df = pd.read_csv("informacao_clubes.csv",sep=',',quotechar='\'',encoding='utf8') 
    df.to_sql('clubes',con=engine,index=False, if_exists='append') 
    print("Dados de clubes enviados com sucesso !")

def inserir_dados_competicao():
    df = pd.read_csv("informacao_competicao.csv",sep=',',quotechar='\'',encoding='utf8') 
    df.to_sql('competicao',con=engine,index=False,if_exists='append') 
    print("Dados de competição enviados com sucesso !")
   

def inserir_dados_jogadores():
    df = pd.read_csv("informacao_jogadores.csv",sep=',',quotechar='\'',encoding='utf8') 
    df.to_sql('jogadores',con=engine,index=False,if_exists='append')
    print("Dados de jogadores enviados com sucesso !") 

if __name__ == "__main__":
   inserir_dados_clubes()
   inserir_dados_competicao()
   inserir_dados_jogadores()