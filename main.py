import os
import warnings



warnings.filterwarnings("ignore")

# Disable ChromaDB telemetry entirely
os.environ["ANONYMIZED_TELEMETRY"] = "false"

# Patch Chroma telemetry capture function (Windows fix)
try:
    import chromadb.telemetry
    chromadb.telemetry.capture = lambda *args, **kwargs: None
except Exception:
    pass

# Disable HuggingFace logs & progress bars
os.environ["TRANSFORMERS_VERBOSITY"] = "error"
os.environ["HF_HUB_DISABLE_TELEMETRY"] = "1"
os.environ["HF_HUB_DISABLE_PROGRESS_BARS"] = "1"
os.environ["TOKENIZERS_PARALLELISM"] = "false"

# Disable LangChain debug/tracing
os.environ["LANGCHAIN_TRACING_V2"] = "false"
os.environ["LANGCHAIN_ENDPOINT"] = ""
os.environ["LANGCHAIN_API_KEY"] = ""

# -----------------------------------------------------------
# IMPORTS
# -----------------------------------------------------------

from typing import List
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA




def load_speech(path: str):
    loader = TextLoader(path, encoding="utf-8")
    return loader.load()


def split_text(documents):
    splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=300,
        chunk_overlap=50
    )
    return splitter.split_documents(documents)


def create_vector_store(chunks):
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="db"
    )
    vectordb.persist()
    return vectordb


def build_qa_system(vectordb):
    retriever = vectordb.as_retriever(search_kwargs={"k": 3})

    llm = Ollama(model="mistral")

    qa_system = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=False
    )

    return qa_system



def main():
    print("\n========== AmbedkarGPT ==========\n")

    documents = load_speech("speech.txt")
    chunks = split_text(documents)
    vectordb = create_vector_store(chunks)
    qa = build_qa_system(vectordb)

    while True:
        query = input("\nQuestion: ").strip()

        if query.lower() == "exit":
            print("\nGoodbye!\n")
            break

        response = qa.invoke({"query": query})
        print("\nAnswer:", response["result"])


if __name__ == "__main__":
    main()
