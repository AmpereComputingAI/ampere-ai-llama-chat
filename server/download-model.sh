#!/bin/bash

model_file=`basename $MODEL_URL`

if [ ! -f $model_file ]; then
    echo "Downloading model: $model_file"
    echo $MODEL_URL | tr -d '"' | xargs wget --no-check-certificate -
fi
