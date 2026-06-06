from langchain_community.document_loaders import WebBaseLoader
Loader=WebBaseLoader("https://www.smartprix.com?utm_source=chatgpt.com")
docs=Loader.load()
print(docs)
