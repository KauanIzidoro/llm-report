# Configurações iniciais

### Preparar o ambiente para desenvolver o agente

- Clonar e navegar até a pasta do projeto

- Instalar a bibliotecas necessárias a partir de um arquivo **requirements** ou **poetry**:

### Quais Bibliotecas Podemos Usar?

**Manipulação de Código:**
- Python: `ast`, `jedi`, `rope`.
- JavaScript: `esprima`, `babel-parser`.

**Criação de Diagramas:**
  - `Graphviz`.
  - `PlantUML`.
  - `ERAlchemy`

**Integração com LLMs:**
  - OpenAI: `openai` (Python SDK).
  - Hugging Face: `transformers`.
  - LangChain: Biblioteca para orquestrar interações com LLMs.

**Processamento de dados:**

- ``pandas`` (para estruturar dados de entrada/saída).
- ``json`` (para manipulação de inputs e outputs).

# Escolha e Configuração do Modelo LLM

## O que é necessário para criar o agente?

### Estrutura do pipeline:

1. Receber input.
    - Strings textuais ou JSON básico.
    - Exemplo: "Desenhe um fluxograma básico."
2. Processar dados com o LLM.
   - Focar em Python como linguagem principal, dada a disponibilidade de bibliotecas robustas para NLP e LLMs.
3. Post-processar output para adequar ao formato esperado.
    - Resposta processada: O código segue esse fluxo A > B > C
    - Resposta mockada: JSON representando os elementos do fluxograma.

### Quais Opções Temos de LLMs?

**Baseados em APIs**
- OpenAI GPT (e.g., GPT-4).
- Cohere.

**Modelos open-source**
- Hugging Face Transformers (e.g., BERT, GPT-NeoX).
- LangChain com Llama2.