from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI


import pinecone
pinecone.init(api_key="", environment="")


from dotenv import dotenv_values
config = dotenv_values(".env") 
if __name__ == "__main__":
    print("Hello VectorStore!")
    api_key = config["OPENAI_API_KEY"]
    loader = TextLoader("D:\LLM and LangChain\intro-into-vector-db\mediumblogs\mediumblogs.txt", encoding="utf-8")
    document = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(document)
    print(len(texts))
    embeddings = OpenAIEmbeddings(openai_api_key=api_key)
    docsearch = Pinecone.from_documents(texts, embeddings, index_name="medium-blogs-embeddings-index")  
    qa = RetrievalQA.from_chain_type(llm=OpenAI(openai_api_key=api_key) , chain_type="stuff", retriever=docsearch.as_retriever())

    query = "What is a vector DB ? Give me a 15 word for a beginner "
    result = qa({"query" : query})
    print(result)