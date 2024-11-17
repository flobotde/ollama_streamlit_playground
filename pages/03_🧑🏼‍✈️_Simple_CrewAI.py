import sys
import streamlit as st
from config.config import settings
from utils.crew import ResearcherCrew, StreamToExpander
from utils.icon import page_icon

st.set_page_config(
    page_title=settings.APP_NAME,
    page_icon="🧑🏼‍✈️",
    layout="wide",
    initial_sidebar_state="expanded",
)

page_icon("🧑🏼‍✈️")
st.subheader("Simple Researcher & Summarizer Agent Crew", divider="red", anchor=False)

message_container = st.container(height=300, border=True)

if st.session_state.selected_model is None:
    st.switch_page("pages/09_⚙️_Settings.py")
        
for crew_message in st.session_state.crew_messages:
    avatar = "🧑🏼‍✈️" if crew_message["role"] == "assistant" else "😎"
    with message_container.chat_message(crew_message["role"], avatar=avatar):
        st.markdown(crew_message["content"])

if prompt := st.chat_input("Enter a prompt here..."):
    try:
        st.session_state.crew_messages.append(
            {"role": "user", "content": prompt})

        message_container.chat_message("user", avatar="😎").markdown(prompt)

        with message_container.chat_message("assistant", avatar="🦔"):
            with st.spinner("model working..."):
                inputs = {'topic': prompt,}
                sys.stdout = StreamToExpander(st)
                crew = ResearcherCrew(topic=prompt)
                crew_result = crew.crew().kickoff(inputs=inputs)
                
            st.success("Research Done!", icon="✌🏼")

        st.session_state.crew_messages.append(
            {"role": "assistant", "content": crew_result})

    except Exception as e:
        st.error(e, icon="⛔️")
 
