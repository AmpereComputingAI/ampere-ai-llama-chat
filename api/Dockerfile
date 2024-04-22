# syntax=docker/dockerfile
FROM python:3.10-slim
SHELL ["/bin/bash", "-c"]

WORKDIR /api

COPY requirements.txt .
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.txt

COPY api_main.py start-api.sh Dockerfile .
