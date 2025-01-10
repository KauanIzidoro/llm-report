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

## Configurar acesso à API:  
   - Crie uma conta em [OpenAI](https://platform.openai.com/signup).  
   - Obtenha uma chave de API.  
   - Adicione a chave ao código:  
     ```python
     import openai

     openai.api_key = "SUA_CHAVE_API"

     def ask_gpt(prompt):
         response = openai.Completion.create(
             engine="text-davinci-003",
             prompt=prompt,
             max_tokens=150
         )
         return response.choices[0].text.strip()
     ```  

**Testar a integração**:  
   - Execute o seguinte código de teste:  
     ```python
     print(ask_gpt("Explique o que é uma POC."))
     ```  

---

### Desenvolvimento do Agente

### **Passo a passo**  
1. **Receber input**:  
   - Defina uma função para receber perguntas:  
     ```python
     def process_input(user_input):
         return user_input.strip()
     ```  

2. **Processar com LLM**:  
   - Use a função `ask_gpt` definida no passo anterior.  

3. **Post-processar output**:  
   - Adapte o formato da resposta, se necessário:  
     ```python
     def process_output(raw_response):
         return {"response": raw_response}
     ```  

4. **Pipeline do agente**:  
   - Integração:  
     ```python
     def agent_pipeline(input_text):
         cleaned_input = process_input(input_text)
         raw_response = ask_gpt(cleaned_input)
         return process_output(raw_response)
     ```  

5. **Teste básico**:  
   - Teste no terminal:  
     ```python
     print(agent_pipeline("Quais são os passos para criar uma POC?"))
     ```  

---

## Mock de Cenários de Uso

### **Passo a passo**  
1. **Definir perguntas mockadas**:  
   - Crie um arquivo `src/mock_data.json`:  
     ```json
     {
       "questions": [
         "O que é uma POC?",
         "Quais linguagens devo usar para uma POC?",
         "Como integrar um LLM com Python?"
       ],
       "expected_responses": [
         "Uma POC é uma prova de conceito.",
         "Use Python para LLMs.",
         "Use a biblioteca OpenAI para integrar LLMs com Python."
       ]
     }
     ```  

2. **Adicionar suporte ao mock**:  
   - Importe os mocks e teste se os resultados são semelhantes:  
     ```python
     import json

     with open("src/mock_data.json") as f:
         mock_data = json.load(f)

     for question in mock_data["questions"]:
         print(agent_pipeline(question))
     ```  


## **Configuração do Ambiente para uma LLM Aberta**
### **1. Preparar o Ambiente**

**Instale as dependências necessárias**:  
   - Instale o Hugging Face Transformers e PyTorch:  
     ```bash
     pip install transformers torch
     ```

---

### **2. Escolha e Download do Modelo**
1. **Selecione o modelo de LLM**:  
   - Para simplicidade, use um modelo pequeno, como `distilgpt2`.  

2. **Carregue o modelo no código**:  
   - Crie um arquivo chamado `src/agent.py` com o seguinte conteúdo:  
     ```python
     from transformers import AutoModelForCausalLM, AutoTokenizer

     # Carregar o modelo e o tokenizer
     def load_model():
         model_name = "distilgpt2"  # Modelo leve e simples
         tokenizer = AutoTokenizer.from_pretrained(model_name)
         model = AutoModelForCausalLM.from_pretrained(model_name)
         return model, tokenizer

     model, tokenizer = load_model()
     ```

### **3. Configurar o Pipeline de Respostas**
1. **Criar uma função para gerar respostas**:  
   - No mesmo arquivo `src/agent.py`, adicione:  
     ```python
     def generate_response(prompt, max_length=50):
         inputs = tokenizer(prompt, return_tensors="pt")
         outputs = model.generate(inputs.input_ids, max_length=max_length, num_return_sequences=1)
         response = tokenizer.decode(outputs[0], skip_special_tokens=True)
         return response
     ```

2. **Teste o código**:  
   - Adicione o seguinte código para verificar:  
     ```python
     if __name__ == "__main__":
         prompt = "Explique o que é uma POC em termos simples."
         print(generate_response(prompt))
     ```

3. **Execute o script**:  
   ```bash
   python src/agent.py
   ```

---

### Dados Mockados
1. **Criar um arquivo de dados mockados**:  
   - No arquivo `src/mock_data.json`:  
     ```json
     {
       "questions": [
         "O que é uma POC?",
         "Como usar uma LLM aberta?",
         "Quais são as vantagens de modelos abertos?"
       ],
       "expected_responses": [
         "Uma POC é uma prova de conceito.",
         "Use bibliotecas como Hugging Face Transformers.",
         "Modelos abertos são gratuitos e personalizáveis."
       ]
     }
     ```

2. **Teste os dados mockados**:  
   - Adicione o seguinte ao `src/agent.py`:  
     ```python
     import json

     with open("src/mock_data.json") as f:
         mock_data = json.load(f)

     for question in mock_data["questions"]:
         print("Pergunta:", question)
         print("Resposta:", generate_response(question))
     ```

**Ajustes Finais**
- **Reduzir tamanho do modelo**: Se `distilgpt2` for muito grande para seu ambiente, use modelos menores, como `gpt2-small`.  
- **Personalizar respostas**: Adapte o prompt para direcionar as respostas.  

**Vantagens de Usar uma LLM Aberta**
1. **Offline**: Você pode usar o modelo sem depender de uma API externa.  
2. **Gratuito**: Não há custos adicionais (a não ser pela infraestrutura).  
3. **Controle total**: Você pode ajustar e treinar o modelo para necessidades específicas.  
