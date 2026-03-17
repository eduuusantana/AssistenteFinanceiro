import json
import pandas as pd
import streamlit as st
import requests

#OLLAMA 

OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "mistral"


#IMPORTANDO OS DADOS DA BASE DE DADOS
perfil = json.load(open('./data/perfil_investidor.json'))
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')
produtos = json.load(open('./data/perfil_investidor.json'))

#CONTEXTO

contexto = f'''
    CLIENTE: {perfil['nome']}, {perfil['idade']}, {perfil['perfil_investidor']}
    OBJETIVO: {perfil['objetivo_principal']}
    PATRIMÔNIO: R$ {perfil['patrimonio_total']} | RESERVA: {perfil['reserva_emergencia_atual']}

    TRANSAÇÕES RECENTES:
    {transacoes.to_string(index=False)}

    ATENDIMENTOS ANTERIORES:
    {historico.to_string(index=False)}

    PRODUTOS DISPONÍVEIS:
    {json.dumps(produtos, indent=2, ensure_ascii=False)}
'''


#PROMPT DO SISTEMA PARA A IA

SYSTEM_PROMPT = '''Você é o Edu, um educador financeiro amigável e didático.

OBJETIVO:
Ensinar conceitos de finanças pessoais de forma simples, usando os dados do cliente como exemplos práticos.

REGRAS:
- NUNCA recomende investimentos específicos, apenas explique como funcionam;
- JAMAIS responda a perguntas fora do tema ensino de finanças pessoais. 
  Quando ocorrer, responda lembrando o seu papel de educador financeiro;
- Use os dados fornecidos para dar exemplos personalizados;
- Linguagem simples, como se explicasse para um amigo;
- Se não souber algo, admita: "Não tenho essa informação, mas posso explicar...";
- Sempre pergunte se o cliente entendeu;
- Responda de forma sucinta e direta, com no máximo 3 parágrafos.
'''

#INVOCANDO OLLAMA

def perguntar(msg):
    prompt = f'''
    {SYSTEM_PROMPT}

    CONTEXTO DO CLIENTE:
    {contexto}

    Pergunta: {msg}'''

    r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False})
    return r.json()['response']

#INTERFACE DO STREAMLIT

st.title("💰EDU, o Educador Financeiro!🪙")

if pergunta := st.chat_input("Sua dúvida sobre finanças..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_message("assistant").write(perguntar(pergunta))

