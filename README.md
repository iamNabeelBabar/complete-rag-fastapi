# **PDF Vector Search with Pinecone and HuggingFace**

This project demonstrates a pipeline for converting PDF documents into searchable vector embeddings using **LangChain**, **HuggingFace embeddings**, and **Pinecone** as the vector store. It enables **semantic similarity search** across a document without a web or API interface — but the code is modular enough to integrate FastAPI, Flask, or any RAG application framework.

---

## **Features**
- **Load PDFs** using `PyPDFLoader`
- **Clean text** to remove unwanted characters and extra spaces
- **Split text** into manageable chunks for better embeddings
- **Generate embeddings** with `BAAI/bge-small-en-v1.5`
- **Store vectors** in Pinecone for scalable retrieval
- **Query** using similarity search to get the most relevant chunks

---

## **Project Structure**
```
services/
├── loader.py           # Loads PDF and extracts text
├── cleaned.py          # Cleans extracted text
├── splitter.py         # Splits text into chunks
├── pinecone_vector.py  # Pinecone integration (create index, store vectors)
main.py                 # Runs the full pipeline
.env                    # Environment variables (Pinecone API key)
requirements.txt        # Dependencies
```

---

## **Installation**
1. **Clone the repository**
```bash
git clone https://github.com/yourusername/pdf-vector-search-pinecone.git
cd pdf-vector-search-pinecone
```

2. **Create and activate a virtual environment**
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
Create a `.env` file and add your Pinecone API key:
```
PINECONE_API_KEY=your_api_key_here
```

---

## **Usage**
1. Place your PDF file in the project directory.
2. Update the `file_path` variable in `main.py` with your PDF filename.
3. Run the pipeline:
```bash
python main.py
```

---

## **Example Query**
```python
query = "What is AI's role in healthcare?"
pinecone_results = vector.similarity_search(query, k=1)
for result in pinecone_results:
    print(result.page_content)
```

---

## **Future Improvements**
- Add **FastAPI** for serving results via API
- Integrate with a **chatbot** or **web UI**
- Support **multiple embedding models**
- Add **batch document processing**

---

## **License**
This project is licensed under the **MIT License**.
