# pages/01_💬_Simple_Chat.py
import streamlit as st
from config.config import settings
from openai import OpenAI
from utils.icon import page_icon

st.set_page_config(
    page_title=settings.APP_NAME,
    page_icon="💬",
    layout="wide",
    initial_sidebar_state="expanded",
)


page_icon("💬")
st.subheader("Simple Chat", divider="red", anchor=False)

client = OpenAI(
    base_url=settings.OPENAI_API_URL,
    api_key=settings.OPENAI_API_KEY,  # required, but unused
)

message_container = st.container(height=300, border=True)

if st.session_state.selected_model is None:
    st.switch_page("pages/09_⚙️_Settings.py")
        
for message in st.session_state.messages:
    avatar = "🦔" if message["role"] == "assistant" else "😎"
    with message_container.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

if prompt := st.chat_input("Enter a prompt here..."):
    try:
        st.session_state.messages.append(
            {"role": "user", "content": prompt})

        message_container.chat_message("user", avatar="😎").markdown(prompt)

        with message_container.chat_message("assistant", avatar="🦔"):
            with st.spinner("model working..."):
                stream = client.chat.completions.create(
                    model=st.session_state.selected_model,
                    messages=[
                        {"role": m["role"], "content": m["content"]}
                        for m in st.session_state.messages
                    ],
                    stream=True,
                )
            # stream response
            response = st.write_stream(stream)
        st.session_state.messages.append(
            {"role": "assistant", "content": response})

    except Exception as e:
        st.error(e, icon="⛔️")

