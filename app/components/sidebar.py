import streamlit as st
from app.services.document_processing import process_pdf
from app.services.vector_store import add_to_vector_store


def render_sidebar(vector_store):
    with st.sidebar:
        st.write('📁 Upload de arquivos')
        uploaded_files = st.file_uploader(
            label='Faça o upload do seu arquivo',
            type=['pdf', 'docx'],
            accept_multiple_files=True,
        )

        if uploaded_files:
            with st.spinner('Processando arquivos...'):
                all_chunks = []
                for uploaded_file in uploaded_files:
                    chunks = process_pdf(file=uploaded_file)
                    all_chunks.extend(chunks)
                st.success('Arquivos processados com sucesso!')
                vector_store = add_to_vector_store(chunks=all_chunks, vector_store=vector_store)
        
        model_options = [
            'gpt-3.5-turbo',
            'gpt-4',
            'gpt-4-turbo',
            'gpt-4o-mini',
            'gpt-4o',
        ]
        selected_model = st.selectbox('Selecione o modelo LLM', options=model_options)
        
        return vector_store, selected_model
