#!/bin/bash

git clone https://github.com/open-webui/open-webui.git
pushd open-webui
git checkout -b v0.1.124 v0.1.124
git apply --3way ../patch/rag-main-py.patch
popd

docker compose build open-webui
