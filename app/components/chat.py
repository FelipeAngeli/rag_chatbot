import streamlit as st

from app.services.question_answering import ask_question


def render_chat(vector_store, selected_model):
    if 'messages' not in st.session_state:
        st.session_state['messages'] = []

    question = st.chat_input('Como posso te ajudar?')

    if vector_store and question:
        for message in st.session_state.messages:
            st.chat_message(message.get('role')).write(message.get('content'))

        st.chat_message('user').write(question)
        st.session_state.messages.append({'role': 'user', 'content': question})

        with st.spinner('Buscando resposta...'):
            response = ask_question(
                model=selected_model,
                query=question,
                vector_store=vector_store,
            )

            st.chat_message('ai').markdown(response)
            st.session_state.messages.append({'role': 'ai', 'content': response})
