# OLLAMA Streamlit playground (ext)

This is a fork of the idea from ☕️ [Ollama x Streamlit Playground](https://github.com/tonykipkemboi/ollama_streamlit_demos)

I changed a bit the structure for my first experiments with CrewAI.

## Prerequisites

* Have an local ollama up and running on your system http://localhost:11434/
* python, pip
* (optional) docker 

## Technology Stack and Features
- 💬 [Ollama](https://ollama.com/) as AI model Server 
- 🚀 [CrewAI](https://https://crewai.com/) for AI Crew Example. (s. utils/crew.py and config/agents.yml und tasks.yml to change)
- 🪟 [Streamlit](https://https://streamlit.io/) for the frontend.
- 🐋 [Docker](https://www.docker.com) for running in a container

## Install

- Clone the repo

```bash
git clone https://github.com/flobotde/ollama_streamlit_playground.git
```

- change dir 

```bash
cd ollama_streamlit_playground/
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
streamlit run 1_🏡_Home.py
```

Visit http://localhost:8501/ (if it doesn't open on it's own)

## Run with docker

-TBDoc

## Known Bugs

- Often see AttributeError: st.session_state has no attribute "selected_model", but it works with a little patience
- Docker with a running ollama on mac not working a.t.m.