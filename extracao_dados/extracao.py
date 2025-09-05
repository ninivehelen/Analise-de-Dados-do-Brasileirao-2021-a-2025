import requests

anos = [2021, 2022, 2023, 2024, 2025]

def extrair_codigos_info_competicao():
    print("-----------------------------------------")
    print("Extrair informações da competição anos 2021, 2022, 2023, 2024, 2025")
    lista_codigo_club = []
    lista_nome = []

    url = "http://localhost:8000/competitions/BRA1/clubs"

    for ano in anos:
        params = {"season_id": ano}
        response = requests.get(url, params=params, verify=False)
        if response.status_code == 200:
            dados = response.json()
            competicao = dados.get("id", "N/A")
            for clube in dados["clubs"]:
                codigo_club = clube.get("id", "N/A")
                nome = clube.get("name", "N/A")
                lista_codigo_club.append(codigo_club)
                lista_nome.append(nome)
                print(f" Competição: {competicao} | Id do clube: {codigo_club} | Nome: {nome} | Ano: {ano}")
        else:
            print(f"Erro: {response.status_code} -> {response.text}")

    return lista_codigo_club


def extrair_info_club(codigos_clube):
    print("-----------------------------------------")
    print("Extrair informações dos clubes")
    codigos_club_sem_dupli = list(set(codigos_clube))
    
    for club_id in codigos_club_sem_dupli:
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
            
            print(f"Id do clube {club_id}: | Clube {nome} | Local: {pais_cidade} | Estádio: {estadio} |  Número de jogadores: {numero_jogadores} | Valor de mercado: {valor_mercado} | Imagem: {image} |")
        else:
            print(f"Erro {response.status_code} para clube {club_id}")

def extrair_info_jogadores(clubes_codigos):
    print("-----------------------------------------")
    print("Extrair informações de jogadores")
    codigos_club_sem_dupli = list(set(clubes_codigos))
    
    for club_id in codigos_club_sem_dupli:
        url = f'http://localhost:8000/clubs/{club_id}/players'
        response = requests.get(url, verify=False)  
        if response.status_code == 200:
            dados = response.json()
            id_clube = dados.get("id", "N/A")
            for jogadores in dados["players"]:
                nome = jogadores.get("name", "N/A")
                posicao = jogadores.get("position", "N/A")
                idade = jogadores.get("age", "N/A")
                nacionalidade = jogadores.get("nationality", "N/A")
                altura = jogadores.get("height", "N/A")
                pe = jogadores.get("foot", "N/A")
                valor = jogadores.get("marketValue", "N/A")
                
                print(f" Id do clube: {id_clube} | Nome do jogador: {nome} | Posição: {posicao} | Idade: {idade} |  Nacionalidade: {nacionalidade} | Altura: {altura} | Se direita ou esquerda: {pe}  | Valor: {valor}")
        else:   
          print(f"Erro {response.status_code} para clube {club_id}")

if __name__ == "__main__":
    clubes_codigo = extrair_codigos_info_competicao()
    extrair_info_club(clubes_codigo)
    extrair_info_jogadores(clubes_codigo)
