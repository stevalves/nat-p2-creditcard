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

col1, col2 = st.columns(2)
with col1:
    time_val = st.number_input("Tempo desde a primeira transação (Time)", min_value=0.0, value=0.0)
with col2:
    amount_val = st.number_input("Valor da Transação (Amount em $)", min_value=0.0, value=150.0)

st.subheader("Variáveis Vx 1~28")
st.markdown("(Não obrigatórias, mas quanto mais preenchidas, mais precisa será a predição)")

#- Gerando os 28 campos automaticamente em 4 colunas para o layout não ficar feio
with st.expander("Clique para inserir as variáveis VXs"):
    cols = st.columns(4)
    v_inputs = {}
    for i in range(1, 29):
        col_idx = (i - 1) % 4
        with cols[col_idx]:
            v_inputs[f'V{i}'] = st.number_input(f'V{i}', value=0.0, format="%.4f")

#- Executar Predição
st.markdown("---")
if st.button("Executar Predição"):
    #- Organiza os dados
    dados_entrada = {'Time': time_val}
    dados_entrada.update(v_inputs)
    dados_entrada['Amount'] = amount_val
    
    df_input = pd.DataFrame([dados_entrada])
    
    #- Garante ordem das colunas correta (Time, V1~V28, Amount)
    ordem_correta = ['Time'] + [f'V{i}' for i in range(1, 29)] + ['Amount']
    df_input = df_input[ordem_correta]
    
    #- Seta o threshold do colab, para classificar como fraude ou não 
    threshold = 0.85
    
    try:
        #- Faz a predição 
        proba_fraude = modelo.predict_proba(df_input)[0][1]
        
        #- Exibição dos Resultados
        st.header("Resultado Finais:")
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