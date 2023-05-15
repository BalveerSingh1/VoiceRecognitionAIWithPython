import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
engine= pyttsx3.init('sapi5')
def speak(audio):
  engine.say(audio)
  engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
      speak("Good morning")
    elif(hour>=12 and hour<=16):
      speak("Good Afternoon !")
    elif(hour>4 and hour<=12):
       speak("Good Evening !")
    speak("I am Anurag's AI . please tell me how may I help u")

def takeCommand():
 #A takes microphone input from the user and return string output
    r = sr.Recognizer() 
    with sr.Microphone() as source:
       print("listering....")
       r.pause_threshold = 1
       audio=r.listen(source)
    try:
       print("Recognizing...")
       query=r.recognize_google(audio,language='en-in')
       print(f"User said {query}\n")

    except Exception as e:
    #    print(e)
       print("say that again Please...")
       return "None"
    return query
def search(query):
    if ('wikipedia' in query):
        speak("Searching Wikipedia.....")
        query= query.replace("Wikipedia","")
        results=wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)
    elif 'time' in query:
        musicPath = "/Users/harry/Downloads/downfall-21371.mp3"
        hour = datetime.datetime.now().strftime("%H")
        min = datetime.datetime.now().strftime("%M")
        second = datetime.datetime.now().strftime("%S")
        print(f"{hour}:{min}:{second}")
        speak(f"Sir time is {hour} bajke {min} minutes")
    elif ( "open youtube" in query):
        webbrowser.open("youtube.com")
    elif("open google"in query):
        webbrowser.open("google.com")
    elif("open whatsapp"in query):
        webbrowser.open("whatsapp.com")
    elif ("play music" in query or "play song" in query or "gaana" in query ):
        webbrowser.open("https://gaana.com/")
    elif("videosong" in query or "video with song" in query):
          webbrowser.open("https://www.youtube.com/results?search_query=song/")
    elif("ms word" in query or "microsoft word" in query):
        codepath ="C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
        os.startfile(codepath)
    elif("notepad++" in query or "notepad plus" in query):
        codepath ="C:\\Program Files\\Notepad++\\notepad++.exe"
        os.startfile(codepath)
if __name__ == '__main__':
  wishMe()
  while True:
    querys=takeCommand().lower()
    language=search(querys)
    if "quit".lower() in querys:
        exit()


#   speak("Balbir is a good boy")


       

    