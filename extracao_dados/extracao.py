import requests

anos = [2021, 2022, 2023, 2024, 2025]

def extrair_codigos_clubes_serie_a():
    lista_codigo = []
    lista_nome = []

    url = "http://localhost:8000/competitions/BRA1/clubs"

    for ano in anos:
        params = {"season_id": ano}
        response = requests.get(url, params=params, verify=False)
        if response.status_code == 200:
            dados = response.json()
            competicao = dados.get("id", "N/A")
            for clube in dados["clubs"]:
                codigo = clube.get("id", "N/A")
                nome = clube.get("name", "N/A")
                lista_codigo.append(codigo)
                lista_nome.append(nome)
                print(f" Competição: {competicao} | Código: {codigo} | Nome: {nome} | Ano: {ano}")
        else:
            print(f"Erro: {response.status_code} -> {response.text}")

    return lista_codigo


def extrair_info_club(codigos):
    codigos_sem_dupli = list(set(codigos))
    
    for club_id in codigos_sem_dupli:
        url = f'http://localhost:8000/clubs/{club_id}/profile'
        response = requests.get(url, verify=False)  
        if response.status_code == 200:
            dados = response.json()
            nome = dados.get("officialName", "N/A")
            pais_cidade = dados.get("addressLine3", "N/A")
            image = dados.get("image", "N/A")
            estadio = dados.get("stadium", "N/A")
            valor_mercado = dados.get("currentMarketValue", "N/A")

            jogadores = dados.get("squad", {})
            numero_jogadores = jogadores.get("size", 0)
            
            print(f" Clube {nome} | Local: {pais_cidade} | Estádio: {estadio} |  Número de jogadores: {numero_jogadores} | Valor de mercado: {valor_mercado} | Imagem: {image} |")
        else:
            print(f"Erro {response.status_code} para clube {club_id}")

def extrair_info_jogadores(codigos):
    codigos_sem_dupli = list(set(codigos))
    
    for club_id in codigos_sem_dupli:
        url = f'http://localhost:8000/clubs/{club_id}/players'
        response = requests.get(url, verify=False)  
        if response.status_code == 200:
            dados = response.json()
            for jogadores in dados["players"]:
                id_clube = jogadores.get("id", "N/A")
                nome = jogadores.get("name", "N/A")
                posicao = jogadores.get("position", "N/A")
                idade = jogadores.get("age", "N/A")
                nacionalidade = jogadores.get("nationality", "N/A")
                altura = jogadores.get("height", "N/A")
                pe = jogadores.get("right", "N/A")
                valor = jogadores.get("marketValue", "N/A")
            
            print(f" Id do clube: {id_clube} | Nome do jogador: {nome} | Posição: {posicao} | Idade: {idade} |  Nacionalidade: {nacionalidade} | Altura: {altura} | Se direita ou esquerda: {pe}  | Valor: {valor}")
        print(f"Erro {response.status_code} para clube {club_id}")

if __name__ == "__main__":
    clubes_codigo = extrair_codigos_clubes_serie_a()
    extrair_info_club(clubes_codigo)
    extrair_info_jogadores(clubes_codigo)
