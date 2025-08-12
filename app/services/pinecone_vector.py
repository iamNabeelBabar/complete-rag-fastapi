import os
import getpass
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore as langchain_pinecone
from fastapi import HTTPException

load_dotenv()  # Load environment variables from .env


def get_pinecone_client():
    """Get a Pinecone client, prompting for API key if not set."""
    try:
        api_key = os.getenv("PINECONE_API_KEY")
        if not api_key:
            api_key = getpass.getpass("Enter your Pinecone API key: ")
            os.environ["PINECONE_API_KEY"] = api_key

        if not api_key.strip():
            raise HTTPException(status_code=500, detail="Pinecone API key is missing or empty.")

        return Pinecone(api_key=api_key)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error initializing Pinecone client: {e}")


def create_index(pc: Pinecone, index_name: str = "rag-ai"):
    """Create Pinecone index if it doesn't exist."""
    try:
        if not pc.has_index(index_name):
            pc.create_index(
                name=index_name,
                dimension=384,
                metric="cosine",
                spec=ServerlessSpec(cloud="aws", region="us-east-1"),
            )
        return pc.Index(index_name)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating Pinecone index '{index_name}': {e}")


def create_vector(doc_list, embed_model, index_name: str = "rag-ai"):
    """Convert documents into Pinecone vectors."""
    try:
        if not doc_list:
            raise HTTPException(status_code=400, detail="Document list is empty.")
        if not embed_model:
            raise HTTPException(status_code=400, detail="Embedding model is missing.")

        return langchain_pinecone.from_documents(
            doc_list,
            embed_model,
            index_name=index_name
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating vectors in index '{index_name}': {e}")
