import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from scipy.stats import pearsonr

def testar_anonimato(dados_originais, dados_anonimizados):
    print("\n=== TESTE DE ANONIMATO ===")

    # 1. Adicionar um ID aos dados originais
    dados_originais = dados_originais.copy()
    dados_originais["id_pessoa"] = range(len(dados_originais))

    # 2. Criar cópias para teste
    orig = dados_originais[["idade", "renda", "genero"]].copy()
    anon = dados_anonimizados[["idade", "renda", "genero"]].copy()

    # 3. Codificar gênero (corrigido para lidar com "Anônimo")
    encoder = LabelEncoder()
    todos_generos = pd.concat([orig["genero"], anon["genero"]], ignore_index=True)
    encoder.fit(todos_generos)

    orig["genero"] = encoder.transform(orig["genero"])
    anon["genero"] = encoder.transform(anon["genero"])

    # 4. Calcular correlação média entre dados originais e anonimizados
    correlacoes = []
    for col in ["idade", "renda", "genero"]:
        try:
            corr, _ = pearsonr(orig[col], anon[col])
            correlacoes.append(corr)
        except Exception:
            correlacoes.append(0)
    media_corr = np.mean(correlacoes)

    print(f"\nCorrelação média entre dados originais e anonimizados: {media_corr:.3f}")
    if media_corr < 0.3:
        print("✅ Baixa correlação: os dados foram bem anonimizados.")
    else:
        print("⚠️ Correlação alta: ainda há semelhança entre os dados.")

    # 5. Teste de reidentificação com Machine Learning
    X_train, X_test, y_train, y_test = train_test_split(
        anon, dados_originais["id_pessoa"], test_size=0.3, random_state=42
    )

    modelo = RandomForestClassifier(random_state=42)
    modelo.fit(X_train, y_train)
    acuracia = modelo.score(X_test, y_test)

    print(f"\nAcurácia tentando reidentificar pessoas: {acuracia*100:.2f}%")
    if acuracia < 20:
        print("✅ Excelente: o modelo não consegue reidentificar pessoas (dados anônimos).")
    else:
        print("⚠️ Acurácia ainda alta: pode haver risco de reidentificação.")

    # 6. Comparar estatísticas descritivas
    print("\n=== Comparação Estatística ===")
    print("Originais:")
    print(orig.describe())
    print("\nAnonimizados:")
    print(anon.describe())

    print("\nInterpretação:")
    print("- Se médias e desvios-padrão mudaram, houve transformação real.")
    print("- O ideal é que a estrutura geral se mantenha (tendência estatística), mas sem manter vínculos individuais.")
