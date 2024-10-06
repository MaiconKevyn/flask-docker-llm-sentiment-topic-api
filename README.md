# Feedback Analysis Application

## Visão Geral
Esta é uma aplicação web construída com Flask que permite analisar feedbacks de usuários para determinar o sentimento e classificar tópicos principais dos comentários. A aplicação utiliza modelos de classificação de sentimento e classificação de tópicos da biblioteca `transformers` da Hugging Face.

## Estrutura do Projeto
O projeto possui a seguinte estrutura de diretórios:

feedback_analysis/
├── app/
│ ├── init.py
│ ├── routes.py
├── feedback_analysis_service/
│ ├── init.py
│ ├── feedback_analysis_service.py
├── templates/
│ ├── results.html
│ ├── topic_sentiment.html
├── config.py
├── run.py
├── logs/
│ ├── feedback.log
└── .gitignore


## Instalação

1. **Clone o Repositório**
    ```sh
    git clone https://github.com/seu-usuario/feedback-analysis.git
    cd feedback-analysis
    ```

2. **Crie um Ambiente Virtual**
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```

3. **Instale as Dependências**
    ```sh
    pip install -r requirements.txt
    ```

4. **Configure Variáveis de Ambiente**
    Crie um arquivo `.env` ou configure variáveis de ambiente no seu sistema:
    ```sh
    export FLASK_APP=run.py
    export FLASK_ENV=development
    ```

## Como Executar

1. **Inicie a Aplicação**
    ```sh
    flask run
    ```

2. **Acesse a Aplicação**
    Abra o navegador e vá para `http://127.0.0.1:5000`.

## Endpoints

### `/analyze` [POST]
Recebe um comentário e retorna a análise de sentimento e os tópicos principais.
- **Corpo da Requisição**:
    ```json
    {
        "comment": "Seu comentário aqui"
    }
    ```
- **Resposta**:
    ```json
    {
        "sentiment": "positive",
        "topic": ["Usability"]
    }
    ```

## Exemplo de Uso

### Analisar Comentário
Para analisar um comentário, faça uma requisição POST para `/analyze`:
```sh
curl -X POST http://127.0.0.1:5000/analyze -H "Content-Type: application/json" -d '{"comment": "This app is very helpful."}'ß
