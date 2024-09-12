# This is server code to send video and audio frames over TCP

import socket
import threading, wave, pyaudio,pickle,struct


host_name = socket.gethostname()
host_ip =socket.gethostbyname(host_name)
print(host_ip)
port = 9611
CHUNK = 1024
WAVE_FILE = 'grpcTest/Warrenty.wav'

##This will load the audio file
wf=wave.open(WAVE_FILE,'rb')
p = pyaudio.PyAudio()

stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True
                )
audio_data=wf.readframes(CHUNK)

client_socket=None

def serverStart():
    global client_socket
    server_socket=socket.socket()
    server_socket.bind((host_ip,(port-1)))
    server_socket.listen(5)
    print("Server listening at ",host_ip,(port-1))
    client_socket,addr = server_socket.accept()
    print("Client has connect at ",addr)



def on_input_press():
    global client_socket
    print("Input detected")
    if client_socket:
        wf.setpos(0)
        while True:
            data = wf.readframes(CHUNK)
            if not data:
                break
            a = pickle.dumps(data)
            message = struct.pack("Q",len(a)) + a
            client_socket.sendall(message)

server_thread=threading.Thread(target=serverStart)
server_thread.start()
while True:
    print("")
    user_input=input("Press enter to send audio or 'q' to quit: ")
    if user_input.lower()=='q':
        break
    on_input_press()

