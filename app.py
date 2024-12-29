import streamlit as st
from openai import OpenAI
import os
# Fetch the API key from Streamlit secrets
api_key = st.secrets['secrets']["OPENAI_API_KEY"]


# Initialize OpenAI client with the secret key
client = OpenAI(api_key=api_key)

st.set_page_config(page_title="My GPT Chat", page_icon="🤖")

# Display your logo
st.image("/Users/ha/Documents/Crewai/GbGPT/gbk_logo.svg", width=150)  # Adjust width as needed

st.title("Gulf Bank GPT")

# Initialize the session state for message history
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

user_input = st.text_input("Your message:", value="")

if st.button("Send"):
    if user_input.strip():
        # Add user message
        st.session_state["messages"].append({"role": "user", "content": user_input})

        # Call the model
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=st.session_state["messages"]
        )
        assistant_reply = response.choices[0].message.content
        st.session_state["messages"].append({"role": "assistant", "content": assistant_reply})

# Now we display messages *after* potentially adding new ones
for msg in st.session_state["messages"]:
    if msg["role"] == "user":
        st.markdown(f"**User:** {msg['content']}")
    elif msg["role"] == "assistant":
        st.markdown(f"**Assistant:** {msg['content']}")
