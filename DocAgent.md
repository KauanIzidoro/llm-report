# Planejamento para a POC do Agente

## Objetivo
Desenvolver uma prova de conceito (POC) para um agente capaz de analisar dados de um repositório e gerar saídas estruturadas conforme exemplos definidos. O foco será na parte de desenvolvimento do agente, enquanto interfaces e UX serão tratados por outro time.

---

## Itens de Backlog

1. **Preparação do Ambiente**
   - Garantir que o repositório local está clonado.
   - Configurar dependências necessárias no ambiente de desenvolvimento.
     - Linguagem: Python (outras linguagens podem ser avaliadas conforme necessário).
     - Instalação de bibliotecas principais:
       - `eralchemy`
       - `graphviz`
       - Outras bibliotecas para manipulação de dados e LLMs.

2. **Pesquisa e Escolha de LLMs**
   - Identificar opções disponíveis para LLMs:
     - Modelos de código aberto: GPT, Llama 2, etc.
     - APIs de serviços externos, como OpenAI ou Hugging Face.
   - Avaliar prós e contras de cada opção com base em:
     - Facilidade de integração.
     - Eficiência e precisão para gerar saídas desejadas.
     - Custos (se aplicável).

3. **Desenvolvimento do Agente**
   - Criar um esqueleto básico para o agente:
     - **Input**: Dados do repositório.
     - **Output**: Diagrama e respostas conforme exemplos fornecidos.
   - Implementar suporte para entradas/saídas simples:
     - Inputs: Arquivos estruturados (e.g., JSON, CSV).
     - Outputs: Diagramas em formatos gráficos (e.g., PNG, PDF) e textos estruturados.
   - Testar as bibliotecas:
     - `eralchemy` para geração de diagramas de banco de dados.
     - `graphviz` para visualizações.

4. **Mockar Dados e Fluxos**
   - Criar exemplos simples que representem os dados esperados.
   - Desenvolver fluxos mockados para validar o comportamento esperado:
     - Exemplos de inputs.
     - Outputs pré-definidos para verificar se o agente está funcionando conforme esperado.

5. **Testes e Validação**
   - Testar o agente com os dados mockados.
   - Ajustar saídas para se alinhar aos exemplos definidos.
   - Documentar os passos de execução e ajustes feitos.

---

## Estimativa de Tempo (em alto nível)

| Atividade                         | Tempo Estimado  |
|------------------------------------|-----------------|
| Preparação do Ambiente             | 1 dia           |
| Pesquisa e Escolha de LLMs         | 2 dias          |
| Desenvolvimento do Agente          | 5 dias          |
| Mockar Dados e Fluxos              | 2 dias          |
| Testes e Validação                 | 3 dias          |
| **Total Estimado**                 | **13 dias**     |

---

## Ordem de Execução dos Itens

1. Preparação do Ambiente.
2. Pesquisa e Escolha de LLMs.
3. Mockar Dados e Fluxos (parcial, para inputs e outputs simples).
4. Desenvolvimento do Agente (iterativo, com validação inicial usando dados mockados).
5. Testes e Validação.

---

## Considerações Técnicas

### Linguagens e Ferramentas
- **Linguagem principal**: Python.
- **Bibliotecas**:
  - `eralchemy` e `graphviz` para visualizações.
  - Bibliotecas de integração com LLMs (e.g., `openai`, `transformers`).
  - Frameworks auxiliares para manipulação de dados (e.g., `pandas`, `json`).

### Inputs e Outputs
- **Inputs**: Arquivos JSON ou CSV simples representando os dados do projeto.
- **Outputs**:
  - Diagramas em formatos gráficos gerados por `eralchemy` e `graphviz`.
  - Respostas textuais estruturadas.

### Mock de Dados
- Exemplos de banco de dados fictícios (estrutura e dados).
- Exemplos de perguntas que o agente deve responder e os diagramas correspondentes.

---

## Próximos Passos

1. Concluir a configuração do ambiente e testar as bibliotecas `eralchemy` e `graphviz`.
2. Finalizar a escolha do LLM a ser utilizado.
3. Desenvolver a primeira versão do agente com dados mockados.
4. Iterar e ajustar conforme necessário até atingir os requisitos da POC.
