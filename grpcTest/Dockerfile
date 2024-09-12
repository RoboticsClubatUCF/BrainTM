FROM ubuntu:latest
WORKDIR /app
RUN apt-get update &&\
    apt-get install -y pulseaudio
RUN apt-get update && apt-get install -y alsa-utils mpg123
RUN apt-get update && apt-get install -y \
    python3.8 \
    python3-pip \
    && apt-get clean
RUN apt-get update
RUN apt-get install -y libasound-dev libportaudio2 libportaudiocpp0 portaudio19-dev
RUN pip install pyaudio --break-system-packages
COPY client.py /app/client.py
CMD ["python3", "/app/client.py"]
