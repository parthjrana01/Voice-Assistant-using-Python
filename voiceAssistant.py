import pyttsx3 # text to speech conversion
import pywhatkit # youtube and whatsapp
import speech_recognition as sr # recognize speech input
import datetime # for knowing current time
import wikipedia # searching on wikipedia
import webbrowser # to open links on browsers
import os 
import random 
import smtplib #for email
import pyjokes # for telling random jokes

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

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=5 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good afternoon!")

    elif hour>=18 and hour<21:
        speak("Good evening!")

    else:
        speak("Good Night!")

    speak(f"I am {vName}. Your voice assistant. How may I help you?")

def Namakarana():
    speak("Hii I am your voice assistant")
    # speak("Which voice would you like: Enter 1 for Men or 2 for Women")
    speak("Which voice would you like: Men or Women")
    # print("Which voice would you like:-\n1 for Men\n2 for Women\nEnter your choice : ")
    # choice=int(input())

   
    ch = takeCommand().lower()
    while 'none' in ch:
        ch = takeCommand().lower()

    if 'women' in ch:
        vID=1
        engine.setProperty('voice',voices[vID].id)
    else:
        vID=0
        engine.setProperty('voice',voices[vID].id)

    speak("Please Give me a Name")
    # name=input("Give me a Name : ")
    # vName=name

    name=takeCommand()
    while 'None' in name:
        name=takeCommand()

    vName=name

    speak(f"I am {vName}. Your voice assistant. How may I help you?")
      

def sendEmail(to,content):
    fp = open('pwd.txt','r')
    pwd = fp.read()
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('21bce247@nirmauni.ac.in',pwd)
    server.sendmail('21bce247@nirmauni.ac.in',to,content)
    server.close()


if __name__ == "__main__":

    wishMe()
    # Namakarana()
    while True:
        query = takeCommand().lower()

        if 'how are you' in query:
            speak("I am fine! What about you")
        elif 'i am happy' in query or 'i am fine' in query:
            speak("Nice to hear! I am happy too.")
        elif 'i am sad' in query:
            from quotes import get_quotes
            get_quotes(vID,vName)
        elif 'thank you' in query:
            speak("your welcome!")

        # to execute user choice tasks
        if 'wikipedia' in query or 'search' in query:
            speak("Searching wikipedia...")
            # query=query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=1)
            speak("According to wikipedia")
            # print(results)
            speak(results)

        elif 'play' in query and 'youtube' in query:
            c = 'Opening youtube'
            speak(c)
            pywhatkit.playonyt(query)

        elif 'youtube' in query:
            c = 'Opening youtube'
            #speak(c)
            engine.say(c)
            engine.runAndWait()
            webbrowser.open("youtube.com")

        elif 'google' in query:
            c = 'Opening google'
            speak(c)
            webbrowser.open("google.com")

        elif 'lms' in query:
            c = 'Opening LMS'
            speak(c)
            webbrowser.open("lms.nirmauni.ac.in")

        elif 'amazon' in query:
            c = 'Opening Amazon'
            speak(c)
            webbrowser.open('https://www.amazon.in/')

        elif 'code forces' in query:
            c = 'Opening codeforces'
            speak(c)
            webbrowser.open("codeforces.com")

        elif 'assistant' in query or 'switch assistant' in query or 'change assistant' in query:
            if vID==0:
                vID=1
                vName='siri'
                engine.setProperty('voice',voices[vID].id)
            else:
                vID=0
                vName='jarvis'
                engine.setProperty('voice',voices[vID].id)

            speak(f"I am {vName}. Your voice assistant. How may I help you?")

        elif 'play music' in query:
            music_dir = "C:\\Users\\HP\OneDrive\\Desktop\\Projects\\Python\\Voice assistant\\songs"
            songs = os.listdir(music_dir)
            print(songs)
            r = random.randint(0,len(songs)-1)
            os.startfile(os.path.join(music_dir,songs[r]))

        elif 'the time' in query or 'tell me the time' in query or 'time' in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {time}")
        
        elif 'who are you' in query:
            speak(f"I am {vName}. Your voice assistant. How may I help you?")

        elif 'ticket' in query or 'movie' in query:
            c = 'Opening Bookmyshow'
            speak(c)
            webbrowser.open('https://in.bookmyshow.com/explore/home/ahmedabad')

        elif 'vs code' in query:
            c = 'Opening VS CODE'
            speak(c)
            path = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)

        elif 'email' in query:
            try:
                speak("what you want to send?")
                content = takeCommand()
                to = '21bce256@nirmauni.ac.in'
                sendEmail(to,content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry I am not able to send mail.Please try again")

        elif 'whatsapp' in query:
            from Whatsapp import sendMessage
            sendMessage(vID,vName)

        elif 'joke' in query:
            My_joke = pyjokes.get_joke()
            speak(My_joke)

        # elif 'news' in query or 'current affairs':
        #     from news import latestNews
        #     latestNews()

        elif 'play a game' in query:
            from game import game_play
            game_play(vID,vName)
    

        elif 'quit' in query or 'exit' in query:
            break
