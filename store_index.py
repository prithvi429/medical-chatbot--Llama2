from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_huggingface.embeddings import HuggingFaceEmbeddings  # Corrected import
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Pinecone  # Corrected import
import pinecone
from dotenv import load_dotenv
import os

from src.helper import load_pdf, text_split, download_hugging_face_embeddings

# Load environment variables
load_dotenv()

# Get the environment variables
api_key = os.getenv("api_key")
index_name = os.getenv("index_name")

# Initialize Pinecone client
pinecone.init(api_key=api_key, environment="us-west1-gcp")  # Add the environment if necessary

# Load and split data
extracted_data = load_pdf("Data")  # Path to your data (PDFs, etc.)
text_chunks = text_split(extracted_data)

# Initialize HuggingFace embeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Create the Pinecone index (if not already created)
if index_name not in pinecone.list_indexes():
    pinecone.create_index(index_name, dimension=768)  # Ensure dimension matches your embedding size

# Connect to Pinecone index
index = pinecone.Index(index_name)

# Store vectors in Pinecone
docsearch = Pinecone.from_texts(
    [chunk.page_content for chunk in text_chunks],
    embedding=embeddings,
    index_name=index_name
)

print(f"Indexing completed successfully!")
