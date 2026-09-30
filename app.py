import streamlit as st

# Page settings
st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖"
)

# Title
st.title("🤖 AI Chatbot")
st.write("Simple AI chatbot using Streamlit")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])


# Chat input
user_input = st.chat_input("Type your message here...")

if user_input:

    # Display user message
    with st.chat_message("user"):
        st.write(user_input)

    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # Simple chatbot response
    user_message = user_input.lower()

    if "hello" in user_message or "hi" in user_message:
        response = "Hello! 👋 How can I help you?"

    elif "name" in user_message:
        response = "I am your Streamlit AI chatbot."

    elif "how are you" in user_message:
        response = "I am doing great! 😊"

    elif "ai" in user_message:
        response = "AI means Artificial Intelligence. It helps computers perform tasks that normally require human intelligence."

    elif "bye" in user_message:
        response = "Goodbye! 👋 Have a great day!"

    else:
        response = "I received your message: " + user_input

    # Display chatbot response
    with st.chat_message("assistant"):
        st.write(response)

    # Save chatbot response
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })
