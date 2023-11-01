import speech_recognition as sr
import tkinter as tk
import threading
import pyttsx3
import pywhatkit  # youtube and whatsapp
import datetime  # for knowing current time
import wikipedia  # searching on wikipedia
import webbrowser  # to open links on browsers
import os
import random
import smtplib  # for email
import pyjokes  # for telling random jokes
from tkinter import Label
from PIL import ImageTk, Image
import requests
from io import BytesIO
import pywhatkit
import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
from bs4 import BeautifulSoup
from time import sleep
import os
from datetime import timedelta
# from datetime import datetime

recognizer = sr.Recognizer()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
vID=1
vName="siri"
engine.setProperty('voice',voices[vID].id)

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("400x600")
        self.master.configure(bg='#202020')
        self.pack(fill=tk.BOTH, expand=1)
        self.create_widgets()
        self.vName = "siri"
            # Set the background image
        
    def create_widgets(self):
        self.label = tk.Label(self, text="Click the button to start", font=('Arial', 12),
                            bg='#202020', fg='white')
        self.label.pack(pady=10)

        self.button = tk.Button(self, text="Start", font=('Arial', 12), bg='#e63946',
                        fg='white', activebackground='#a71d2a', activeforeground='white', command=self.start_thread)
        self.button.pack(side=tk.BOTTOM, pady=10)

        self.instructions_button = tk.Button(self, text="Instructions", font=('Arial', 12), bg='#202020',
                            fg='white', activebackground='#303030', activeforeground='white', command=self.show_instructions)
        self.instructions_button.pack(side=tk.BOTTOM, pady=10)
        self.back_button = tk.Button(self, text="Back", font=('Arial', 12), bg='#202020',
                                      fg='white', activebackground='#303030', activeforeground='white', command=self.hide_instructions)

    def speak(self,audio):
        # print(audio,"\n")

        self.label["text"]=audio
        engine.say(audio)
        engine.runAndWait()

    def show_instructions(self):
        instructions = "Here are some things\n you can ask me:\n\n"\
            "- Tell me a joke\n"\
            "- Search Wikipedia for <query>\n"\
            "- Play <song name> on YouTube\n"\
            "- Open <website URL>\n"\
            "- Send email\n"\
            "- Who is <person name>?\n"\
            "- Play rock paper scisoor\n"\
            "- Open LMS\n"\
            "- What is <query>?\n"\
            "- Exit\n"\
            "\nTo activate voice recognition,\n click the 'Start' button."
        self.label["text"] = instructions
        self.instructions_button.pack_forget()  # Hide the instructions button
        self.back_button.pack(side=tk.BOTTOM, pady=0)

    def hide_instructions(self):
        self.label["text"] = "Click the button to start"
        self.back_button.pack_forget()  # Hide the back button
        self.instructions_button.pack(side=tk.BOTTOM, pady=8) 
    def start_thread(self):
        self.thread = threading.Thread(target=self.run_assistant)
        self.thread.start()

    def run_assistant(self):
        self.wishMe()
        self.voiceAssistantp()
        # self.sendMessage()

    def start_listening(self):
        
        
        with sr.Microphone() as source:
            self.speak("Listening")
            recognizer.pause_threshold=1
            recognizer.energy_threshold=800
            audio = recognizer.listen(source)
        try:
            self.label["text"] = "Recognising..."
            query = recognizer.recognize_google(audio, language='en-in')
            self.speak("You said " + query)
        except Exception as e:
            # print(e)
            self.speak("Say that again please....")
            return "None"

        return query    
    
       
    def wishMe(self):
  

        hour = int(datetime.datetime.now().hour)
        if hour>=5 and hour<12:
         
            self.speak("Good Morning")
        
            

        elif hour>=12 and hour<18:
            
            self.speak("Good afternoon!")

        elif hour>=18 and hour<21:
            
            self.speak("Good evening!")

        else:
            
            self.speak("Good Night")

        
        self.speak(f"I am {self.vName}.\nYour voice assistant.\nHow may I help you?")
        
        
        
    def game_play(self):
        self.speak("LETSS PLAY ROCK-PAPER-SCISSOR")
        self.speak("YOU CHOOSE FIRST")
        count = 0
        Me_score = 0
        comp_score = 0

        while count<5:
            choose = ("rock","paper","scissor")
            comp_choice = random.choice(choose)
            l = ['rock','paper','scissor','caesar','None']

            # self.speak("self.speak [r for rock], [p for paper], [s for scissor]")
            query = self.start_listening().lower()
            # query = int(input("1 : rock\n2 : paper\n3 : scissor\nEnter ypur choice : "))

            if 'exit' in query or 'stop' in query or 'close' in query or 'quit' in query:
                break
 
            if query not in l:
                continue

            if(query == 'rock'):
                # self.speak("YOU CHOSE ROCK")
                if(comp_choice == 'rock'):
                    self.speak("rock")
                elif(comp_choice == 'paper'):
                    self.speak("paper")
                    comp_score+=1
                elif(comp_choice == 'scissor'):
                    self.speak("scissor")
                    Me_score+=1

            elif(query == 'paper'):
                # self.speak("YOU CHOSE PAPER")
                if(comp_choice == 'rock'):
                    self.speak("rock")
                    Me_score+=1
                elif(comp_choice == 'paper'):
                    self.speak("paper")
                elif(comp_choice == 'scissor'):
                    self.speak("scissor")
                    comp_score+=1

            elif(query == 'scissor' or query == 'caesar'):
                # self.speak("YOU CHOSE SCISSOR")
                if(comp_choice == 'rock'):
                    self.speak("rock")
                    comp_score+=1
                elif(comp_choice == 'paper'):
                    self.speak("paper")
                    Me_score+=1
                elif(comp_choice == 'scissor'):
                    self.speak("scissor")     

            self.speak(f"Score:-\nMy : {Me_score}\nVoice assistant : {comp_score}\n")   
            # print(f"Score:-\nMy : {Me_score}\nVoice assistant : {comp_score}\n")
            count+=1

        
        self.speak(f"Final Score\nMy : {Me_score}\nVoice assistant : {comp_score}")

        if Me_score==comp_score:
            self.speak("MATCH TIED")
        elif Me_score>comp_score:
            self.speak("CONGRATULATIONS! YOU WON")
        elif Me_score<comp_score:
            self.speak("BETTER LUCK NEXT TIME! I WON")
    
    def get_quotes(self):
        fp = open("good_quotes.txt","r")
        content = fp.read()
        quotes = content.split("\n")
        quote = random.choice(quotes)
        words = quote.split()
        groups_of_three = [words[i:i+3] for i in range(0, len(words), 3)]
        formatted_quote = "\n".join([" ".join(group) for group in groups_of_three])
        self.label["text"]=formatted_quote
        engine.say(quote)
        engine.runAndWait()

    def sendMessage(self):
        
        strTime = int(datetime.datetime.now().strftime("%H"))
        time = int((datetime.datetime.now()+timedelta(minutes=2)).strftime("%M"))

        self.speak("who do you want to message?")
        
        a=int(input('''
        Aditya - 1
        Arafat - 2
        Priyanshu - 3
        Jayesh - 4
        Enter your choice :
        '''))
        b = f"Aditya - 1\nArafat - 2\nPriyanshu - 3\nJayesh - 4\nEnter your choice :"
        self.speak(b)
        if a == 1:
            self.speak("what's the message")
            message = self.start_listening()
            pywhatkit.sendwhatmsg("+916353178377",message,time_hour=strTime,time_min=time)
        elif a == 2:
            self.speak("what's the message")
            message = self.start_listening()
            pywhatkit.sendwhatmsg("+917066020465",message,time_hour=strTime,time_min=time)
        elif a == 3:
            self.speak("what's the message")
            message = self.start_listening()
            pywhatkit.sendwhatmsg("+918401087744",message,time_hour=strTime,time_min=time)
        elif a == 4:
            self.speak("what's the message")
            message = self.start_listening()
            pywhatkit.sendwhatmsg("+919726634150",message,time_hour=strTime,time_min=time)

    
    def voiceAssistantp(self):
    
        running = True
        while running:  
            query = self.start_listening().lower()

            if 'how are you' in query:
                self.speak("I am fine! What about you")
            elif 'i am happy' in query or 'i am fine' in query:
                self.speak("Nice to hear! I am happy too.")
            elif 'i am sad' in query:
                self.get_quotes()
            elif 'thank you' in query:
                self.speak("your welcome!")

            # to execute user choice tasks
            if 'wikipedia' in query or 'search' in query:
                self.speak("Searching wikipedia...")
                results = wikipedia.summary(query, sentences=1)
                self.speak("According to wikipedia")
                # Split the results into separate lines based on periods
                lines = results.split(" ")
                
                # Combine every three words with spaces and a newline character
                lines = [ " ".join(lines[i:i+3])+"\n" for i in range(0, len(lines), 3) ]
                
                # Combine the lines into a string
                formatted_results = "".join(lines)
                # Update the label text with the formatted results
                self.label['text']=formatted_results
                engine.say(results)
                engine.runAndWait()

            elif 'play' in query and 'youtube' in query:
                c = 'Opening youtube'
                self.speak(c)
                pywhatkit.playonyt(query)

            elif 'youtube' in query:
                c = 'Opening youtube'
                #self.speak(c)
                self.speak(c)
                webbrowser.open("youtube.com")

            elif 'google' in query:
                c = 'Opening google'
                self.speak(c)
                webbrowser.open("google.com")

            elif 'lms' in query:
                c = 'Opening LMS'
                self.speak(c)
                webbrowser.open("lms.nirmauni.ac.in")

            elif 'amazon' in query:
                c = 'Opening Amazon'
                self.speak(c)
                webbrowser.open('https://www.amazon.in/')

            elif 'code forces' in query:
                c = 'Opening codeforces'
                self.speak(c)
                webbrowser.open("codeforces.com")

            elif 'assistant' in query or 'switch assistant' in query or 'change assistant' in query:
                global vID
                if vID==0:
                    vID=1
                    self.vName='siri'
                    engine.setProperty('voice',voices[vID].id)
                else:
                    vID=0
                    self.vName='jarvis'
                    engine.setProperty('voice',voices[vID].id)
                
               
                self.speak(f"I am {self.vName}.\nYour voice assistant.\nHow may I help you?")

            elif 'play music' in query:
                music_dir = "C:\\Users\\HP\OneDrive\\Desktop\\Projects\\Python\\Voice assistant\\songs"
                songs = os.listdir(music_dir)
                print(songs)
                r = random.randint(0,len(songs)-1)
                os.startfile(os.path.join(music_dir,songs[r]))

            elif 'the time' in query or 'tell me the time' in query or 'time' in query:
                time = datetime.datetime.now().strftime("%H:%M:%S")
                times= f"The time is {time}"
                self.speak(f"The time is {time}")
            
            elif 'who are you' in query:
                self.speak(f"I am {self.vName}.\nYour voice assistant.\nHow may I help you?")

            elif 'ticket' in query or 'movie' in query:
                c = 'Opening Bookmyshow'
                self.speak(c)
                webbrowser.open('https://in.bookmyshow.com/explore/home/ahmedabad')

            elif 'VS code' in query:
                c = 'Opening VS CODE'
                self.speak(c)
                path = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(path)

            elif 'email' in query:
                try:
                    self.speak("what you want to send?")
                    content = self.start_listening()
                    to = '21bce256@nirmauni.ac.in'
                    sendEmail(to,content)

                    self.speak("Email has been sent")
                    
                except Exception as e:
                    print(e)
                    self.speak("Sorry I am not able to send mail.Please try again")

            elif 'whatsapp' in query:
                self.sendMessage()

            elif 'joke' in query:
                My_joke = pyjokes.get_joke()
                lines = My_joke.split(" ")
                
                # Combine every three words with spaces and a newline character
                lines = [ " ".join(lines[i:i+3])+"\n" for i in range(0, len(lines), 3) ]
                
                # Combine the lines into a string
                formatted_results = "".join(lines)
                self.label["text"]=formatted_results
                engine.say(My_joke)
                engine.runAndWait()
           
            elif 'game' in query:
                self.game_play()
            
            elif 'quit' in query or 'exit' in query:
                on_closing()
                running = False

def sendEmail(to,content):
        fp = open('pwd.txt','r')
        pwd = fp.read()

        # simple mail transfer protocol
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login('21bce247@nirmauni.ac.in',pwd)
        server.sendmail('21bce247@nirmauni.ac.in',to,content)
        server.close()

def on_closing():
           # This function will be called when the user closes the window
           
           root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Speech to Text")
    root.protocol("WM_DELETE_WINDOW",on_closing)
    app = Application(master=root)
    app.mainloop()
