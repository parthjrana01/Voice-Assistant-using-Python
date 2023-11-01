import requests
import json
import pyttsx3

engine=pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
vID=1
vName="jarvis"
engine.setProperty('voice',voices[vID].id)


def speak(audio):
    print(audio,"\n")
    engine.say(audio)
    engine.runAndWait()

def latestNews():
    api_dict = {"Bussiness":"https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=163e58500eca47cdafc6a577efd8e614",
               "Entertainment":"https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=163e58500eca47cdafc6a577efd8e614",
               "Health":"https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=163e58500eca47cdafc6a577efd8e614",
               "Science":"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=163e58500eca47cdafc6a577efd8e614",
               "Sports":"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=163e58500eca47cdafc6a577efd8e614",
               "Technology":"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=163e58500eca47cdafc6a577efd8e614"}
    
    content = None
    url = None
    speak("Which field news do you want, [Bussiness] , [Health], [Entertainment], [Science], [Sports], [Technology]")
    field = input("Enter field : ")
    for key,value in api_dict.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            print("url was found")
            break
        else:
            url = True
            if url is True:
                print("url not found")

    news = requests.get(url).text
    news = json.loads(news)

    arts = news["articles"]
    for articles in arts:
        article = articles["title"]
        print(article)
        speak(article)
        news_url = article["url"]
        print(f"for more info visit : {news_url}")

        a=int(input("1 : stop\n2 : continue\nEnter : "))
        if a==1:
            break




    


# 163e58500eca47cdafc6a577efd8e614