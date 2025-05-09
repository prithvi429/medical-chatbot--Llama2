# Medical Chatbot with Llama 2

This project implements a medical chatbot using the Llama 2 language model, Pinecone for vector storage, and LangChain for retrieval-based question answering. The chatbot is designed to provide helpful answers to medical queries based on a dataset of medical documents.

## Features

- **PDF Document Processing**: Load and process medical PDFs to extract relevant information.
- **Text Chunking**: Split large documents into manageable chunks for efficient embedding and retrieval.
- **Embeddings**: Use HuggingFace embeddings for semantic similarity.
- **Vector Storage**: Store embeddings in Pinecone for fast similarity searches.
- **Retrieval-Based QA**: Answer user queries by retrieving the most relevant chunks and generating responses using the Llama 2 model.
- **Interactive Chat**: Engage in a conversational interface to ask medical questions.

## Prerequisites

- Python 3.8 or higher
- Anaconda or virtual environment
- Pinecone API key and environment
- Llama 2 model (downloaded locally)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/medical-chatbot-llama2.git
   cd medical-chatbot-llama2
   ```

2. Create a virtual environment and activate it:
   ```bash
   conda create -n medical python=3.8 -y
   conda activate medical
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Install Pinecone:
   ```bash
   pip install pinecone-client
   ```

5. Download the Llama 2 model and place it in the `model` directory:
   ```plaintext
   C:\Users\DELL\medical-chatbot--Llama2\model\llama-2-7b-chat.ggmlv3.q4_0.bin
   ```

## Usage

1. Start the Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

2. Open the `trials.ipynb` notebook and execute the cells step by step.

3. Interact with the chatbot:
   - Provide a query in the input prompt.
   - Type `exit` or `quit` to end the session.

## Project Structure

```
medical-chatbot--Llama2/
├── Data/                     # Directory for medical PDFs
├── model/                    # Directory for the Llama 2 model
├── research/
│   ├── trials.ipynb          # Main notebook for the chatbot
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies
```

## Key Components

- **LangChain**: Framework for building retrieval-based question-answering systems.
- **Pinecone**: Vector database for storing and retrieving embeddings.
- **HuggingFace Embeddings**: Pre-trained embeddings for semantic similarity.
- **Llama 2**: Language model for generating responses.

## Example Query

```plaintext
Input Prompt (or type 'exit' to quit): What are allergies?
Response: Allergies occur when your immune system overreacts to a foreign substance, such as dust, pollen, or pet dander.
```

## Troubleshooting

- **Connection Issues**: Ensure your Pinecone API key and environment are correctly configured.
- **Model Loading Errors**: Verify the Llama 2 model path and file integrity.
- **Dependency Errors**: Ensure all required packages are installed using `pip install -r requirements.txt`.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Meta's Llama 2](https://ai.meta.com/llama/)
- [Pinecone](https://www.pinecone.io/)
- [LangChain](https://www.langchain.com/)
- [HuggingFace](https://huggingface.co/)

## Contact

For questions or feedback, please contact [your-email@example.com].