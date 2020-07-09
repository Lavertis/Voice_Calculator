from gtts import gTTS
from speech_recognition import *
from playsound import playsound

try:
    r = Recognizer()
    with Microphone() as src:
        r.adjust_for_ambient_noise(src)
except IOError:
    print('No microphone detected, exiting')
    exit(0)


def listen():
    with Microphone() as source:
        print('Speak now')
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language='pl-PL')
        debug(text)
        return text.lower()
    except UnknownValueError:
        return 'Nie usłyszałem polecenia'


temp_path = os.getenv('LOCALAPPDATA') + '\\Temp\\tts.mp3'


def say(text):
    tts = gTTS(text=text, lang='pl')
    tts.save(temp_path)
    playsound(temp_path)
    os.remove(temp_path)


def debug(user_input):
    print('User: ' + user_input)
