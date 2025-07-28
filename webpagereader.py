import os
from dotenv import load_dotenv
from llama_index.readers.web import SimpleWebPageReader
from llama_index.core import VectorStoreIndex

# Load environment variables from .env file
load_dotenv()

def main(url: str) -> None:
    # Load webpage
    documents = SimpleWebPageReader(html_to_text=True).load_data(urls=[url])

    # Create index
    index = VectorStoreIndex.from_documents(documents=documents)

    # Query the index
    query_engine = index.as_query_engine()
    response = query_engine.query("What is the history of generative AI?")

    # Print the result
    print(response)

if __name__ == "__main__":
    main("https://medium.com/@raja.gupta20/generative-ai-for-beginners-part-1-introduction-to-ai-eadb5a71f07d")
