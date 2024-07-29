#!/bin/bash

git clone https://github.com/open-webui/open-webui.git
pushd open-webui
git checkout -b v0.3.10 v0.3.10
git apply --3way ../patch/rag-main-py.patch
popd

docker compose build open-webui
