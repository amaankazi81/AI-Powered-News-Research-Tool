import streamlit as st
import os
from dotenv import load_dotenv
from langchain_community.document_loaders.text import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough

from utils import load_article, load_pdf

# Load env
load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

st.set_page_config(page_title="News Research Tool", layout="wide")
st.title("📊 AI News Research Tool (Finance & Stocks)")

# Sidebar
st.sidebar.header("Upload Data")
urls = st.sidebar.text_area("Paste News Article URLs (one per line)")
pdf_files = st.sidebar.file_uploader("Upload PDFs", type=["pdf"], accept_multiple_files=True)

process_btn = st.sidebar.button("Process Data")

# Session state
if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None

if process_btn:
    documents = []

    if urls:
        for url in urls.split("\n"):
            if url.strip():
                documents.append(load_article(url.strip()))

    if pdf_files:
        for pdf in pdf_files:
            documents.append(load_pdf(pdf))

    combined_text = "\n".join(documents)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100
    )

    chunks = splitter.split_text(combined_text)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.from_texts(chunks, embeddings)
    st.session_state.vectorstore = vectorstore

    st.success("✅ Data processed successfully!")

# Question Section
st.header("Ask a Financial Question")
query = st.text_input("Ask about stocks, market trends, financial insights")

if query and st.session_state.vectorstore:
    retriever = st.session_state.vectorstore.as_retriever(search_kwargs={"k": 4})

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash-lite",
        temperature=0.2
    )

    prompt = PromptTemplate(
        template="""
You are a financial research assistant.
Use the provided context to answer the question accurately.
Focus on stock market, finance, companies, trends and insights.

Context:
{context}

Question:
{question}

Answer:
""",
        input_variables=["context", "question"]
    )

    chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
    )

    response = chain.invoke(query)

    st.subheader("📌 Answer")
    st.write(response.content)

elif query:
    st.warning("⚠️ Please process data first.")
