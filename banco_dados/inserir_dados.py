import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:3623@localhost:3306/campeonato_brasileiro")

# def inserir_dados_clubes():
#     df = pd.read_csv("informacao_clubes.csv",sep=',',quotechar='\'',encoding='utf8') 
#     df.to_sql('clubes',con=engine,index=False,if_exists='append') 

def inserir_dados_competicao():
    df = pd.read_csv("informacao_competicao.csv",sep=',',quotechar='\'',encoding='utf8') 
    df.to_sql('competicao',con=engine,index=False,if_exists='append') 
   

def inserir_dados_jogadores():
    "Em construção"
    pass 

inserir_dados_competicao()