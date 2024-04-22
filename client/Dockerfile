# syntax=docker/dockerfile
FROM node:20-slim
ARG REPO_URL
ENV REPO_URL=${REPO_URL}
SHELL ["/bin/bash", "-c"]

WORKDIR /app

RUN --mount=type=cache,id=apt-cache,target=/var/cache/apt,sharing=locked \
    --mount=type=cache,id=apt-lib,target=/var/lib/apt,sharing=locked \
    --mount=type=cache,id=debconf,target=/var/cache/debconf,sharing=locked \
    set -exu && \
    apt-get update -qq && \
    DEBIAN_FRONTEND=noninteractive \
    apt-get -y install -y -qq --no-install-recommends git gnupg curl rsync

COPY --chown=1000 build-chatui.sh start-client.sh ./
COPY --chown=1000 env.local ./.env.local
RUN ./build-chatui.sh

#RUN --mount=type=cache,target=/app/.npm \
#        pushd ${REPO_NAME} && \
#        npm set cache /app/.npm && \
#        npm ci
