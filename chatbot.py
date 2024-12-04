import streamlit as st
from aiagent import generate_response

# Page Config
st.set_page_config("AI Agent", page_icon=":movie_camera:")
# tag::write_message[]


# Set up Session State
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi, I'm your personal AI Agent!  How can I help you?"},
    ]

# Submit handler
def handle_submit(message):
    """
    Submit handler:

    You will modify this method to talk with an LLM and provide
    context using data from Neo4j.
    """

    # Handle the response
    with st.spinner('Thinking...'):
        response = generate_response(message)
        from time import sleep
        sleep(1)
        write_message('assistant', response)

def write_message(role, content, save = True):
    """
    This is a helper function that saves a message to the
     session state and then writes a message to the UI
    """
    # Append to session state
    if save:
        st.session_state.messages.append({"role": role, "content": content})

    # Write to UI
    with st.chat_message(role):
        st.markdown(content)
# end::write_message[]

# # Display messages in Session State
for message in st.session_state.messages:
     write_message(message['role'], message['content'], save=False)
#
# # Handle any user input
if question := st.chat_input("Type your question here?"):
    # Display user message in chat message container
    write_message('user', question)

    # Generate a response
    handle_submit(question)


