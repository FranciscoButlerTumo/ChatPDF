import streamlit as st
import process
from htmlTemplates import css, bot_template, user_template

def handle_user_input(user_question):
    response = st.session_state.conversation(user_question)
    st.session_state.chat_history = response["chat_history"]

    for i,message in enumerate(st.session_state.chat_history):
        if i % 2 == 0: #first user, late bot
            st.write(user_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)


def main():
    st.set_page_config(page_title="Chat PDF", 
                       page_icon=":wave:")
    
    st.write(css, unsafe_allow_html=True)
    
    if 'conversation' not in st.session_state:
        st.session_state.conversation = None
    
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history= None

    st.header("Chat whit multiple PDFs")
    user_question = st.text_input("Ask a question about your documents: ")

    if user_question:
        handle_user_input(user_question)
    
    with st.sidebar:
        st.subheader("Your documents")
        pdf_Docs = st.file_uploader("Upload your PDFs here and press on click on 'Process'", accept_multiple_files=True)
        
        if st.button("Process"):
            with st.spinner("Processing"):
                raw_text = process.get_pdfs_text(pdf_Docs) #return all tex in the pdf's documents
                text_chunks = process.get_text_chunks(raw_text) #filtrer this text
                vector_store = process.get_vector_store(text_chunks) #create embeddings and vector store
                st.session_state.conversation = process.get_conversation_chain(vector_store) #realice the context of the conversaton

if __name__ == "__main__":
    main()