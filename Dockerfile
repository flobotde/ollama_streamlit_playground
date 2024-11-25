FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://0.0.0.0:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "1_🏡_Home.py", "--server.port=8501", "--server.address=0.0.0.0"]