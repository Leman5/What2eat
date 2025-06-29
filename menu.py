#this file will use most of the code from menu.ipynb to get menu and weather data
import pandas as pd
from langchain.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEndpointEmbeddings
from questionnaire import get_user_inputs
from dotenv import dotenv_values, load_dotenv

load_dotenv() 
dotenv_values() 

def get_menu():

    user_profile = get_user_inputs()

    Hf_embeddings = HuggingFaceEndpointEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2", task="feature-extraction")
    menu_vectorstore = Chroma(
        persist_directory="embeddings",
        collection_name="menu_items",
        embedding_function=Hf_embeddings
    )
    query="{}, {}, {}, {}".format(
            user_profile["meal"], user_profile["mood"], user_profile["spice"], user_profile["diet"]
        )
    results = menu_vectorstore.max_marginal_relevance_search_by_vector(
        embedding=Hf_embeddings.embed_query(query),
        k=20,
    )
    print(len(results))
    return results








