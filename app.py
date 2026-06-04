import streamlit as st
import pandas as pd
import numpy as np
import joblib

#- Configuração da Página
st.set_page_config(page_title="Detecção de Fraudes", page_icon="pesquisa", layout="wide")

st.title("Sistema de Detecção de Fraudes em Cartões")
st.markdown("Simulador para verificar se uma transação é Legítima ou Fraude.")

#- Carregando o Modelo
@st.cache_resource # Cache recomendado pela Streamlit
def carregar_modelo():
    return joblib.load('model/modelo_final.joblib')

modelo = carregar_modelo()

#- Entradas
st.header("Dados da Transação")

amount_val = st.number_input("Valor da Transação (Amount em $)", min_value=0.0, value=150.0)

#- Para apresentação, preferimos fazer um preenchimento automatico
st.markdown("Teste rapido:")
col_btn1, col_btn2, col_btn3 = st.columns(3)

with col_btn1:
    if st.button("Preencher Exemplo Legítimo"):
        # Injeta valores normais considerados pelo modelo.
        for i in range(1, 29):
            st.session_state[f'v{i}_input'] = 0.05

with col_btn2:
    if st.button("Preencher Exemplo de Fraude"):
        # Injeta valores anormais considerados pelo modelo.
        for i in range(1, 29):
            st.session_state[f'v{i}_input'] = -5.5 if i % 2 == 0 else 6.2

with col_btn3:
    if st.button("Limpar Dados"):
        # Zera todos os valores
        for i in range(1, 29):
            st.session_state[f'v{i}_input'] = 0.0

#- Gerando os 28 campos
st.subheader("Variáveis Vx 1~28")
st.markdown("(Não obrigatórias, mas quanto mais preenchidas, mais precisa será a predição)")
with st.expander("Clique para visualizar ou editar as variáveis VXs"):
    cols = st.columns(4)
    v_inputs = {}
    for i in range(1, 29):
        col_idx = (i - 1) % 4
        
        #- Se a variável ainda não existe na memória, cria ela valendo 0.0
        if f'v{i}_input' not in st.session_state:
            st.session_state[f'v{i}_input'] = 0.0
            
        with cols[col_idx]:
            #- O parâmetro 'key' é o que conecta o campo visual à memória do Streamlit
            v_inputs[f'V{i}'] = st.number_input(
                f'V{i}', 
                format="%.4f", 
                key=f'v{i}_input'
            )

#- Executar Predição
st.markdown("---")
if st.button("Executar Predição"):
    dados_entrada = {}
    dados_entrada.update(v_inputs)
    dados_entrada['Amount'] = amount_val
    
    df_input = pd.DataFrame([dados_entrada])
    
    ordem_correta = [f'V{i}' for i in range(1, 29)] + ['Amount']
    df_input = df_input[ordem_correta]
    
    #- Seta o threshold do colab, para classificar como fraude ou não 
    threshold = 0.85
    
    try:
        #- Faz a predição 
        proba_fraude = modelo.predict_proba(df_input)[0][1]
        
        #- Exibição dos Resultados
        st.header("Resultados Finais:")
        if proba_fraude >= threshold:
            st.error(f"* Comportamento anormal, probabilidade de fraude: {proba_fraude:.2%}")
            st.write("(Comportamento fora do comum, recomendado bloquear preventivamente e contatar o cliente)")
        else:
            st.success(f"! Comportamento normal, probabilidade de fraude: {proba_fraude:.2%}")
            st.write("(Comportamento padrão, recomendado aprovar a transação)")
            
    except Exception as e:
        proba_fraude = modelo.predict_proba(df_input.values)[0][1]
        
        #- Exibição dos Resultados
        st.header("Resultados Finais:")
        if proba_fraude >= threshold:
            st.error(f"* Comportamento anormal, probabilidade de fraude: {proba_fraude:.2%}")
            st.write("(Comportamento fora do comum, recomendado bloquear preventivamente e contatar o cliente)")
        else:
            st.success(f"! Comportamento normal, probabilidade de fraude: {proba_fraude:.2%}")
            st.write("(Comportamento padrão, recomendado aprovar a transação)")