from dotenv import load_dotenv

load_dotenv()
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAI , ChatGoogleGenerativeAI
from langchain_community.vectorstores import InMemoryVectorStore

## Document Loader
## Load the PDF document using PyPDFLoader




## splitting the document into smaller chunks using RecursiveCharacterTextSplitter








## embedding the document chunks using GoogleGenerativeAI embeddings and storing them in an InMemoryVectorStore