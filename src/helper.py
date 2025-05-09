from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader  # Updated imports
#from langchain_community.text_splitter import RecursiveCharacterTextSplitter  # Updated import
from langchain_community.embeddings import HuggingFaceEmbeddings  # Updated import
from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader

# Load PDFs
def load_pdf(directory_path):
    loader = DirectoryLoader(directory_path, glob="*.pdf", loader_cls=PyPDFLoader)
    return loader.load()


def text_split(extracted_data):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=20)
    return text_splitter.split_documents(extracted_data)


def download_hugging_face_embeddings():
    return HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

embeddings = download_hugging_face_embeddings()





