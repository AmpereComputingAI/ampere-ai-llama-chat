# syntax=docker/dockerfile
FROM ubuntu:22.04
ARG DEBIAN_FRONTEND=noninteractive
ARG REPO_URL
ENV REPO_URL=${REPO_URL}
ENV MODEL_URL=${MODEL_URL}
ENV SERVER_PORT=${SERVER_PORT}
SHELL ["/bin/bash", "-c"]

WORKDIR /workspace/llama

COPY download-llama.sh download-model.sh start-server.sh ./

RUN --mount=type=cache,id=apt-cache,target=/var/cache/apt,sharing=locked \
    --mount=type=cache,id=apt-lib,target=/var/lib/apt,sharing=locked \
    --mount=type=cache,id=debconf,target=/var/cache/debconf,sharing=locked \
    set -exu && \
    apt-get update -qq && \
    DEBIAN_FRONTEND=noninteractive \
    apt-get -y install -y -qq --no-install-recommends \
        libnuma-dev wget

RUN ./download-llama.sh
