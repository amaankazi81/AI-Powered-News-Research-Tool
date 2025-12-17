# 📰 AI-Powered News Research Tool (Finance & Stock Market)

An AI-based news research application that enables users to analyze **financial news articles and PDFs** and ask **natural language questions** to receive accurate, context-aware insights related to the **stock market and finance domain**.

The project is built using **LangChain (LCEL)**, **Google Gemini**, **FAISS**, and **Streamlit**, following a modern **Retrieval-Augmented Generation (RAG)** architecture.

---

## 🚀 Features

- 📄 Upload **financial PDFs** (reports, analysis documents)
- 🔗 Input **news article URLs**
- 💬 Ask natural language questions
- 📊 Get AI-generated insights focused on:
  - Stock market trends  
  - Company performance  
  - Financial analysis  
- ⚡ Fast semantic search using vector embeddings
- 🧠 Reduced hallucinations using RAG architecture
- 🖥️ User-friendly Streamlit interface

---

## 🧠 Project Architecture (RAG Pipeline)

User Input (URL / PDF)
        ↓
Text Extraction
        ↓
Text Chunking
        ↓
Embedding Generation
        ↓
FAISS Vector Store
        ↓
Relevant Context Retrieval
        ↓
Gemini LLM
        ↓
Final Answer




---

## 🛠️ Tech Stack

| Technology | Purpose |
|---------|--------|
| **Python** | Backend language |
| **Streamlit** | Web UI |
| **LangChain (LCEL)** | AI workflow orchestration |
| **Google Gemini (gemini-pro)** | Large Language Model |
| **FAISS** | Vector similarity search |
| **HuggingFace Embeddings** | Text embeddings |
| **Newspaper3k** | News article extraction |
| **PyPDF** | PDF text extraction |

---

## 📂 Project Structure

    ```text
      news-research-tool/
      │
      ├── app.py              # Main Streamlit application
      ├── utils.py            # Article & PDF loading utilities
      ├── requirements.txt    # Project dependencies
      ├── .env                # Environment variables
      └── README.md           # Project documentation


## ⚙️ Installation & Setup

  1. **Clone the Repository**
      ```bash
            git clone https://github.com/your-username/news-research-tool.git
            cd news-research-tool
  
  2. **Create Virtual Environment**
      ```
        python -m venv venv
        venv\Scripts\activate 
  
  ### 3️⃣ Install Dependencies
      ```bash
      pip install -r requirements.txt
      pip install lxml[html_clean]
  
  ### 4️⃣ Set Environment Variables
      Create a .env file:
      
          ```env
          GOOGLE_API_KEY=your_google_gemini_api_key
  
  ### 5️⃣ Run the Application
      ```bash
      streamlit run app.py


## 🧪 How It Works (Technical Overview)

1. **Text Extraction**

  - News articles are parsed using newspaper3k
  
  - PDFs are parsed using pypdf

2. **Text Chunking**

  - Large documents are split into overlapping chunks to handle token limits

3. **Embeddings**

  - Each chunk is converted into vector embeddings using HuggingFace models

4. **Vector Storage**

  - FAISS stores embeddings and enables fast similarity search

5. **Query Processing**

  - Relevant chunks are retrieved based on user queries

6. **Answer Generation**

  - Google Gemini (gemini-pro) generates context-aware answers using retrieved data


## 📄 License

This project is for educational and demonstration purposes.
