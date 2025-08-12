
from langchain.docstore.document import Document
#Recursive character text splitter
from langchain_text_splitters import RecursiveCharacterTextSplitter



re_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 800,
    chunk_overlap = 200
)


def splitted_data(cleaned_data):
    doc_list = []
    for page in cleaned_data:
        pg_split = re_splitter.split_text(page.page_content)

        for pg_sub_split in pg_split:
            metadata = {"source": "AI policy", "page_no": page.metadata["page"] + 1}

            doc_string = Document(page_content = pg_sub_split, metadata=metadata)
            doc_list.append(doc_string)
    return doc_list