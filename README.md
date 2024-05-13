<h1 align="center">Ampere Llama Chat based on Ollama</h1>

## Download the demo repository
```shell
$ git clone https://github.com/AmpereComputingAI/ampere-ai-llama-chat.git
$ cd ampere-ai-llama-chat
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
 ✔ Container ollama-server  Started                  0.3s 
 ✔ Container open-webui     Started                  0.4s
```

```docker
$ docker ps
CONTAINER ID   IMAGE                                           COMMAND              CREATED         STATUS              PORTS     NAMES
19e4d8f91988   ghcr.io/open-webui/open-webui:0.1.124           "bash start.sh"      2 minutes ago   Up About a minute             open-webui
dbb922f9b72c   ghcr.io/amperecomputingai/ollama-ampere:0.0.1   "bin/ollama serve"   2 minutes ago   Up About a minute             ollama-server
```

Open the Chrome browser and type in the following URL.
```
http://<server-IP>:3000
```

## Use the application
Please follow this [documentation](https://docs.openwebui.com) on how to use the application  

![Open WebUI](https://docs.openwebui.com/assets/images/demo-6793d95448aa180bca8dafbd21aa91b5.gif)


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
