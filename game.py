import pyttsx3
import speech_recognition as sr
import random

engine=pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)

vID=1
vName="jarvis"
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

def game_play():
    speak("LETSS PLAY ROCK-PAPER-SCISSOR")
    speak("YOU CHOOSE FIRST")
    count = 0
    Me_score = 0
    comp_score = 0

    while count<5:
        choose = ("rock","paper","scissor")
        comp_choice = random.choice(choose)
        l = ['rock','paper','scissor','caesar','None']

        # speak("speak [r for rock], [p for paper], [s for scissor]")
        query = takeCommand().lower()
        # query = int(input("1 : rock\n2 : paper\n3 : scissor\nEnter ypur choice : "))

        if query not in l:
            continue

        if(query == 'rock'):
            speak("YOU CHOSE ROCK")
            if(comp_choice == 'rock'):
                speak("rock")
            elif(comp_choice == 'paper'):
                speak("paper")
                comp_score+=1
            elif(comp_choice == 'scissor'):
                speak("scissor")
                Me_score+=1

        elif(query == 'paper'):
            speak("YOU CHOSE PAPER")
            if(comp_choice == 'rock'):
                speak("rock")
                Me_score+=1
            elif(comp_choice == 'paper'):
                speak("paper")
            elif(comp_choice == 'scissor'):
                speak("scissor")
                comp_score+=1

        elif(query == 'scissor' or query == 'caesar'):
            speak("YOU CHOSE SCISSOR")
            if(comp_choice == 'rock'):
                speak("rock")
                comp_score+=1
            elif(comp_choice == 'paper'):
                speak("paper")
                Me_score+=1
            elif(comp_choice == 'scissor'):
                speak("scissor")
                
            
        print(f"Score:-\nMy : {Me_score}\nVoice assistant : {comp_score}\n")
        count+=1

    print(f"\nFinal Score\nMy : {Me_score}\nVoice assistant : {comp_choice}")

    if Me_score==comp_score:
        speak("MATCH TIED")
    elif Me_score>comp_score:
        speak("CONGRATULATIONS! YOU WON")
    elif Me_score<comp_score:
        speak("BETTER LUCK NEXT TIME! I WON")