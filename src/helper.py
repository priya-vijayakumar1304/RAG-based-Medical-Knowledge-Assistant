from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from typing import List
from langchain_core.documents import Document


def load_pdf_files(data_path):
    """
    Extracts texts from PDF files in the directory
    """
    loader = DirectoryLoader(
        data_path,
        glob="*.pdf", #can load multiple documents
        loader_cls=PyPDFLoader,
    )
    documents = loader.load()
    return documents


def filter_to_minimal_docs(docs: List[Document]) -> List[Document]:
    """
    Given a list of Documents, return a new list of Document objects containing only source and page no
    """
    minimal_docs: List[Document] = []
    for doc in docs:
        minimal_metadata = {
            "source": doc.metadata.get("source"),
            "page_no": doc.metadata.get("page_label")
        }
        minimal_doc = Document(page_content=doc.page_content, metadata=minimal_metadata)
        minimal_docs.append(minimal_doc)
    return minimal_docs


def text_split(documents):
    """
    Splits the documents into smaller chunks
    """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=100,
    )
    text_chunks = text_splitter.split_documents(documents)
    return text_chunks


def download_embeddings_model():
    """
    Downloads and returns a HuggingFaceEmbeddings model
    """
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    return embeddings