from dotenv import load_dotenv

load_dotenv()
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import InMemoryVectorStore
import streamlit as st
from time import sleep

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None

if "messages" not in st.session_state:
    st.session_state.messages = [] 

def document_process(path):
    # Load PDF
    loader = PyPDFLoader(path)
    documents = loader.load()

    # Split document into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    documents = text_splitter.split_documents(documents)

    # Create embeddings and vector store
    embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2-preview")
    vectorstore = InMemoryVectorStore.from_documents(documents=documents, embedding=embeddings)

    st.session_state.vectorstore = vectorstore
    st.session_state.document_Uploaded = True









st.subheader("Document Q&A ChatBot - Ask questions about the document")
if "document_Uploaded" not in st.session_state:
    st.session_state.document_Uploaded = False


## document upload
if not st.session_state.document_Uploaded:
    file = st.file_uploader("select your PDF file", type="pdf")
    if file:
        with open("uploaded_document.pdf", "wb") as f:
            f.write(file.getvalue())
        with st.spinner("Processing document..."):
            document_process("./uploaded_document.pdf")  
        st.markdown("Document processed successfully ")   
        sleep(2)
        st.rerun() 

if st.session_state.document_Uploaded and st.session_state.vectorstore:

    for one_message in st.session_state.messages:
        role = one_message["role"]
        content = one_message["content"]

        st.chat_message(role).markdown(content)


    query = st.chat_input("Ask a Question ")
    if query:
        st.session_state.messages.append({"role": "user", "content": query})

        st.chat_message("user").markdown(query)
        
        docs = st.session_state.vectorstore.similarity_search(query=query, k=3)
        context=""
        for doc in docs:
            context += doc.page_content + "\n"
        prompt= f"""
                you are a helpful assistant that answers questions based on the context provided below 
                context: {context} and the question is: {query}

        """  

        result = llm.invoke(prompt)  

        st.session_state.messages.append({"role": "ai", "content": result.content})
        st.chat_message("ai").markdown(result.content)

        