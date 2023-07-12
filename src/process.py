from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI

#load keys
load_dotenv()

#get pdf text
def get_pdfs_text(pdf_Docs):
    raw_text=""
    for pdf in pdf_Docs:
        pdf_reader=PdfReader(pdf)
        for page in pdf_reader.pages:
            text = page.extract_text()
            if text: #
                raw_text += text
    return raw_text

#get the text chunks
def get_text_chunks(raw_text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000, #number of words to read
        chunk_overlap=200, #amount of protection words to avoid losing the context
        length_function=len
    )
    chunks=text_splitter.split_text(raw_text)
    return chunks

#create vectore store
def get_vector_store(text_chunks):
    embeddings = OpenAIEmbeddings()
    vector_store=FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return(vector_store)

#feed model on verctor_store
def get_conversation_chain(vector_store):
    llm = ChatOpenAI(temperature=0.1) #temperature indicates randomness
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm, #model lenguage 
        retriever=vector_store.as_retriever(), #retriever context of pdfs
        memory=memory #memory of the process
    )
    return conversation_chain