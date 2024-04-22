#!/bin/bash

./download-model.sh

repo_dir=`basename $REPO_URL .tar.gz`
model_file=`basename $MODEL_URL`

$repo_dir/server \
    -m $model_file \
    -c 2048 -t 64 -np 4 \
    --port $SERVER_PORT
