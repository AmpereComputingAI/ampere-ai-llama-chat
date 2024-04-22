<h1 align="center">Llama.cpp + HF Chat UI based LLM Chat application</h1>

## Download the demo repository
```shell
$ git clone https://github.com/AmpereComputingAI/ampere-ai-llama-chat.git
$ cd ampere-ai-llama-chat
```

## Install docker
Follow the instructions from this link,
https://docs.docker.com/engine/install/ubuntu/

## Install compose plugin
Follow the instructions from this link,
https://docs.docker.com/compose/install/linux/#install-using-the-repository

## Open the required ports
```shell
$ sudo firewall-cmd --zone public --permanent --add-port 8008/tcp
$ sudo firewall-cmd --reload
```

## Start the demo
Run the following script to start the demo

```shell
$ ./start-app.sh
```

```docker
$ docker ps
CONTAINER ID   IMAGE                                                          COMMAND                  CREATED         STATUS         PORTS          NAMES
ec1bfe344ae4   ghcr.io/amperecomputingai/ampere-ai-llama-chat:client-0.0.1    "docker-entrypoint.s…"   2 minutes ago   Up 2 minutes        ampere-ai-llama-chat-client-1
dadf53b9e93c   ghcr.io/amperecomputingai/ampere-ai-llama-chat:api-app-0.0.1   "./start-api.sh"         2 minutes ago   Up 2 minutes        ampere-ai-llama-chat-api-app-1
7410d371ee40   mongo:latest                                                   "docker-entrypoint.s…"   2 minutes ago   Up 2 minutes        ampere-ai-llama-chat-db-1
7a20d77223f6   ghcr.io/amperecomputingai/ampere-ai-llama-chat:server-0.0.1    "./start-server.sh"      2 minutes ago   Up 2 minutes        ampere-ai-llama-chat-server-1
```

Open the Chrome browser and type in the following URL.
```
http://<server-IP>:3000
```

## Stop the demo
Run the following script to stop the demo
```shell
$ ./stop-app.sh
[+] Running 4/4
 ✔ Container ampere-ai-llama-chat-client-1   Remove...                                           0.0s
 ✔ Container ampere-ai-llama-chat-server-1   Remove...                                           0.0s
 ✔ Container ampere-ai-llama-chat-api-app-1  Remov...                                            0.0s
 ✔ Container ampere-ai-llama-chat-db-1       Removed                                             0.0s
```


## Developers
#### Build the application
This command will build the application
```shell
$ ./build.sh
[+] Building 3.1s (33/33) FINISHED                                                                                 docker:default
 => [server internal] load .dockerignore                                                                           0.0s
 => => transferring context: 2B                                                                                    0.0s
 => [server internal] load build definition from Dockerfile                                                        0.0s
 => => transferring dockerfile: 741B                                                                               0.0s
 => [client] resolve image config for docker.io/docker/dockerfile:latest                                           1.2s
 => [api-app internal] load .dockerignore                                                                          0.0s
 => => transferring context: 2B                                                                                    0.0s
 => [api-app internal] load build definition from Dockerfile                                                       0.0s
 => => transferring dockerfile: 282B                                                                               0.0s
 => CACHED [client] docker-image://docker.io/docker/dockerfile@sha256:dbbd5e059e8a07ff7ea6233b213b36aa516b4c53c64  0.0s
 => [server internal] load metadata for docker.io/library/ubuntu:22.04                                             0.6s
 => [api-app internal] load metadata for docker.io/library/python:3.10-slim                                        0.6s
 => [server stage-0 1/5] FROM docker.io/library/ubuntu:22.04@sha256:1b8d8ff4777f36f19bfe73ee4df61e3a0b789caeff29c  0.0s
 => [server internal] load build context                                                                           0.0s
 => => transferring context: 111B                                                                                  0.0s
 => CACHED [server stage-0 2/5] WORKDIR /workspace/llama                                                           0.0s
 => CACHED [server stage-0 3/5] COPY download-llama.sh download-model.sh start-server.sh ./                        0.0s
 => CACHED [server stage-0 4/5] RUN --mount=type=cache,id=apt-cache,target=/var/cache/apt,sharing=locked           0.0s
 => CACHED [server stage-0 5/5] RUN ./download-llama.sh                                                            0.0s
 => [server] exporting to image                                                                                    0.0s
 => => exporting layers                                                                                            0.0s
 => => writing image sha256:f5a499664d3861aa8a6187e3f4b2efb63ef33a51b201e8d345033c4dde36a33a                       0.0s
 => => naming to ghcr.io/amperecomputingai/ampere-ai-llama-chat:server-0.0.1                                       0.0s
 => [api-app stage-0 1/5] FROM docker.io/library/python:3.10-slim@sha256:64157e9ca781b9d18e4d7e613f4a3f19365a26d8  0.0s
 => [api-app internal] load build context                                                                          0.0s
 => => transferring context: 129B                                                                                  0.0s
 => CACHED [api-app stage-0 2/5] WORKDIR /api                                                                      0.0s
 => CACHED [api-app stage-0 3/5] COPY requirements.txt .                                                           0.0s
 => CACHED [api-app stage-0 4/5] RUN --mount=type=cache,target=/root/.cache/pip  pip install -r requirements.txt   0.0s
 => CACHED [api-app stage-0 5/5] COPY api_main.py start-api.sh Dockerfile .                                        0.0s
 => [api-app] exporting to image                                                                                   0.0s
 => => exporting layers                                                                                            0.0s
 => => writing image sha256:087ef3b9d0c728866428147439dbf10f8078e7e828ce6dfba3f0905fd26f34b7                       0.0s
 => => naming to ghcr.io/amperecomputingai/ampere-ai-llama-chat:api-app-0.0.1                                      0.0s
 => [client internal] load .dockerignore                                                                           0.0s
 => => transferring context: 2B                                                                                    0.0s
 => [client internal] load build definition from Dockerfile                                                        0.0s
 => => transferring dockerfile: 792B                                                                               0.0s
 => [client internal] load metadata for docker.io/library/node:20-slim                                             0.6s
 => [client stage-0 1/6] FROM docker.io/library/node:20-slim@sha256:9f938a1eeb3f85ca7691e1b4b5e9ab91e1d2efa7afc1d  0.0s
 => [client internal] load build context                                                                           0.0s
 => => transferring context: 100B                                                                                  0.0s
 => CACHED [client stage-0 2/6] WORKDIR /app                                                                       0.0s
 => CACHED [client stage-0 3/6] RUN --mount=type=cache,id=apt-cache,target=/var/cache/apt,sharing=locked           0.0s
 => CACHED [client stage-0 4/6] COPY --chown=1000 build-chatui.sh start-client.sh ./                               0.0s
 => CACHED [client stage-0 5/6] COPY --chown=1000 env.local ./.env.local                                           0.0s
 => CACHED [client stage-0 6/6] RUN ./build-chatui.sh                                                              0.0s
 => [client] exporting to image                                                                                    0.0s
 => => exporting layers                                                                                            0.0s
 => => writing image sha256:7100da2a9eb9a43902ef8c2d8df42a3f5749c3ff365ca0d888f9ea3a43b6beae                       0.0s
 => => naming to ghcr.io/amperecomputingai/ampere-ai-llama-chat:client-0.0.1                                       0.0s
```

## References
https://github.com/ggerganov/llama.cpp  
https://github.com/huggingface/chat-ui
