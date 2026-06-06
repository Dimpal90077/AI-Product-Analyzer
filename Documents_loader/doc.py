from langchain_community.document_loaders import TextLoader
Loader=TextLoader("Documents_Loader/notes.txt")
docs=Loader.load()
print(len(docs))
print(docs[0].page_content)