import os
from dotenv import load_dotenv
from llama_index.core import SimpleDirectoryReader
from llama_index.core import VectorStoreIndex
import logging
import sys

load_dotenv()

def main(url: str)->None:
    documents = SimpleDirectoryReader(url).load_data()
    index = VectorStoreIndex.from_documents(documents)
    query_engine = index.as_query_engine()
    response = query_engine.query("What did the artical say about artificial intelligence?")
    print(response)

if __name__ == '__main__':
    main(url=r"C:\Users\Kusum\Downloads\data")
