# AssistenteFinanceiro
💰 EDU – Assistente Educador Financeiro com IA

O EDU é um assistente de educação financeira desenvolvido com Python + Streamlit + Ollama + LLM local, que utiliza dados do cliente para explicar conceitos financeiros de forma personalizada e didática.

O sistema não recomenda investimentos, apenas ensina conceitos, simulando um educador financeiro.

🚀 Tecnologias utilizadas

Python

Pandas

Streamlit

Requests

Ollama (LLM local)

Modelo Mistral

JSON / CSV

📂 Estrutura do projeto
Projeto Assistente Financeiro
│
├── src
│   └── app.py
│
├── data
│   ├── perfil_investidor.json
│   ├── transacoes.csv
│   ├── historico_atendimento.csv
│
├── README.md
⚙️ Passo a passo para rodar o projeto
1️⃣ Instalar Python

Baixe em:

https://www.python.org/downloads/

Durante a instalação marque:

Add Python to PATH

Verificar:

python --version
2️⃣ Criar ambiente virtual (recomendado)
python -m venv .venv

Ativar:

Windows:

.venv\Scripts\activate

Linux / Mac:

source .venv/bin/activate
3️⃣ Instalar dependências
pip install streamlit pandas requests

Opcional:

pip install ollama
4️⃣ Instalar o Ollama

Baixar:

https://ollama.com/download

Instalar normalmente.

Testar:

ollama --version
5️⃣ Baixar o modelo de IA

Este projeto usa o modelo mistral.

ollama pull mistral

Outros modelos possíveis:

ollama pull llama3:8b
ollama pull phi3
6️⃣ Iniciar o Ollama

O Ollama deve estar rodando em:

http://localhost:11434

Teste:

ollama run mistral

Se responder, está OK.

7️⃣ Rodar o Streamlit

Na pasta do projeto:

streamlit run src/app.py

ou (recomendado)

python -m streamlit run src/app.py
💡 Como funciona

O sistema:

Lê dados do cliente

Monta um contexto

Envia para o Ollama

O modelo responde como educador financeiro

O Streamlit mostra no chat

Arquivos usados:

perfil_investidor.json

transacoes.csv

historico_atendimento.csv

🧠 Prompt da IA

A IA segue regras:

Apenas educação financeira

Sem recomendações de investimento

Linguagem simples

Usa dados do cliente

Respostas curtas

💰 Exemplo de uso

Pergunta:

Como funciona renda fixa?

Resposta:

Renda fixa é um tipo de investimento onde você sabe
como o dinheiro vai render.

No seu caso, como você tem perfil moderado...
⚠️ Observações

O Ollama deve estar rodando

O modelo deve estar baixado

O caminho dos arquivos deve estar correto

O Streamlit deve estar instalado
