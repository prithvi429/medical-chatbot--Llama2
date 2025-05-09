# AniMed Assistant - Medical Chatbot

AniMed Assistant is an interactive medical chatbot powered by Llama 2, Pinecone, and LangChain. It provides intelligent responses to medical queries based on a dataset of medical documents. The chatbot features a futuristic UI with animations and particle effects for an engaging user experience.

## Features

- **Interactive Chat Interface**: A visually appealing chat interface with animations and glitch effects.
- **Medical Query Processing**: Answers medical-related questions using advanced language models.
- **PDF Document Processing**: Loads and processes medical PDFs to extract relevant information.
- **Vector Storage**: Uses Pinecone for efficient vector storage and retrieval.
- **Customizable Prompt**: Define custom prompts for the chatbot's responses.

## Prerequisites

- Python 3.8 or higher
- Node.js (optional, for frontend development)
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

4. Install additional packages:
   ```bash
   pip install -U langchain-community langchain-huggingface
   ```

5. Download the Llama 2 model and place it in the `model` directory:
   ```plaintext
   C:\Users\DELL\medical-chatbot--Llama2\model\llama-2-7b-chat.ggmlv3.q4_0.bin
   ```

6. Set up your `.env` file with the following variables:
   ```plaintext
   api_key=your_pinecone_api_key
   index_name=medical-chatbot
   ```

## Usage

1. Start the Flask application:
   ```bash
   python app.py
   ```

2. Open your browser and navigate to:
   ```plaintext
   http://127.0.0.1:5000/
   ```

3. Interact with the chatbot by typing your queries in the input box.

## Project Structure

```
medical-chatbot--Llama2/
├── Data/                     # Directory for medical PDFs
├── model/                    # Directory for the Llama 2 model
├── src/
│   ├── helper.py             # Helper functions for loading PDFs and embeddings
├── templates/
│   ├── chat.html             # Frontend HTML for the chatbot
├── app.py                    # Flask application
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
User: What are the symptoms of diabetes?
Bot: The symptoms of diabetes include increased thirst, frequent urination, extreme hunger, unexplained weight loss, and fatigue.
```

## Troubleshooting

- **No Response from Chatbot**:
  - Ensure the `/get` endpoint is correctly configured in `app.py`.
  - Verify the frontend sends the query in JSON format.

- **Model Loading Errors**:
  - Check the path to the Llama 2 model in `app.py`.
  - Ensure the model file is downloaded and placed in the correct directory.

- **Dependency Errors**:
  - Ensure all required packages are installed using `pip install -r requirements.txt`.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Meta's Llama 2](https://ai.meta.com/llama/)
- [Pinecone](https://www.pinecone.io/)
- [LangChain](https://www.langchain.com/)
- [HuggingFace](https://huggingface.co/)

## Contact

For questions or feedback, please contact [prithvirathod29884@gmail.com].