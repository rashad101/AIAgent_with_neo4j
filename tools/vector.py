import streamlit as st
from llm import llm, embedding
from graph import graph
from langchain_community.vectorstores.neo4j_vector import Neo4jVector
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain

# Create the Neo4jVector
neo4jvector = Neo4jVector.from_existing_index(
    embedding,                               # (1)
    graph=graph,                             # (2)
    index_name="moviePlots",                 # (3)
    node_label="Movie",                      # (4)
    text_node_property="plot",               # (5)
    embedding_node_property="plotEmbedding", # (6)
    retrieval_query="""
                    RETURN
                        node.plot AS text,
                        score,
                        {
                            title: node.title,
                            directors: [ (person)-[:DIRECTED]->(node) | person.name ],
                            actors: [ (person)-[r:ACTED_IN]->(node) | [person.name, r.role] ],
                            tmdbId: node.tmdbId,
                            source: 'https://www.themoviedb.org/movie/'+ node.tmdbId
                        } AS metadata
                    """
)
# Create the retriever
retriever = neo4jvector.as_retriever()

# Create the prompt
instructions = (
    "Use the given context to answer the question."
    "If you don't know the answer, say you don't know."
    "Context: {context}"
)
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", instructions),
        ("human", "{input}")
    ]
)

# Create the chain
question_answer_chain = create_stuff_documents_chain(llm,prompt)
plot_retriever = create_retrieval_chain(
    retriever,
    question_answer_chain
)

# Create a function to call the chain
def get_movie_plot(user_input):
    return plot_retriever.invoke({"input": user_input})