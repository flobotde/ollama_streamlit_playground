# config/config.py
import os
import streamlit as st
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    
    model_config = SettingsConfigDict(
        # Use top level .env file (one level above ./config/)
        env_file=os.path.abspath(os.path.join(os.path.dirname(__file__), "../.env")),
        env_ignore_empty=True,
        extra="ignore",
    )
    
    APP_NAME: str
    OPENAI_API_URL: str
    OPENAI_API_KEY: str # required, but unused
    
    # Init Session vars
    if "selected_model" not in st.session_state:
        st.session_state.selected_model = None
    else:
        st.session_state["selected_model"] = st.session_state.selected_model
    if "messages" not in st.session_state:
        st.session_state.messages = []
    else:
        st.session_state["messages"] = st.session_state.messages
    if "crew_messages" not in st.session_state:
        st.session_state.crew_messages = []
    else:
        st.session_state["crew_messages"] = st.session_state.crew_messages
    if "chats" not in st.session_state:
        st.session_state.chats = []
    else:
        st.session_state["chats"] = st.session_state.chats
    if "uploaded_file_state" not in st.session_state:
        st.session_state.uploaded_file_state = None
    else:
        st.session_state["uploaded_file_state"] = st.session_state.uploaded_file_state
    
settings = Settings()  # type: ignore