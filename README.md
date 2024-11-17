# OLLAMA Streamlit playground (ext)

This is a fork of the idea from ☕️ [Ollama x Streamlit Playground](https://github.com/tonykipkemboi/ollama_streamlit_demos)
Changed a bit the structure for first experiments with CrewAI.

## Prerequisites

* Have an local ollama up and running on your system http://localhost:11434/
* python, pip
* (optional) docker 

## Technology Stack and Features
- 🚀 [CrewAI](https://https://crewai.com/) for AI.
- 🪟 [Streamlit](https://https://streamlit.io/) for the frontend.
- 🐋 [Docker](https://www.docker.com) for running in a container

## Install

- Clone the repo

```bash
git clone __TODO__
```

- change dir 

```bash
cd igl-po-vision/
```

- install requirements

```bash
pip install -r requirements.txt
```
## Copy example.env to .env and edit

```bash
cp example.env .env
```

## Run

```bash
streamlit run Home.py
```

Visit http://localhost:8501/ (if it doesn't open on it's own)

## Run with docker

-TBD

## Known Bugs

- Often see AttributeError: st.session_state has no attribute "selected_model", but it works with a little patience