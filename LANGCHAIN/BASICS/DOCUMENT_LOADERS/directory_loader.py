from langchain_community.document_loaders import DirectoryLoader , PyPDFLoader

loader = DirectoryLoader(
    path = "/Users/pandhari/Desktop/NLP/LANGCHAIN/DOCUMENT_LOADERS/Books" , 
    glob = "*.pdf" , 
    loader_cls = PyPDFLoader
)

docs = loader.lazy_load()

for documents in docs:
    print(documents.metadata)

