import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

loader = PyPDFLoader("data/sample.pdf")
documents = loader.load()

splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = splitter.split_documents(documents)

embeddings = OpenAIEmbeddings()
db = FAISS.from_documents(docs, embeddings)

llm = ChatOpenAI()

while True:
    query = input("Ask: ")
    if query == "exit":
        break
    results = db.similarity_search(query)
    context = " ".join([doc.page_content for doc in results])
    response = llm.predict(f"Context: {context}\nQuestion: {query}")
    print(response)
