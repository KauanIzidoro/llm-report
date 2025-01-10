
# Parte da Task
```
Focar na parte do desenvolvimento do agente
O que preciso para criar o agente
Quais opções temos de LLMs
Quais bibliotecas podemos usar
```

## Foco na Parte do Desenvolvimento do Agente
### O que é necessário para criar o agente?
1. Estrutura do pipeline:
- Receber input.
- Processar dados com o LLM.
- Post-processar output para adequar ao formato esperado.
- Integração com o LLM escolhido.
- Testes com casos de uso mockados.

## Quais Bibliotecas Podemos Usar?
### Para interação com LLMs:

- openai (para modelos GPT).
- transformers (Hugging Face).
- langchain (para pipelines e fluxos).

### Para processamento de dados:

- pandas (para estruturar dados de entrada/saída).
- json (para manipulação de inputs e outputs).

### Para testes:

- unittest ou pytest (testes automatizados).

## Quais Opções Temos de LLMs?
### Baseados em APIs

- OpenAI GPT (e.g., GPT-4).
- Cohere.

### Modelos open-source

- Hugging Face Transformers (e.g., BERT, GPT-NeoX).
- LangChain com Llama2.