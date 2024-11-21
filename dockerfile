FROM ubuntu:18.04

WORKDIR /tmp

COPY ./entrypoint.sh /tmp/entrypoint.sh

EXPOSE 11434

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y curl wget nano vim
RUN curl -fsSL https://ollama.com/install.sh | sh
RUN chmod +x entrypoint.sh 

CMD ["bash"]


## USE THIS TO BOOT IN BASH    " docker run -it --rm -p 11434:11434 tp_llm "
##docker run -d --gpus=all -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
