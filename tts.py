import pyttsx3 as tts
from LLM import textGeneration
##import pygame
import os
import time
#I chose sapi5 because it can be generated offline
ttsEngine = tts.init(driverName='sapi5')

##pygame.mixer.init()

while(True):
    print("Please enter prompt")
    textToGen = input()
    generatedText = textGeneration(textToGen)
    print("this is the response\n" + generatedText['message']['content'])
    ttsEngine.save_to_file(text=generatedText['message']['content'],filename="tempfile.mp3")
    ttsEngine.runAndWait()
    if ttsEngine.isBusy():
        time.sleep(1)
    
    
""" 
    pygame.mixer.music.load("tempfile.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(1)
    pygame.mixer.music.stop()
    pygame.mixer.music.unload()

    if os.path.exists("tempfile.mp3"):
        os.remove("tempfile.mp3")
    else:
        print("file not found")

"""

#The below script is for playing the audio on the system

"""
text = "Hello world, I am a tts test"

ttsObj = gTTS(text=text,lang = 'en', slow=False)

ttsObj.save("test.mp3")

pygame.mixer.init()
pygame.mixer.music.load("test.mp3")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    time.sleep(1)
pygame.mixer.music.stop()
pygame.mixer.music.unload()


if os.path.exists("test.mp3"):
    os.remove("test.mp3")
else:
    print("The file doesnt exsit")

"""