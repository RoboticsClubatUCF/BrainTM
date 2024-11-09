from gtts import gTTS

LANGUAGE = "en"

def ttsGenerate(textStr):
    ttsObj = gTTS(text = textStr, lang = LANGUAGE, slow= False)
    ttsObj.save("tempFile.mp3")

print("Enter Text to Generate")

textToGen = input()

ttsGenerate(textToGen)



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