import streamlit as st


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