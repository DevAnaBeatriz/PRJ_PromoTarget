import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import pickle
import os

# Caminhos para salvar o modelo e o encoder
MODELO_PATH = 'modelo_treinado.pkl'
ENCODER_PATH = 'encoder_genero.pkl'

def treinar_modelo(dados):
    """Treina o modelo e salva o encoder para uso posterior."""
    dados = dados.copy()
    encoder = LabelEncoder()
    dados['genero'] = encoder.fit_transform(dados['genero'])

    X = dados[['idade', 'renda', 'genero']]
    y = dados['comprou']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    modelo = RandomForestClassifier(random_state=42)
    modelo.fit(X_train, y_train)

    acuracia = modelo.score(X_test, y_test)

    # Salvar modelo e encoder
    with open(MODELO_PATH, 'wb') as f:
        pickle.dump(modelo, f)
    with open(ENCODER_PATH, 'wb') as f:
        pickle.dump(encoder, f)

    return modelo, encoder, acuracia


def carregar_modelo_e_encoder():
    """Carrega o modelo e o encoder já treinados, se existirem."""
    if os.path.exists(MODELO_PATH) and os.path.exists(ENCODER_PATH):
        with open(MODELO_PATH, 'rb') as f:
            modelo = pickle.load(f)
        with open(ENCODER_PATH, 'rb') as f:
            encoder = pickle.load(f)
        return modelo, encoder
    else:
        raise FileNotFoundError("Modelo ou encoder não encontrados. Execute o treinamento primeiro.")
