# Projeto: PromoTarget 

## Descrição
Este projeto demonstra como é possível usar **Machine Learning** para direcionar promoções a pessoas com base em dados simples (idade, renda e gênero) e, em seguida, aplicar técnicas estatísticas para **anonimização**, garantindo que não seja possível identificar indivíduos específicos.

O objetivo é mostrar **duas etapas complementares**:
1. **Predição e caracterização de perfis de consumo** — o modelo consegue identificar tendências (ex: pessoas com renda alta têm maior probabilidade de comprar uma promoção).
2. **Anonimização de dados pessoais** — após o uso para fins analíticos, os dados passam por um processo de anonimização (agrupamento de idades e ruído estatístico na renda), o que impede a identificação de uma pessoa individualmente.

---

## Conceitos principais
- **Direcionar uma compra:** prever, com base nos dados, quem tem maior probabilidade de aceitar uma promoção.
- **Caracterizar uma pessoa:** o modelo aprende padrões que distinguem grupos (ex: idade e renda influenciam a decisão).
- **Anonimização estatística:** técnica para evitar reidentificação (com ruído e agrupamento).

---

## Estrutura do Projeto
```
promo_target_pt/
│
├── dados/
│   └── clientes.csv            # Dados de exemplo
│
├── src/
│   ├── modelo.py               # Treinamento do modelo de ML
│   ├── anonimizar.py           # Funções de anonimização
│   └──testar_anonimato
├── main.py                 # Execução principal
│
├── requirements.txt
└── README.txt
```

---

## Execução
1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
2. Execute o projeto:
   ```bash
   python main.py
   ```

---

## Saída esperada
O terminal exibirá:
- Os dados originais;
- A acurácia do modelo;
- A previsão para um novo cliente;
- A demonstração de que o modelo caracteriza perfis;
- Os dados anonimizados (sem identificação individual).

---

## Resultado resumido
- O modelo de **Machine Learning** identifica padrões úteis para marketing direcionado.  
- Após a **anonimização estatística**, é impossível rastrear uma pessoa específica.  
Assim, o projeto mostra o equilíbrio entre **utilização inteligente de dados** e **proteção da privacidade**.
