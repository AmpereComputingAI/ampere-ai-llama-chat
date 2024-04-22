#!/bin/bash

# Download, patch and build chat-ui

echo "REPO_URL: $REPO_URL"
repo_dir=`basename $REPO_URL .git`
export GIT_SSL_NO_VERIFY=true

tmpdir="tmp"
git clone --depth 1 $REPO_URL $tmpdir
rsync -a $tmpdir/ .
rm -rf $tmpdir

npm set cache /app/.npm
npm ci 
npm run build 
