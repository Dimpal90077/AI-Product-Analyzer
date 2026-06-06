from dotenv import load_dotenv
from langchain_community.document_loaders import WebBaseLoader
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
load_dotenv()
Loader=WebBaseLoader("https://www.smartprix.com?utm_source=chatgpt.com")
docs=Loader.load()
temp=ChatPromptTemplate.from_messages([
    ("system","you are a helpul AI Assistant that helps users to summaries the content of documents"),
    ("human","{Loader}")
])
llm = ChatMistralAI(
    model="mistral-large-latest",
)

prompt=temp.format_messages(Loader=docs[0].page_content)

response = llm.invoke(prompt)
print(response.content)