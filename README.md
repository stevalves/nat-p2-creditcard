# Detecção de Fraudes em Cartão de Crédito
> Deploy [StreamLit](https://nat-p2-creditcard-auox3wiahqhaclaxi92vcr.streamlit.app)

## Integrantes
* Estevão Alves dos Santos - 1990000
* Vanessa Kaori Kurauchi - 2002344

## Projeto (De acordo com o PDF com a descrição do trabalho)
* Problema: Fraudes causam bilhões em prejuízos anuais. O desafio é identificar transações fraudulentas sem bloquear transações legítimas indevidamente
* Objetivo: Desenvolver e comparar dados de transações
* Dataset: Credit Card Fraud Detection (Kaggle)
> Dataset desbalanceado demais, existindo 284.315 transações legítimas e apenas 492 fraudes (0.17%)

## Metodologia e Tecnologias
* Técnicas: Pipeline com Scaler, Undersampling e StratifiedKFold, Tuning via RandomizedSearchCV (Já feito na P1)
* Modelos Testados: Logistic Regression, AdaBoost, Random Forest
* Modelo Escolhido: Random Forest (Otimizado por AUC-PR e ajuste de Threshold na Validação) -> 85% ACC! Excelente
* Tecnologias: Python, Scikit-Learn, Pandas, Streamlit

## Resultados e tratativas
Como estava muito desbalanceado, a acurácia não foi levada muito em consideração pois consideramos AUC-PR e o Recall acima dele. o threshold de 0.85 que foi definido no conjunto da validação, conseguimos maximizar a identificação de ameaças reais (Mesmo as vezes pegando algumas transações legítimas)

## Como Executar (Repositório)
1. Instale as dependências: `pip install -r requirements.txt`
2. Rode o app do Streamlit: `streamlit run app.py`

## Como Executar (StreamLit)
1. Acessar o link: `StreamLit` abaixo
2. Testar utilizando os botões pre-configurados ou inserir os dados manualmente

## Como Executar (Colab)
1. Acessar o link: `Colab` abaixo
2. Baixar o dataset no [Kaggle](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
3. Colocar no mesmo ambiente de execução do colab
4. Rodar

## Links
- [StreamLit](https://nat-p2-creditcard-auox3wiahqhaclaxi92vcr.streamlit.app)
- [Colab](https://colab.research.google.com/drive/1URMTpv8Sb_oknIUczE0mYJ_qXQ38z_Yv?usp=sharing)

## Limitações
Como as variáveis V1 a V28 foram anonimizadas pelo distribuidor dos dados, ficou impossível de criar regras de negócios baseadas no dia-a-dia para facilitar o entendimento

## Conclusão final
<p>
Apesar da dificuldade em entender os padrões, fizemos decisões que auxiliaram na capacitação do modelo utilizado que foi remover alguns campos que não contribuiram ativamente para o aumento da acuracia.
</p>
<p>
Além de removermos esses dados, fizemos alguns testes com cargas diferentes mesmo normalizando a quantidade utilizando undersampling com diferentes valores de testes e confirmando a baixa alternancia entre a acc final.
</p>
<p>
No final, após testes medindo os modelos citados anteriormente, decidimos ficar com o Random Forest que foi o modelo de melhor resultado (resultados disponíveis na <a href="https://nat-p2-creditcard-auox3wiahqhaclaxi92vcr.streamlit.app">StreamLit</a>.
</p>
<p>
Pelos dados estarem anonimizados, é difícil definirmos um padrão visível entre as variáveis, então foram tentativas sempre medindo os resultados e definindo se está agindo de acordo com o esperado.
</p>
