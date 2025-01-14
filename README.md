<h1 align="center">Ampere Llama Chat based on Ollama</h1>

## Download the demo repository
```shell
$ git clone https://github.com/AmpereComputingAI/ampere-ai-llama-chat.git
$ cd ampere-ai-llama-chat
$ git checkout 0.0.8 -b 0.0.8
```

## Install docker and compose
Follow the instructions from this link,  
https://docs.docker.com/engine/install/ubuntu/  
https://docs.docker.com/compose/install/linux/#install-using-the-repository

## Open the required ports
```shell
$ sudo firewall-cmd --zone public --permanent --add-port 8080/tcp
$ sudo firewall-cmd --zone public --permanent --add-port 11434/tcp
$ sudo firewall-cmd --reload
```

## Start the demo
Run the following script to start the demo

```shell
$ ./start-app.sh
 [+] Running 2/2
 ✔ Container ollama-server  Started                  0.2s 
 ✔ Container open-webui     Started                  0.2s
```

```docker
$ docker ps
CONTAINER ID   IMAGE                                               COMMAND              CREATED         STATUS                            PORTS     NAMES
c4c292349d2a   ghcr.io/open-webui/open-webui:v0.4.7                "bash start.sh"      6 seconds ago   Up 5 seconds (health: starting)             open-webui
54515ff4ab15   ghcr.io/amperecomputingai/ollama-ampere:0.0.6-ol9   "bin/ollama serve"   6 seconds ago   Up 5 seconds                                ollama-server
```

Open the Chrome browser and type in the following URL.
```
http://<server-IP>:8080
```

## Use the application using UI
Follow this [documentation](https://docs.openwebui.com) on how to use the application

![Open WebUI](https://github.com/open-webui/open-webui/blob/4269df041fef62208d59babe0faae866d2bfbc3c/demo.gif)

## Use the application using APIs/command line
Follow this [documentation](api-endpoints.MD) on how to use the application


## Stop the demo
Run the following script to stop the demo
```shell
$ ./stop-app.sh 
[+] Running 2/2
 ✔ Container open-webui     Removed               3.1s 
 ✔ Container ollama-server  Removed               0.1s
```

## References
https://github.com/open-webui/open-webui.git
https://github.com/ggerganov/llama.cpp  
https://github.com/ollama/ollama.git
