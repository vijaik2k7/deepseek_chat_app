import streamlit as st
import ollama

st.title("DeepSeek R1 Chatbot (Local Ollama)")

# Initialize chat history in session state if it doesn't exist
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What's up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get response from Ollama/DeepSeek R1
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        for response in ollama.chat(model='deepseek-r1:1.5B', messages=[
            {'role': 'user', 'content': prompt},
        ], stream=True):
            full_response += response['message']['content']
            message_placeholder.markdown(full_response + "▌") # Typing effect
        message_placeholder.markdown(full_response) # Final response

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})