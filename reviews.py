# This file will use most of the code from What2eat.ipynb to get reviews data

import pandas as pd
from langchain_huggingface import HuggingFaceEndpointEmbeddings
from langchain_chroma import Chroma
from dotenv import dotenv_values, load_dotenv
load_dotenv() # Load environment variables
dotenv_values()


Hf_embeddings = HuggingFaceEndpointEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2",task="feature-extraction")

review_vectorstore = Chroma(
    persist_directory="embeddings",
    collection_name="restaurant_reviews1",
    embedding_function=Hf_embeddings
)


query = "food to have on a date night"

results = review_vectorstore.similarity_search(query, k=5)
print("  wekj",results)
for idx, doc in enumerate(results, 1):
    print(f"\nResult {idx}:")
    print("Review:", doc.page_content)
    print("Metadata:", doc.metadata)