from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
load_dotenv()
Loader=PyPDFLoader("Documents_Loader/GRU.pdf")
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