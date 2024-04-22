#!/bin/bash

echo "MODEL_URL: $MODEL_URL"
echo "REPO_URL: $REPO_URL"
echo "SERVER_PORT: $SERVER_PORT"

repo_file=`basename $REPO_URL`
repo_dir=`basename $REPO_URL .tar.gz`

if [ ! -d $repo_dir ]; then
    echo "Downloading llama: $repo_file"
    wget --no-check-certificate -qO- $REPO_URL | tar xz
fi
