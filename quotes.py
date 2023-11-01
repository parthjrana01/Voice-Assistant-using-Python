import pyttsx3 # text to speech conversion
import speech_recognition as sr # recognize speech input
import random 

# from gui import play_gif
# play_gif()

engine=pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)

vID=1
vName="siri"
engine.setProperty('voice',voices[vID].id)


def speak(audio):
    print(audio,"\n")
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    #takes microphone input from user

    r=sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        r.energy_threshold=700 #we have to speak loudly so that background voice can be ignored by AI (byDefault=300)
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said : {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    
    return query

def get_quotes(id,name):

    vID=id
    vName=name
    engine.setProperty('voice',voices[vID].id)

    fp = open("good_quotes.txt","r")
    content = fp.read()
    quote = content.split("\n")
    r = random.randint(0,len(quote))
    speak(quote[r])

    

