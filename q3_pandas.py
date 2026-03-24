import pandas as pd
import numpy as np

dados_extraidos = {
    'id_processo': [101, 102, None, 104, 105],
    'valor_causa': ['R$ 1.500,00', '2000', 'R$ 350,50', '5000.00', None],
    'status': ['Ativo', 'encerrado', 'ATIVO', 'Arquivado', 'Ativo'],
    'estado': ['SP', 'RJ', 'sp', 'MG', 'SP']
}

df = pd.DataFrame(dados_extraidos)

df = df.dropna(subset=['id_processo'])

df['status'] = df['status'].str.capitalize()

def higienizar_moeda(valor):
    """Converte valores monetarios em float, preservando nulos como NaN."""
    if pd.isna(valor):
        return np.nan

    v = str(valor).replace('R$', '').strip()

    if ',' in v:
        v = v.replace('.', '')
        v = v.replace(',', '.')

    return float(v)

df['valor_causa'] = df['valor_causa'].apply(higienizar_moeda)

print("--- DataFrame Limpo ---")
print(df)
print("\n--- Tipos de Dados das Colunas ---")
print(df.dtypes)
