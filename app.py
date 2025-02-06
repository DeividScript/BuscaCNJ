from flask import Flask, render_template, request
import json
import requests
import re
import os
from dotenv import load_dotenv

app = Flask(__name__)

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()
API_KEY = os.getenv("API_KEY")
API_URL = "https://api-publica.datajud.cnj.jus.br/api_publica_tjsp/_search"

# Verifica se a chave da API foi carregada corretamente
if not API_KEY:
    raise ValueError("API_KEY não encontrada. Verifique se o arquivo .env está configurado corretamente.")

print("API_KEY carregada com sucesso.")  # Confirmação de carregamento da chave (oculte esta informação em produção!)

# Filtro de template para verificar se um objeto é um dicionário
@app.template_filter('is_dict')
def is_dict_filter(obj):
    return isinstance(obj, dict)

# Rota principal da aplicação
@app.route("/", methods=["GET", "POST"])
def index():
    processo_data = None
    mensagem_erro = None

    if request.method == "POST":
        numero_processo = request.form.get("numero_processo")
        if numero_processo:
            # Formata o número do processo antes de buscar
            numero_processo_formatado = formatar_numero_processo(numero_processo)
            if numero_processo_formatado:
                processo_data = buscar_processo(numero_processo_formatado)
                if isinstance(processo_data, str):
                    mensagem_erro = processo_data
                    processo_data = None
            else:
                mensagem_erro = "Formato de número de processo inválido."

    return render_template("index.html", processo=processo_data, mensagem_erro=mensagem_erro, is_dict=is_dict_filter)

# Função para formatar o número do processo
def formatar_numero_processo(numero_processo):
    """Formata o número do processo, aceitando o novo e o antigo formato."""

    padrao_novo = r"(\d{7})-(\d{2})\.(\d{4})\.(\d)\.(\d{2})\.(\d{4})"
    match_novo = re.match(padrao_novo, numero_processo)

    if match_novo:
        return "".join(match_novo.groups())  # Concatena todos os grupos

    padrao_antigo = r"(\d{13})(\d{7})"  # Aceita o formato antigo também
    match_antigo = re.match(padrao_antigo, numero_processo)
    
    if match_antigo:
        return "".join(match_antigo.groups())

    return None  # Retorna None se nenhum dos padrões corresponder

# Função para buscar o processo na API
def buscar_processo(numero_processo):
    payload = json.dumps({
        "query": {
            "match": {
                "numeroProcesso": numero_processo
            }
        }
    })
    headers = {
        'Authorization': f'ApiKey {API_KEY}',
        'Content-Type': 'application/json'
    }

    try:
        response = requests.request("POST", API_URL, headers=headers, data=payload, timeout=50)
        response.raise_for_status()
        data = response.json()

        if data['hits']['total']['value'] > 0:
            return data['hits']['hits'][0]['_source']
        else:
            return "Processo não encontrado"
    except requests.exceptions.RequestException as e:
        return f"Erro na requisição à API: {e}"

# Executa a aplicação Flask
if __name__ == "__main__":
    app.run(debug=True)