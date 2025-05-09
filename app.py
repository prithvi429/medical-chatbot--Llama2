from flask import Flask, render_template, jsonify, request
from src.helper import download_hugging_face_embeddings, load_pdf, text_split
from langchain_community.vectorstores import Pinecone  # Updated import
from langchain_community.embeddings import HuggingFaceEmbeddings  # Updated import
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.llms import CTransformers  # Updated import
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
import os
import pinecone 

# Initialize Flask app
app = Flask(__name__)

# Load environment variables
load_dotenv()

# Get the API key and index name from the environment variables
api_key = os.getenv("api_key")
index_name = os.getenv("index_name")

# Initialize Pinecone


# Load and split documents from a directory
document_directory = r"C:\Users\DELL\medical-chatbot--Llama2\Data"  # Path to your directory containing PDFs
extracted_data = load_pdf(document_directory)
text_chunks = text_split(extracted_data)

# Initialize the embeddings
embeddings = download_hugging_face_embeddings()

docsearch = Pinecone.from_texts(
    [chunk.page_content for chunk in text_chunks],
    embedding=embeddings,
    index_name=index_name
)

# Define the prompt template
prompt = PromptTemplate(input_variables=["query"], template="Answer the following question based on the provided context: {query}")

# Wrap it in a dictionary for RetrievalQA
chain_type_kwargs = {"prompt": prompt}

# Initialize the LLM
llm = CTransformers(
    model=r"C:\Users\DELL\medical-chatbot--Llama2\model\llama-2-7b-chat.ggmlv3.q4_0.bin",  # Corrected raw string path
    model_type="llama",
    config={"max_new_tokens": 512, "temperature": 0.7}
)

# Setup the RetrievalQA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=docsearch.as_retriever(),
    chain_type="stuff",
    chain_type_kwargs={"prompt": prompt}
)

# Route for the homepage
@app.route('/')
def home():
    return render_template('chat.html')

# Route to process chat queries and return answers
@app.route("/get", methods=["POST"])
def chat():
    try:
        # Parse JSON data from the request
        data = request.get_json()
        msg = data.get("msg", "").strip()  # Safely get the 'msg' key
        print("User Input:", msg)

        if not msg:
            return jsonify({"answer": "Please provide a valid query."})

        # Process the query using qa_chain
        result = qa_chain.run({"query": msg})
        print("Response:", result)
        return jsonify({"answer": result})  # Return the response as JSON
    except Exception as e:
        print("Error:", str(e))
        return jsonify({"answer": "Sorry, I couldn't process your request."})

# Start the Flask app
if __name__ == "__main__":
    app.run(debug=True)
