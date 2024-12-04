import streamlit as st
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

# create the LLM endpoint
llm = ChatOpenAI(
    openai_api_key=st.secrets["OPENAI_API_KEY"],
    model=st.secrets["OPENAI_MODEL"]
)

# create the embedding model endpoint

embedding = OpenAIEmbeddings(
    openai_api_key=st.secrets["OPENAI_API_KEY"]
)