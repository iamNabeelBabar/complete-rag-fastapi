from services.cleaned import clean_data
from services.loader import load_file
from services.splitter import splitted_data
from services.pinecone_vector import create_index
from services.pinecone_vector import get_pinecone_client
from services.pinecone_vector import create_vector
from langchain_huggingface import HuggingFaceEmbeddings

# -------> File path (Path of the pdf that we have to load)
file_path = 'national ai policy.pdf'
pages = load_file(file_path)
# print(pages[0])  ---> print the len of pages


# -------> Cleaned data is stored
cleaned_data = clean_data(pages)


# ------>splitted data is stored
splitted_data = splitted_data(cleaned_data)
# print(splitted_data[80]) ---> print the splitted page
# print(len(splitted_data))

#  ------> Intialize embedding model
embed_model = HuggingFaceEmbeddings(model_name='BAAI/bge-small-en-v1.5')

# --------> get pinecone index
pc = get_pinecone_client()

# -------> Create Index
index = create_index(pc)

#Convert documents into vectors using LangPinecone

vector = create_vector(splitted_data, embed_model=embed_model, index_name="rag-ai")

# Query from vector store
query = "What is ai role in healthcare?"
pinecone_results = vector.similarity_search(query, k=1)

for result in pinecone_results:
  print(result.page_content)