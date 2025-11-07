import pandas as pd

def anonimizar_dados(df):
    """Aplica anonimização simples aos dados."""
    df_anon = df.copy()
    df_anon['renda'] = df_anon['renda'].apply(lambda x: round(x, -2))  # Arredonda para centenas
    df_anon['idade'] = df_anon['idade'].apply(lambda x: (x // 5) * 5)  # Agrupa idades em faixas de 5 anos
    df_anon['genero'] = 'Anônimo'  # Remove distinção por gênero
    return df_anon
