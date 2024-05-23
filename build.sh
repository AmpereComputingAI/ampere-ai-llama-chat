#!/bin/bash

git clone https://github.com/open-webui/open-webui.git
pushd open-webui
git checkout -b v0.1.124 v0.1.124
popd

docker compose build open-webui
