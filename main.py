import pandas as pd
from src.modelo import treinar_modelo, carregar_modelo_e_encoder
from src.anonimizar import anonimizar_dados
from src.testar_anonimato import testar_anonimato


# === 1. Carregar dados ===
dados = pd.read_csv('dados/clientes.csv', encoding='utf-8')
print('=== DADOS ORIGINAIS ===')
print(dados)

# === 2. Treinar o modelo ===
modelo, encoder, acuracia = treinar_modelo(dados)
print(f'\nAcurácia do modelo: {acuracia*100:.2f}%')

# === 3. Fazer previsão em novo cliente ===
novo_cliente = pd.DataFrame({'idade': [34], 'renda': [5200], 'genero': ['F']})

# Codificar o gênero com o encoder salvo
novo_cliente['genero'] = encoder.transform(novo_cliente['genero'])

predicao = modelo.predict(novo_cliente)
print(f'\nPrevisão para novo cliente: {"Compraria" if predicao[0] == 1 else "Não compraria"} a promoção.')

# === 4. Mostrar que dá pra caracterizar uma pessoa ===
print('\nO modelo consegue identificar padrões individuais como:')
print('- Pessoas com renda alta e idade média tendem a comprar.')
print('- Jovens com renda baixa tendem a não comprar.')

# === 5. Aplicar anonimização ===
print('\nAplicando anonimização estatística...')
dados_anon = anonimizar_dados(dados)
print('\n=== DADOS APÓS ANONIMIZAÇÃO ===')
print(dados_anon.head())

print('\nObservação: após a anonimização, não é possível identificar indivíduos específicos.')

# === 5. Testando anonimização ===
print('\n=== TESTANDO SE OS DADOS ESTÃO REALMENTE ANONIMIZADOS ===')
testar_anonimato(dados, dados_anon)
