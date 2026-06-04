# Detecção de Fraudes em Cartão de Crédito
> https://nat-p2-creditcard-auox3wiahqhaclaxi92vcr.streamlit.app

## Integrantes
* Estevão Alves dos Santos - 1990000
* Vanessa Kaori Kurauchi - 2002344

## Projeto (De acordo com o PDF com a descrição do trabalho)
* Problema: Fraudes causam bilhões em prejuízos anuais. O desafio é identificar transações fraudulentas sem bloquear transações legítimas indevidamente
* Objetivo: Desenvolver e comparar dados de transações classificação
* Dataset: Credit Card Fraud Detection (Kaggle)
> Dataset desbalanceado demais, existindo 284.315 transações legítimas e apenas 492 fraudes (0.17%)

## Metodologia e Tecnologias
* Técnicas: Pipeline com Scaler, Undersampling e StratifiedKFold, Tuning via RandomizedSearchCV (Já feito na P1)
* Modelos Testados: Logistic Regression, AdaBoost, Random Forest
* Modelo Escolhido: Random Forest (Otimizado por AUC-PR e ajuste de Threshold na Validação) -> 85% ACC! Excelente
* Tecnologias: Python, Scikit-Learn, Pandas, Streamlit

## Resultados e tratativas
Como estava muito desbalanceado, a acurácia não foi levada muito em consideração pois consideramos AUC-PR e o Recall acima dele. o threshold de 0.85 que foi definido no conjunto da validação, conseguimos maximizar a identificação de ameaças reais (Mesmo as vezes pegando algumas transações legítimas)

## Como Executar Localmente
1. Instale as dependências: `pip install -r requirements.txt`
2. Rode o app do Streamlit: `streamlit run app.py`

## Limitações
Como as variáveis V1 a V28 foram anonimizadas pelo distribuidor dos dados, ficou impossível de criar regras de negócios baseadas no dia-a-dia para facilitar o entendimento
