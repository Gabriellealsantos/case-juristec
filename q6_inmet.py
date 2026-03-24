# q6_inmet.py

import requests
from datetime import datetime
from typing import Dict, Tuple


def obter_dados_clima(municipio: str, estado: str) -> Dict[str, Tuple[float, float]]:
    """Retorna medicoes horarias de temperatura e umidade para municipio e estado."""
    hoje = datetime.now().strftime('%Y-%m-%d')
    url_estacoes = "https://apitempo.inmet.gov.br/estacoes/T"

    try:
        resposta_estacoes = requests.get(url_estacoes, timeout=10)
        resposta_estacoes.raise_for_status()
        estacoes = resposta_estacoes.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar API de estacoes: {e}")
        return {}

    codigo_estacao = None
    nome_oficial_estacao = ""

    for estacao in estacoes:
        nome_api = estacao.get('DC_NOME', '').upper()
        if (municipio.upper() in nome_api and
            estacao.get('SG_ESTADO', '').upper() == estado.upper()):
            codigo_estacao = estacao.get('CD_ESTACAO')
            nome_oficial_estacao = nome_api
            break

    if not codigo_estacao:
        print(f"[-] Estacao meteorologica nao encontrada para {municipio} - {estado}.")
        return {}

    print(f"[+] Estacao encontrada: {nome_oficial_estacao} (Codigo: {codigo_estacao})")

    url_dados = f"https://apitempo.inmet.gov.br/estacao/dados/{hoje}/{hoje}/{codigo_estacao}"

    try:
        resposta_dados = requests.get(url_dados, timeout=10)
        resposta_dados.raise_for_status()
        dados_clima = resposta_dados.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar API de dados climaticos: {e}")
        return {}

    if not dados_clima or (isinstance(dados_clima, dict) and 'Status' in dados_clima):
        print("[-] A API nao retornou medicoes para esta estacao no dia de hoje (possivel indisponibilidade do INMET).")
        return {}

    resultado = {}
    for medicao in dados_clima:
        hora_raw = medicao.get('HR_MEDICAO')
        temp = medicao.get('TEM_INS')
        umid = medicao.get('UMD_INS')

        if hora_raw is not None and temp is not None and umid is not None:
            hora_formatada = f"{hora_raw[:2]}:{hora_raw[2:]}"
            resultado[hora_formatada] = (float(temp), float(umid))

    return resultado


if __name__ == "__main__":
    print("Buscando dados no INMET...\n")
    dados = obter_dados_clima("Belo Horizonte", "MG")

    if dados:
        print("\n--- Dados Coletados com Sucesso ---")
        for hora, (temperatura, umidade) in dados.items():
            print(f"Hora: {hora} | Temp: {temperatura} C | Umid: {umidade}%")
    else:
        print("\nNenhum dado valido para exibicao.")
