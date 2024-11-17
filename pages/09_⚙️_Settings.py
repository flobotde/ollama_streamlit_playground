import ollama
import streamlit as st
from utils.icon import page_icon

st.set_page_config(
    page_title="Settings",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="expanded",
)

def extract_model_names(models_info: list) -> tuple:
    """
    Extracts the model names from the models information.

    :param models_info: A dictionary containing the models' information.

    Return:
        A tuple containing the model names.
    """

    return tuple(model["name"] for model in models_info["models"])


page_icon("⚙️")
st.subheader("Model Management", divider="red", anchor=False)

# Select Model section
st.subheader("Set Model", anchor=False)
models_info = ollama.list()
available_models = extract_model_names(models_info)

if available_models:
    if st.session_state.selected_model is not None:
        index = available_models.index(st.session_state.selected_model)
    else:
        index = 0
        st.warning("You have not sellected any model from Ollama yet!", icon="⚠️")

    selected_model = st.selectbox(
        "Pick a model available locally on your system ↓", available_models, index=index
    )
    st.write("You selected:", selected_model)
    st.session_state.selected_model = selected_model

# Download Model section
st.subheader("Download Models", anchor=False)
model_name = st.text_input(
    "Enter the name of the model to download ↓", placeholder="mistral"
)
if st.button(f"📥 :green[**Download**] :red[{model_name}]"):
    if model_name:
        try:
            ollama.pull(model_name)
            st.success(f"Downloaded model: {model_name}", icon="🎉")
            st.balloons()
            sleep(1)
            st.rerun()
        except Exception as e:
            st.error(
                f"""Failed to download model: {
                model_name}. Error: {str(e)}""",
                icon="😳",
            )
    else:
        st.warning("Please enter a model name.", icon="⚠️")

st.divider()

# Create model section
st.subheader("Create model", anchor=False)
modelfile = st.text_area(
    "Enter the modelfile",
    height=100,
    placeholder="""FROM mistral
SYSTEM You are mario from super mario bros.""",
)
model_name = st.text_input(
    "Enter the name of the model to create", placeholder="mario"
)
if st.button(f"🆕 Create Model {model_name}"):
    if model_name and modelfile:
        try:
            ollama.create(model=model_name, modelfile=modelfile)
            st.success(f"Created model: {model_name}", icon="✅")
            st.balloons()
            sleep(1)
            st.rerun()
        except Exception as e:
            st.error(
                f"""Failed to create model: {
                model_name}. Error: {str(e)}""",
                icon="😳",
            )
    else:
        st.warning("Please enter a **model name** and **modelfile**", icon="⚠️")

st.divider()

# Delete Model Section
st.subheader("Delete Models", anchor=False)
models_info = ollama.list()
available_models = [m["name"] for m in models_info["models"]]

if available_models:
    selected_models = st.multiselect("Select models to delete", available_models)
    if st.button("🗑️ :red[**Delete Selected Model(s)**]"):
        for model in selected_models:
            try:
                ollama.delete(model)
                st.success(f"Deleted model: {model}", icon="🎉")
                st.balloons()
                sleep(1)
                st.rerun()
            except Exception as e:
                st.error(
                    f"""Failed to delete model: {
                    model}. Error: {str(e)}""",
                    icon="😳",
                )
else:
    st.info("No models available for deletion.", icon="🦗")

