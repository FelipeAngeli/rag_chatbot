import streamlit as st

from app.services.vector_store import load_existing_vector_store
from app.components.sidebar import render_sidebar
from app.components.chat import render_chat


st.set_page_config(
    page_title='Rag Chatbot',
    page_icon='🤖',
    layout="wide",
)

st.header('🤖 Chat com seus documentos RAG')

vector_store = load_existing_vector_store()
vector_store, selected_model = render_sidebar(vector_store)

render_chat(vector_store, selected_model)