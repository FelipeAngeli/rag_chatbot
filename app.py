import os
import tempfile
import streamlit as st

from decouple import config

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma  import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import OpenAIEmbeddings


os.environ['OPENAI_API_KEY'] = config('OPENAI_API_KEY')
persist_direrctory = 'db'


def process_pdf(file):
    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as temp_file:
        temp_file.write(file.read())
        temp_file_path = temp_file.name

    loader = PyPDFLoader(temp_file_path)
    docs = loader.load()

    os.remove(temp_file_path)

    text_spliter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=400,
    )
    chunks = text_spliter.split_documents(documents=docs)
    return chunks

def load_existing_vector_store():
    if os.path.exists(os.path.join(persist_direrctory)):
        vector_store = Chroma(
            persist_directory=persist_direrctory,
            embedding_function=OpenAIEmbeddings(),
        )
        return vector_store
    return None

def add_to_vector_store(chunks, vector_store=None):
    if vector_store:
        vector_store.add_documents(chunks)
    else:
        vector_store = Chroma.from_documents(
            documents=chunks,
            embedding=OpenAIEmbeddings(),
            persist_directory=persist_direrctory,
        )
    return vector_store        


vector_store = load_existing_vector_store()

st.set_page_config(
    page_title='Rag Chatbot',
    page_icon='🤖',
),

st.header('🤖 Chat com seus documentos RAG')

with st.sidebar:
    st.write('📁 Upload de arquivos')
    uploaded_file = st.file_uploader(
        label= 'Faça o upload do seu arquivo',
        type= ['pdf', 'docx'],
        accept_multiple_files= True,
        )
    
    if uploaded_file:
        st.spinner('Processando arquivos...')
        all_chunks = []
        for uploaded_file in uploaded_file:
            chunks = process_pdf(file=uploaded_file)
            all_chunks.extend(chunks)
        st.success('Arquivos processados com sucesso!')
        vector_store = add_to_vector_store(
            chunks=all_chunks,
            vector_store=vector_store,
            )

    model_options = [
        'gpt-3.5-turbo',
        'gpt-4',
        'gpt-4-turbo',
        'gpt-4o-mini',
        'gpt-4o',
    ]
    selected_model = st.sidebar.selectbox(
        label='Selecione o modelo LLM',
        options=model_options,
    ),

if 'messages' not in st.session_state:
    st.session_state['messages'] = []
    

question = st.chat_input('Como posso te ajudar?')

if vector_store and question:
    ...