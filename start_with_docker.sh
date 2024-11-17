#!/bin/sh
docker run -d \
  -p 8501:8501 \
  -v $(pwd):/app \
  --name streamlit-app \
  --health-cmd="curl --fail http://localhost:8501/_stcore/health" \
  --health-interval=30s \
  --health-timeout=10s \
  --health-retries=3 \
  --entrypoint streamlit \
  $(docker build -q .) \
  run 1_🏡_Home.py --server.port=8501 --server.address=0.0.0.0