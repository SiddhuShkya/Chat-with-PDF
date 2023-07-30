import os
import streamlit as st
from dotenv import load_dotenv
from htmlTemplates import css, bot_template, user_template
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import HuggingFaceHub
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
import pickle

def checkPDF(pdf):
    if pdf is None:
        return False
    return True

def checkEmbedding(store_name):
    if os.path.exists(f"./embeddings/{store_name}.pkl"):
        return True
    return False

def getPDFtext(pdf):
    text = ""
    for page in pdf.pages:
        text += page.extract_text()
    return text

def textTochunks(text):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text=text)
    return chunks

def getVectorstore(chunks, store_name):
    if checkEmbedding(store_name):
        with open(f"./embeddings/{store_name}.pkl", "rb") as f:
            VectorStore = pickle.load(f)
        st.write('Embeddings Loaded from the Disk.')
    else:
        embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
        VectorStore = FAISS.from_texts(chunks, embedding=embeddings)
        with open(f"./embeddings/{store_name}.pkl", "wb") as f:
            pickle.dump(VectorStore, f)
        st.write('Embeddings Computation Completed.')
    return VectorStore

def get_conversation_chain(vector_store):
    repo_id = "tiiuae/falcon-7b-instruct"
    llm = HuggingFaceHub(repo_id=repo_id, model_kwargs={"temperature":0.6, "max_new_tokens":500})
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm, 
        retriever=vector_store.as_retriever(),
        memory=memory
    )
    return conversation_chain

def handle_user_input(question):
    response = st.session_state.conversation({'question': question})
    st.session_state.chat_history = response['chat_history']
    for i, message in enumerate(st.session_state.chat_history):
        if i%2 == 0:
            st.write(user_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)

def main():
    load_dotenv()
    st.set_page_config(page_title="Chat With PDF", page_icon="📑")
    st.header("Chat with PDF 📑")
    st.markdown(css, unsafe_allow_html=True)
    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None
    user_question = st.text_input("Your Question : ", key="user_input")
    if user_question:
        handle_user_input(user_question)
    with st.sidebar:
        st.subheader("Your documents")
        pdf = st.file_uploader("upload your PDF here and Click on 'Process'")
        if (checkPDF(pdf) and st.button("Process")):
            store_name = pdf.name[:-4]
            with st.spinner("Processing"):
                pdf_reader = PdfReader(pdf)
                text = getPDFtext(pdf_reader)
                chunks = textTochunks(text)
                vectorstore = getVectorstore(chunks, store_name)
                st.session_state.conversation = get_conversation_chain(vectorstore)


if __name__ == '__main__':
    main()
