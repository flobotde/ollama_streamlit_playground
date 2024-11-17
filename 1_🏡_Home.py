import streamlit as st
from utils.icon import page_icon
from config.config import settings

st.set_page_config(
    page_title=settings.APP_NAME,
    page_icon="🏡",
    layout="wide",
    initial_sidebar_state="expanded",
)

page_icon("🏡")
st.title("🏡 Herzlich Willkommen!")
st.subheader("Willkommen bei " + settings.APP_NAME)

# switch to settings tab, if model is not selected yet
if st.session_state.selected_model is None:
    st.switch_page("pages/09_⚙️_Settings.py")

# Page Content
st.write("""
Schön, dass Sie hier sind! Diese Seite ist der Startpunkt für unsere Anwendung.
Fühlen Sie sich wie zu Hause und erkunden Sie die verschiedenen Funktionen, die wir anbieten.
""")

try:
    # Hier können Sie weiteren Code hinzufügen
    pass
except Exception as e:
    st.error(f"Ein Fehler ist aufgetreten: {e}", icon="⛔️")
