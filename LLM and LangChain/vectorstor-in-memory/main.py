from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

from dotenv import dotenv_values
config = dotenv_values(".env") 


if __name__ == "__main__":
    api_key = config["OPENAI_API_KEY"]
    pdf_path = "D:\\LLM and LangChain\\vectorstor-in-memory\\Christian-stoicism.pdf"
    loader = PyPDFLoader(file_path=pdf_path)
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=30, separator="\n")
    docs = text_splitter.split_documents(documents=documents)

    embeddings = OpenAIEmbeddings(openai_api_key=api_key)
    vectorstore = FAISS.from_documents(docs,embeddings)
    vectorstore.save_local("faiss_index_react") 

    new_vectorstore = FAISS.load_local("faiss_index_react", embeddings)
    qa = RetrievalQA.from_chain_type(llm=OpenAI(openai_api_key=api_key), chain_type="stuff", retriever = new_vectorstore.as_retriever())
    res = qa.run("Apa itu stoisisme kristen ?")
    print(res)