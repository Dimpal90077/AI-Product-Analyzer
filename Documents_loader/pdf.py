from langchain_community.document_loaders import PyPDFLoader
Loader=PyPDFLoader("Documents_Loader/GRU.pdf")
docs=Loader.load()
print(len(docs))