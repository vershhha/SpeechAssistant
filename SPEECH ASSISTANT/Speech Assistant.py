#--------------------------------------------------------------------------------------------------------------------------------------------------------------
# modules used
'''PLEASE install "pyaudio", "pillow" and the following modules using the pip command.
To install PYAUDIO =>
___________________
pip install pipwin
pipwin install pyaudio

pip install SpeechRecognition

rest can be installed using
pip install <module name>
___________________'''
#add pywhatkit
import pyttsx3
import pyjokes
import datetime
import speech_recognition as sr
import webbrowser
import wikipedia
import os
import random
import wolframalpha
import requests, json
from pprint import pprint
from translate import Translator
from tkinter import *
from PIL import ImageTk, Image
from playsound import playsound

#==============================================================================================================================================================

# FUNCTIONS

#==============================================================================================================================================================

# using tkinter for making introduction window
def intro():
         root = Tk()
         root.after(8000, lambda: root.destroy())
         root.title("PROJECT")
         root.geometry("900x750")
         root.configure(background="black")

         one = Label(root, text="SPEECH ASSISTANT", font="CASTELLAR 50 bold",bg='black', fg='cyan')
         one.pack(side=TOP)

         one2 = Label(root, text="CREATED BY VERSHA", font="Bauhaus 20",bg='black', fg='white')
         one2.pack()

         one3= Label(root, text="Class- XII-A", font="Bauhaus 20", bg='black', fg='white')
         one3.pack()

         frame = Frame(root, width = 2000, height = 3, highlightbackground="purple", highlightcolor="cyan",highlightthickness=2, bd=0)
         l = Entry(frame, borderwidth=0, relief="flat", highlightcolor="purple")
         l.place(width=2000, height=1)
         frame.pack
         frame.pack()
         frame.place(x=0, y=1)

         f = Frame(root, width = 2000, height = 3, highlightbackground="purple", highlightcolor="cyan",highlightthickness=2, bd=0)
         l = Entry(f, borderwidth=0, relief="flat", highlightcolor="purple")
         l.place(width=2000, height=1)
         f.pack
         f.pack()
         f.place(x=0, y=70)

         path= "C:\\Users\\versh\\OneDrive\\Desktop\\PROJECT\\mic.png"
         img = ImageTk.PhotoImage(Image.open(path))
         panel = Label(root, image = img)
         panel.pack(side = "top")
         root.mainloop()


#--------------------------------------------------------------------------------------------------------------------------------------------------------------
# for providing voice to this assistant
engine= pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
newVoiceRate = 175
engine.setProperty('rate',newVoiceRate)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------
def speak(audio):
    # for reading something for us
    engine.say(audio)
    engine.runAndWait()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------
def wishMe():
    # for wishing us according to time
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("ME: Good Morning!")
        speak('Good Morning!')
    elif hour>=12 and hour<18:
        print("ME: Good Afternoon!")
        speak('Good Afternoon!')
    else:
        print("ME: Good Evening!")
        speak('Good Evening!')
    print("ME: I'm your Speech Assistant. Please tell me how may I help you?")
    speak("I'm your Speech Assistant. Please tell me how may I help you?")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------
def takecommand():
     #it takes microphone input from the user and returns string out
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("ME: Listening...")
        r.pause_threshold=0.5
        audio=r.listen(source)
    try:
            print("ME: Recognizing...")
            query=r.recognize_google(audio, language='en-in')
            print(f"YOU: {query}\n")

    except Exception:
            print("ME: Say that again, please...")
            return 'None'
    return query

#--------------------------------------------------------------------------------------------------------------------------------------------------------------
def gnews():   
    # write your own apiKey here
    #BBC news API
    main_url = " https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=6a63b49072f3452e9015a643647d35c4"

    # fetching data in json format 
    open_bbc_page = requests.get(main_url).json() 
  
    # getting all articles in a string article 
    article = open_bbc_page["articles"] 

    # empty list which will  
    # contain all trending news 
    results = [] 
      
    for ar in article: 
        results.append(ar["title"]) 
          
    for i in range(len(results)): 
        # printing all trending news 
        print('ME: ',i + 1, results[i])
        # to read the news out loud for us 
        speak(results[i])
   
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
def news():
    # write your own apiKey here
    main_url = ("https://newsapi.org/v2/top-headlines?country=in&apiKey=6a63b49072f3452e9015a643647d35c4")

    # fetching data in json format 
    open_ht_page = requests.get(main_url).json() 
  
    # getting all articles in a string article 
    article = open_ht_page["articles"] 

    # empty list which will  
    # contain all trending news 
    results = [] 
      
    for ar in article: 
        results.append(ar["title"]) 
          
    for i in range(len(results)): 
        # printing all trending news
        print('ME: ',i + 1,')', results[i])
        # to read the news out loud for us 
        speak(results[i])

#--------------------------------------------------------------------------------------------------------------------------------------------------------------
def search_web(query): 

    # it searches query in web
    if query == 'search google' or query=='open google':
        webbrowser.open("https://www.google.com")

    elif 'youtube' in query: 
        speak("Opening in youtube") 
        webbrowser.open("http://www.youtube.com")
  
    elif 'classroom' in query:
        speak("opening google classroom")
        webbrowser.open("https://classroom.google.com/u/1/h")

    elif 'bodhi' in query or 'bodhisattva' in query or 'class plus' in query or 'class +' in query:
        speak("opening bodhisattva website")
        webbrowser.open("https://web.classplusapp.com/batches")

    elif 'fb' in query or 'facebook' in query:
        speak("opening Facebook login page")
        webbrowser.open("https://www.facebook.com")

    elif 'insta' in query or 'instagram' in query:
        speak("opening instagram login page")
        webbrowser.open("https://www.instagram.com/accounts/login/?hl=en")

    elif 'google' in query or 'search' in query:
        indx = query.split(' ')
        for i in indx:
            if i=='google':
                indx.remove(i)
        for j in indx:
            if j=='search':
                indx.remove(j)
        for i in indx:
                if i=='open':
                        indx.remove(i)
        for j in indx:
                if i== 'website' or i=='web':
                        indx.remove(j)
        speak("opening in google")
        webbrowser.open("https://www.google.com/?#q="+ ' '.join(indx))



#--------------------------------------------------------------------------------------------------------------------------------------------------------------
def recent(query):

    # it takes query and gives date, time, month and year
    if "what's the time" in query or  "what is the time" in query or "current time" in query or "time" in query:
        strTime = datetime.datetime.now().strftime("%I:%M:%S %p")
        print("ME: The time is:", strTime)
        speak(f"The time is {strTime}")

    elif "today's date" in query or "current date" in query or "what is the date" in query or "what's the date" in query or 'recent date' in query:
        date=datetime.date.today()
        print("ME: The date is:", date)
        speak(f"The date is {date}")

    elif "current month" in query or "what is the month" in query or "what's the month" in query or 'recent month' in query or 'month' in query:
        month=datetime.datetime.today().strftime("%m")
        print("ME: The month is:", month)
        speak(f"The month is {month}")

    elif "current year" in query or "what is the year" in query or "what's the year" in query or 'recent year' in query:
        year=datetime.datetime.today().strftime("%Y")
        print("ME: The year is:", year)
        speak(f"The year is {year}")

        
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
def weather_data(query):
	res=requests.get('http://api.openweathermap.org/data/2.5/weather?'+query+'&APPID=b35975e18dc93725acb092f7272cc6b8&units=metric');
	return res.json()

def print_weather(result,city):
    
    # for printing and reading weather conditions for us
	print("{}'s temperature: {}°C ".format(city,result['main']['temp']))
	speak("{}'s temperature: {}°C ".format(city,result['main']['temp']))
	print("Wind speed: {} m/s".format(result['wind']['speed']))
	speak("Wind speed: {} m/s".format(result['wind']['speed']))
	print("Description: {}".format(result['weather'][0]['description']))
	speak("Description: {}".format(result['weather'][0]['description']))
	print("Weather: {}".format(result['weather'][0]['main']))
	speak("Weather: {}".format(result['weather'][0]['main']))

def main():
    speak('City name?')
    print("City name?...")
    city=takecommand()
    if city=='none':
            print("ME: Say that again, please...")
            speak("ME: Say that again, please...")
            city=takecommand()
    try:
        query='q='+city;
        w_data=weather_data(query);
        print_weather(w_data, city)
    except:
        print('City name not found...')
        speak('City name not found')

        
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
def open_application(query): 

    # it opens various pre-installed applications
    # provide app_path here
    if "chrome" in query: 
        print("ME: Opening Google Chrome")
        speak("opening google chrome")
        os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome.lnk') 

    elif "calculator" in query:
        print("ME: Opening Calculator")
        speak("opening calculator")
        os.startfile(os.path.join('C:\\Windows\\System32\\calc.exe'))

    elif "open command prompt" in query or "open cmd" in query:
        print("ME: Opening Command Prompt")
        speak("opening command prompt")
        os.startfile(os.path.join('C:\\Windows\\System32\\cmd.exe'))

    elif "python shell" in query or 'idle' in query or 'python' in query:
        print("ME: Opening IDLE")
        speak("opening IDLE")
        os.startfile(os.path.join("C:\\Users\\versh\\OneDrive\\Desktop\\IDLE (Python 3.9 64-bit).lnk"))
    
    elif "notepad" in query:
        print("ME: Opening Notepad")
        speak("opening notepad")
        os.startfile(os.path.join('C:\\Users\\versh\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad.lnk'))

    elif "whatsapp" in query:
        print("ME: Opening WhatsApp Desktop")
        speak("opening whatsapp desktop")
        os.startfile(os.path.join("C:\\Users\\versh\\OneDrive\\Desktop\\WhatsApp.lnk"))
    
    elif "microsoft edge" in query:
        print("ME: Opening Microsoft Edge")
        speak("opening microsoft edge")
        os.startfile(os.path.join("C:\\Users\\Public\\Desktop\\Microsoft Edge.lnk"))

    elif "mysql" in query:
        print("Qpening MySQL")
        speak("Opening MySQL")
        os.startfile(os.path.join("C:\\Users\\versh\\OneDrive\\Desktop\\MySQL 8.0 Command Line Client.lnk"))

    elif "one drive" in query or 'onedrive' in query:
        print("Opening OneDrive")
        speak("opening one drive")
        os.startfile(os.path.join("C:\\Users\\versh\\OneDrive"))

    elif "paint" in query:
        print("Opening Paint")
        speak("opening paint")
        os.startfile(os.path.join('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Paint.lnk'))

    elif "wordpad" in query:
        print("Opening WordPad")
        speak("opening wordpad")
        os.startfile(os.path.join("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Wordpad.lnk"))
    
    else:
        print("ME: Application not found")
        speak("application not found")

#==============================================================================================================================================================

# MAIN PROGRAM

#==============================================================================================================================================================

if __name__=="__main__":
    intro()
    # for wishing us according to time
    wishMe()
    c=0
    while True:
        query= takecommand().lower()

        # logic for executing tasks based on query
        if 'hello' in query or 'hi' in query or 'hey' in query or 'namaste' in query or 'hola' in query or 'ola' in query:
            i=["Hi! How may I help you?","Namaste! That's hello in Indian! How may I help?",
               "Ola! That's hello in Portuguese! How can I help you?",
               "Ciao! That's hello in Italian! How may I help?",
               "Kon'nichiwa! That's hello in Japanese! What can I do for you?",
               "Hey there how may I help you",
               "Annyeonghaseyo. That's hello in Korean! How may I help?",
               "Hallo! That's hello in German! How can I help?",
               "G'day! That's hello in Australian! How may I help?"]
            
            x=random.randint(0, len(i)-1)
            print('ME: ',i[x])
            speak(i[x])

        elif "what's up" in query:
            print("Simply. too too good")
            speak("Simply. too too good")

        elif "your name" in query:
                print('You can call me your Virtual Assistant')
                speak('You can call me your Virtual Assistant')
                
        elif 'how are you' in query:
            i=['Your voice perks me up. Literally. How may I help',
               "I'm well, thank you. How can i help",
               "Feeling great!, what can I do for you?",
               "Good to hear from you! How may I help",
               "Thank you for asking. I am well. How may I help?"]
            
            x=random.randint(0, len(i)-1)
            print('ME: ',i[x])
            speak(i[x])

        elif "who are you" in query or "define yourself" in query or "describe yourself" in query: 
            print("ME: Hello, I am your Virtual Assistant. I am here to make your life easier. You can command me to perform various tasks such as opening applications, searching websites, calculations, can also give answers to your questions, I can crack jokes as well etc.. ^_^ ")
            speak ('Hello, I am your Virtual Assistant. I am here to make your life easier. You can command me to perform various tasks such as opening applications, searching websites, calculations, can also give answers to your questions, i can crack jokes as well etcetera')

        elif 'what can you do' in query or 'things which you can perform' in query or 'things which you can do' in query or 'brief of your skills' in query or 'menu' in query or 'list' in query or 'brief your skills' in query:
            print("ME: You can command me to perform various tasks such as opening applications, searching websites, calculations, can also give answers to your questions etc")
            speak("You can command me to perform various tasks such as opening applications, searching on websites, calculations, can also give answers to your questions etcetera")

        elif 'language do you speak' in query:
            print("ME: I speak Python")
            speak("I speak Python")

        elif 'why are you so smart' in query:
            print("ME: Learning makes me more artificially intelligent.... Machine learning!...^_^")
            speak("Learning makes me more artificially intelligent.... Machine learning!")

        elif 'joke' in query:
                joke=pyjokes.get_joke()
                print('ME:',joke)
                speak(joke)
                playsound("C:\\Users\\versh\\OneDrive\\Desktop\\PROJECT\\mixkit-cartoon-laugh-voice-2882.wav")

        elif 'wikipedia' in query:
            # for searching in wikipedia
            speak("searching Wikipedia...")
            results=wikipedia.summary(query,sentences=2)
            print("ME: According to Wikipedia...")
            speak("According to Wikipedia...")
            print("ME: ",results)
            speak(results)

        elif 'play music' in query or 'play a song' in query:
            songs_path=["C:\\Users\\versh\\OneDrive\\Desktop\\PROJECT\\MUSIC\\Apna Time Aayega- Gully Boy.mp3",
            "C:\\Users\\versh\\OneDrive\\Desktop\\PROJECT\\MUSIC\\Ed Sheeran - Shape Of You [Official].mp3",
            "C:\\Users\\versh\\OneDrive\\Desktop\\PROJECT\\MUSIC\\Girls Like You ft. Cardi B.mp3",
            "C:\\Users\\versh\\OneDrive\\Desktop\\PROJECT\\MUSIC\\Harrdy Sandhu- Kya Baat Ay.mp3",
            "C:\\Users\\versh\\OneDrive\\Desktop\\PROJECT\\MUSIC\\Khairiyat- Chhichhore.mp3",
            "C:\\Users\\versh\\OneDrive\\Desktop\\PROJECT\\MUSIC\\Let Me Love You.mp3",
            "C:\\Users\\versh\\OneDrive\\Desktop\\PROJECT\\MUSIC\\One Direction - What Makes You Beautiful.mp3",
            "C:\\Users\\versh\\OneDrive\\Desktop\\PROJECT\\MUSIC\\The Chainsmokers - Closer ft. Halsey.mp3",
            "C:\\Users\\versh\\OneDrive\\Desktop\\PROJECT\\MUSIC\\ZAYN - No Candle No Light feat. Nicki Minaj.mp3"]

            x=random.randint(0, len(songs_path)-1)
            k=songs_path[x]
            print("ME: I'm playing", k[46:])
            playsound(songs_path[x])


        elif 'search' in query or 'google' in query or 'youtube' in query or 'web' in query or 'website' in query or 'open in google' in query or 'open google' in query:
            # for web search
            search_web(query)

        elif 'open' in query: 
            # opens pre-installed applications
            open_application(query)

        elif "time" in query or "date" in query or "month" in query or "year" in query:
            recent(query)

        elif 'weather' in query:
            # for weather forecast
            main()
        
        elif 'news' in query:
            # for latest news
            if 'global' in query or 'international' in query or 'countries' in query:
                gnews()
            else:
                news()

        elif "calculate" in query: 
            # write your wolframalpha app_id here 
            client = wolframalpha.Client('PQQL43-R4KHW9VK7A')
            indx = query.split().index('calculate') 
            query = query.split()[indx + 1:] 
            res = client.query(' '.join(query)) 
            answer = next(res.results).text 
            print("ME: ", answer)
            speak(answer)

        elif 'translate' in query or 'translation' in query or 'translator' in query:
            # for translating statement from one language to another
            print('ME: From which language?')
            speak('from which language')
            f= takecommand()
            print('YOU: ',f)
            
            print("ME: To which language?")
            speak('to which language')
            t= takecommand()
            print('YOU: ',t)
                            
            print("ME: Tell me the statement for translation")
            speak('tell me the statement for translation')                    
            statement= takecommand()
            print('YOU:',statement)
                    
            translator= Translator(from_lang= str(f),to_lang= str(t))
            translation = translator.translate(str(statement))
            print('ME: ',translation)
            speak(translation)

        elif 'quit' in query or 'exit' in query  or 'bye' in query or 'see you later' in query or 'talk to you later' in query or 'ttyl' in query or 'goodbye' in query:
            hour=int(datetime.datetime.now().hour)
            if hour>=21 and hour<24:
                    print("ME: Good Night!")
                    speak('Good Night!')
            print("ME: Good to hear you, thank you!")
            speak("Good to hear you, thank you!")
            break
        
        elif  query!= 'none':
            # write your own wolframalpha app_id here
            client = wolframalpha.Client('PQQL43-R4KHW9VK7A')
            res = client.query(query)
            try:
                output = next(res.results).text
                print('ME: ', output )
                speak(output)
            except Exception:
                print("Never thought you'll ask this")
                speak('Never thought you will ask this')
                
        elif  query== 'none':
                 c+=1
                 if c==15:
                          print("ME: It's been a long you haven't given me any command.  So, I'm shutting down myself\n")
                          speak("It's been a long you haven't given me any command")
                          speak(" So, I'm  shutting down myself")
                          hour=int(datetime.datetime.now().hour)
                          if hour>=21 and hour<24:
                                    print("ME: Good Night!")
                                    speak('Good Night!')
                          print("ME: Good to hear you, thank you!")
                          speak("Good to hear you, thank you!")
                          break

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

