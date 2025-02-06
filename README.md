# Consulta de Processos CNJ

Este projeto implementa uma aplicação web simples em Python com Flask para consultar metadados de processos judiciais utilizando a API Pública do CNJ (Conselho Nacional de Justiça) para buscas processos do TJSP.

## Funcionalidades

- Busca de processos por número.
- Exibição de todos os metadados do processo em formato tabular, incluindo informações aninhadas como movimentos, assuntos e complementos tabelados.
- Tratamento de erros para formatos inválidos de número de processo e problemas de comunicação com a API.
- Formatação amigável da data e hora dos movimentos.
- Estilização básica com Roboto font e Material Icons (integração completa com Material UI requer um framework frontend como React ou Vue.js).


## Instalação

1. **Clone o repositório:**

   ```bash
   git clone <URL_DO_REPOSITORIO>
   ```

2. **Crie um ambiente virtual (recomendado):**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # No Linux/macOS
   .venv\Scripts\activate  # No Windows
   ```

3. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```
   Certifique-se de que o arquivo `requirements.txt` contenha as seguintes dependências:
   ```
    blinker==1.9.0
    certifi==2025.1.31
    charset-normalizer==3.4.1
    click==8.1.8
    colorama==0.4.6
    Flask==3.1.0
    idna==3.10
    itsdangerous==2.2.0
    Jinja2==3.1.5
    jsonify==0.5
    MarkupSafe==3.0.2
    python-dotenv==1.0.1
    requests==2.32.3
    urllib3==2.3.0
    Werkzeug==3.1.3

   ```


4. **Configure a chave da API:**

   Adicione a API_KEY no arquivo`.env` na raiz do projeto.

   ```
   API_KEY=<CHAVE_DE_API>
   ```
   API_KEY pública Pode ser encontrada em https://datajud-wiki.cnj.jus.br/api-publica/acesso


## Execução

1. **Ative o ambiente virtual (se estiver usando um):**

   ```bash
   source .venv/bin/activate  # No Linux/macOS
   .venv\Scripts\activate  # No Windows
   ```

2. **Execute o aplicativo:**

   ```bash
   flask run
   ```

3. **Acesse a aplicação:**

   Abra o seu navegador web e acesse `http://127.0.0.1:5000/`.


## Uso

1. **Insira o número do processo**

No campo de entrada. O formato pode ser o antigo (xxxxxxxxxxxxxxx) ou o novo (xxxxxxx-xx.xxxx.x.xx.xxxx).
2. **Clique em "Buscar".**

Se o processo for encontrado, os metadados serão exibidos em uma tabela. Caso contrário, uma mensagem de erro será exibida.


## Estrutura do projeto

```
seu_projeto/
├── templates/
│   └── index.html
├── app.py
├── .env             
├── requirements.txt    
└── README.md   
```

#  Tratamento de erros

A aplicação inclui tratamento de erros para:

- **Formato inválido do número do processo:** Uma mensagem de erro será exibida se o número do processo não estiver em um formato válido.
- **Erros na requisição à API:**  Mensagens de erro mais descritivas são exibidas em caso de problemas de comunicação com a API do CNJ, incluindo `timeouts`.
- **Processo não encontrado:** Uma mensagem informando que o processo não foi encontrado é exibida.

#  Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.


#  Licença

[MIT](LICENSE) 


**Observações:**

- Se quiser buscar de outros tribunais substitua API_URL. Os endpoints pode ser encontrado em https://datajud-wiki.cnj.jus.br/api-publica/endpoints
