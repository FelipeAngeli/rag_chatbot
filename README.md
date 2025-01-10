
# RAG Chatbot

RAG Chatbot é um projeto desenvolvido utilizando Streamlit, LangChain e OpenAI para criar um chatbot capaz de processar documentos carregados pelo usuário, extrair informações relevantes e responder perguntas de forma interativa.



https://github.com/user-attachments/assets/0c23c712-b6c5-4ea1-b9ce-a5c1b159c029



## Funcionalidades

- **Upload de Arquivos:** Suporta upload de arquivos PDF e DOCX para análise.
- **Processamento de Texto:** Divide os documentos em chunks de texto para melhor processamento.
- **Armazenamento de Dados:** Utiliza vetores com embeddings para armazenar e recuperar informações de forma eficiente.
- **Modelos de IA:** Suporte a modelos LLM como `gpt-3.5-turbo` e `gpt-4`.
- **Interface de Chat:** Interface interativa para o usuário fazer perguntas sobre os documentos carregados.

## Estrutura do Projeto

```
rag_chatbot/
├── app/
│   ├── components/
│   │   ├── chat.py           # Lida com a interface de chat
│   │   ├── sidebar.py        # Gerencia a barra lateral
│   └── services/
│       ├── document_processing.py  # Processa documentos carregados
│       ├── vector_store.py         # Gerencia os vetores de dados
│       ├── question_answering.py   # Realiza perguntas com base nos documentos
├── config/
│   ├── settings.py           # Configurações globais
├── main.py                   # Ponto de entrada do aplicativo
├── requirements.txt          # Dependências do projeto
```

## Tecnologias Utilizadas

- **Streamlit:** Para a interface de usuário.
- **LangChain:** Para gerenciamento de documentos e fluxos de perguntas/respostas.
- **OpenAI:** Modelos de linguagem para processamento e respostas.
- **Chroma:** Armazenamento de vetores.
- **PyPDFLoader:** Processamento de documentos PDF.

## Como Executar

### Pré-requisitos

1. Python 3.8 ou superior.
2. Instalar as dependências listadas no `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

3. Configurar a chave da API OpenAI no arquivo `.env`:
   ```
   OPENAI_API_KEY=your_openai_api_key
   ```

### Rodando o Projeto

1. Execute o seguinte comando para iniciar o Streamlit:
   ```bash
   streamlit run app.py
   ```

2. Acesse o aplicativo no navegador:
   - URL Local: `http://localhost:8501`
   - URL de Rede: `http://<seu_ip_local>:8501`

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## Licença

Este projeto está sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.
