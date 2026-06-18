import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain_pinecone import PineconeVectorStore
from langchain_community.document_loaders import TextLoader


load_dotenv()

if __name__ == "__main__":
    print("Hello from ingestion.py!")
    print(os.environ.get("PINECONE_API_KEY"))