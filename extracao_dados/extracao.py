import requests
import pandas as pd 


anos = [2015, 2016, 2017, 2018,2019, 2020, 2021, 2022, 2023, 2024, 2025]

def extrair_codigos_info_competicao():
    print("-----------------------------------------")
    print("Extraindo informações das competições (anos 2015–2025)...")

    lista_codigo_club = []
    informacao_competicao = []

    url = "http://localhost:8000/competitions/BRA1/clubs"

    for ano in anos:
        params = {"season_id": ano}
        response = requests.get(url, params=params, verify=False)

        if response.status_code == 200:
            dados = response.json()
            competicao = dados.get("id", "N/A")

            for clube in dados["clubs"]:
                registro = {
                    'competicao': competicao,
                    'club_id': clube.get("id", "N/A"),
                    'ano': ano
                }
                informacao_competicao.append(registro)
                lista_codigo_club.append(clube.get("id", "N/A"))  
        else:
            print(f"Erro: {response.status_code} -> {response.text}")

 
    df = pd.DataFrame(informacao_competicao)
    df.to_csv('informacao_competicao.csv', index=False)
    print("Dados de competições salvos: 'informacao_competicao.csv'")
    return lista_codigo_club


def extrair_info_club(codigos_clube):
    print("-----------------------------------------")
    print("Extraindo informações dos clubes...")
    informacao_clube = []

    codigos_club_sem_dupli = list(set(codigos_clube))

    for club_id in codigos_club_sem_dupli:
        url = f'http://localhost:8000/clubs/{club_id}/profile'
        response = requests.get(url, verify=False)

        if response.status_code == 200:
            dados = response.json()
            registro = {
                'id_clube': club_id,
                'nome official': dados.get("officialName", "N/A"),
                'pais': dados.get("addressLine3", "N/A"),
                'imagem': dados.get("image", "N/A"),
                'estadio': dados.get("stadium", "N/A"),
                'valor_mercado': dados.get("currentMarketValue", "N/A"),
                'numero_jogadores': dados.get("squad", {}).get("size", 0),
                'numero_jogadores_estrangeiros': dados.get("squad", {}).get("foreigners", 0)
            }
            informacao_clube.append(registro)
        else:
            print(f"Erro {response.status_code} para clube {club_id}")


    salvar_dados(informacao_clube, 'informacao_clubes')


def extrair_info_jogadores(clubes_codigos):
    print("-----------------------------------------")
    print("Extraindo informações dos jogadores...")
    codigos_club_sem_dupli = list(set(clubes_codigos))
    todos_jogadores = []

    for club_id in codigos_club_sem_dupli:
        url = f'http://localhost:8000/clubs/{club_id}/players'
        response = requests.get(url, verify=False)

        if response.status_code == 200:
            dados = response.json()
            for jogador in dados["players"]:
                registro = {
                    'id_clube': dados.get("id", "N/A"),
                    'nome': jogador.get("name", "N/A"),
                    'posicao': jogador.get("position", "N/A"),
                    'idade': jogador.get("age", "N/A"),
                    'nacionalidade': jogador.get("nationality", "N/A"),
                    'altura': jogador.get("height", "N/A"),
                    'pe': jogador.get("foot", "N/A"),
                    'valor': jogador.get("marketValue", "N/A")
                }
                todos_jogadores.append(registro)
        else:
            print(f"Erro {response.status_code} para clube {club_id}")

    salvar_dados(todos_jogadores, 'informacao_jogadores')


def salvar_dados(arquivo, nome_arquivo):
    df = pd.DataFrame(arquivo)
    df.to_csv(f'{nome_arquivo}.csv', index=False)
    print(f"Dados sobre '{nome_arquivo}' salvos: {nome_arquivo}.csv")
    print(df.head()) 


if __name__ == "__main__":
    clubes_codigo = extrair_codigos_info_competicao()
    extrair_info_club(clubes_codigo)
    extrair_info_jogadores(clubes_codigo)
