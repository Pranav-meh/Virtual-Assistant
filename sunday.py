import pyttsx3  #pip install pyttsx3  Text to speech conversion
import datetime  #module
import speech_recognition as sr  # For speech recognition
import wikipedia   # To use Wikipedia module
import smtplib      # To user SMTP Simple Mail Tranfer Protocol
import webbrowser as wb     # to use chrome browser
import os  #inbuilt       # For OS functionalities
import pyautogui         # To access windows screen cursor usewd in SS
import psutil        # To access OS CPU amd Battery Usage
import pyjokes  # For Jokes
import requests, json  #inbuilt

engine = pyttsx3.init()
engine.setProperty('rate', 190)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('volume', 100)

#change voice
def voice_change(v):
    x = int(v)
    engine.setProperty('voice', voices[x].id)
    speak("done sir")


#speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


#time function
def time():
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    speak("The current time is")
    speak(Time)

OPENWEATHER_APP_ID = "6a57e4f50b3749937c1af2884106c66a"


def get_weather_report(city):
    res = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_APP_ID}&units=metric").json()
    weather = res["weather"][0]["main"]
    temperature = res["main"]["temp"]
    feels_like = res["main"]["feels_like"]
    return weather, f"{temperature}℃", f"{feels_like}℃"

#date function  
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)

def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return(ip_address["ip"])
#drawing shapes
def rectangle():
    pyautogui.press('win')
    pyautogui.PAUSE = 1

    pyautogui.typewrite('paint')
    pyautogui.PAUSE = 1

    pyautogui.press('enter')

    pyautogui.moveTo(600, 600)
    pyautogui.dragTo(600, 700, button='left')
    pyautogui.dragTo(900, 700, button='left')
    pyautogui.dragTo(900, 600, button='left')
    pyautogui.dragTo(600, 600, button='left')

def square_spiral():
    pyautogui.press('win')
    pyautogui.PAUSE = 1

    pyautogui.typewrite('paint')
    pyautogui.PAUSE = 1
    pyautogui.press('enter')

    pyautogui.moveTo(600, 600)
    distance = 200

    while (distance):
        # moves the cursor to the right3
        pyautogui.dragRel(distance, 0)
        distance = distance - 5
        # move the cursor down
        pyautogui.dragRel(0, distance )
        # move the cursor to the left
        pyautogui.dragRel(-distance, 0)
        distance = distance - 5
        # move the cursor up
        pyautogui.dragRel(0, -distance)
def square():
    pyautogui.press('win')
    pyautogui.PAUSE = 1

    pyautogui.typewrite('paint')

    pyautogui.press('enter')

    pyautogui.moveTo(600, 600)
    pyautogui.dragTo(600, 700, button='left')
    pyautogui.dragTo(700, 700, button='left')
    pyautogui.dragTo(700, 600, button='left')
    pyautogui.dragTo(600, 600, button='left')
#ppt
def ppt():
    pyautogui.press('win')
    pyautogui.PAUSE = 1

    pyautogui.typewrite('ppt')
    pyautogui.press('enter')
    pyautogui.moveTo(332, 281)
    pyautogui.PAUSE = 2
    pyautogui.leftClick()

#notepad
def notepad():
    pyautogui.press('win')
    pyautogui.PAUSE = 1

    pyautogui.typewrite('notepad')
    pyautogui.press('enter')

#word
def word():
    pyautogui.press('win')
    pyautogui.PAUSE = 1

    pyautogui.typewrite('word')
    pyautogui.press('enter')
    pyautogui.moveTo(332, 281)
    pyautogui.PAUSE = 2
    pyautogui.leftClick()


def youtube():
    pyautogui.moveTo(990, 1055)
    pyautogui.PAUSE = 2
    pyautogui.leftClick()
    pyautogui.PAUSE = 2
    pyautogui.leftClick(715,64)
    pyautogui.typewrite('youtube.com')
    pyautogui.press('enter')


def checktime(tt):
    hour = datetime.datetime.now().hour
    if ("morning" in tt):
        if (hour >= 6 and hour < 12):
            speak("Good morning sir")
        else:
            if (hour >= 12 and hour < 18):
                speak("it's Good afternoon sir")
            elif (hour >= 18 and hour < 24):
                speak("it's Good Evening sir")
            else:
                speak("it's Goodnight sir")
    elif ("afternoon" in tt):
        if (hour >= 12 and hour < 18):
            speak("it's Good afternoon sir")
        else:
            if (hour >= 6 and hour < 12):
                speak("Good morning sir")
            elif (hour >= 18 and hour < 24):
                speak("it's Good Evening sir")
            else:
                speak("it's Goodnight sir")
    else:
        speak("it's night sir!")
#chatgpt
def chatgpt():
    pyautogui.moveTo(990, 1055)
    pyautogui.PAUSE = 2
    pyautogui.leftClick()
    pyautogui.PAUSE = 2
    pyautogui.leftClick(715, 64)
    pyautogui.typewrite('chat gpt')
    pyautogui.press('enter')
    pyautogui.moveTo(390, 398)
    pyautogui.leftClick(390,398)
    pyautogui.PAUSE = 2
    pyautogui.leftClick(114,802)
#netflix login
def netflix():
    pyautogui.moveTo(990, 1055)
    pyautogui.leftClick()
    pyautogui.PAUSE = 1.2
    pyautogui.leftClick()
    pyautogui.PAUSE = 1.2
    pyautogui.leftClick(812, 631)
    pyautogui.PAUSE = 1.2
    pyautogui.leftClick(734, 530)
    pyautogui.typewrite('9')
    pyautogui.typewrite('9')
    pyautogui.typewrite('1')
    pyautogui.typewrite('1')

#welcome function
def wishme():
    speak("Welcome Back")
    hour = datetime.datetime.now().hour
    if (hour >= 6 and hour < 12):
        speak("Good Morning sir!")
    elif (hour >= 12 and hour < 18):
        speak("Good afternoon sir")
    elif (hour >= 18 and hour < 24):
        speak("Good Evening sir")
    else:
        speak("Goodnight sir")

    speak("Sunday at your service, Please tell me how can i help you?")


def wishme_end():
    speak("signing off")
    hour = datetime.datetime.now().hour
    if (hour >= 6 and hour < 12):
        speak("Good Morning")
    elif (hour >= 12 and hour < 18):
        speak("Good afternoon")
    elif (hour >= 18 and hour < 24):
        speak("Good Evening")
    else:
        speak("Goodnight.. Sweet dreams")
    quit()


#command by user function
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  #Translate audio to query  
        print(query)   ####
    except Exception as e:
        print(e)
        speak("Say that again please...")

        return "None"

    return query


#screenshot function
def screenshot():
    img = pyautogui.screenshot()
    img.save(
        "C:\\Users\\pranav\\Desktop\\Nebula\\ss.png"
    )


#battery and cpu usage
def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU usage is at ' + usage)
    print('CPU usage is at ' + usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)
    print("battery is at:" + str(battery.percent))


#joke function
def jokes():
    j = pyjokes.get_joke()
    print(j)
    speak(j)




def personal():
    speak(
        "I am Sunday, version 1.0, I am an AI assistent, I am developed by Pranav on 29 June 2022 in INDIA"
    )
    speak("Now i hope you know me")


if __name__ == "__main__":
    wishme()
    while (True):
        query = takeCommand().lower()

        #time

        if ('time' in query):
            time()

#date

        elif ('date' in query):
            date()

#personal info
        elif ("tell me about yourself" in query):
            personal()
        elif ("about you" in query):
            personal()
        elif ("who are you" in query):
            personal()
        elif ("yourself" in query):
            personal()

        elif ("developer" in query or "tell me about your developer" in query
              or "father" in query or "who develop you" in query
              or "developer" in query):
            res = open("about.txt", 'r')
            speak("here is the details: " + res.read())

#searching on wikipedia

        elif ('wikipedia' in query or 'what' in query or 'who' in query
              or 'when' in query or 'where' in query):
            speak("searching...")
            query = query.replace("wikipedia", "")
            query = query.replace("search", "")
            query = query.replace("what", "")
            query = query.replace("when", "")
            query = query.replace("where", "")
            query = query.replace("who", "")
            query = query.replace("is", "")
            result = wikipedia.summary(query, sentences=2)
            print(query)
            print(result)
            speak(result)



#sysytem logout/ shut down etc

        elif ("logout" in query):
            os.system("shutdown -1")
        elif ("restart" in query):
            os.system("shutdown /r /t 1")
        elif ("shut down" in query):
            os.system("shutdown /r /t 1")



#reminder function

        elif ("create a reminder list" in query or "reminder" in query):
            speak("What is the reminder?")
            data = takeCommand()
            speak("You said to remember that" + data)
            reminder_file = open("data.txt", 'a')
            reminder_file.write('\n')
            reminder_file.write(data)
            reminder_file.close()

#reading reminder list

        elif ("do you know anything" in query or "remember" in query):
            reminder_file = open("data.txt", 'r')
            speak("You said me to remember that: " + reminder_file.read())

#screenshot
        elif ("screenshot" in query):
            screenshot()
            speak("Done!")

#cpu and battery usage
        elif ("cpu and battery" in query or "battery" in query
              or "cpu" in query):
            cpu()
        
#Find my IP
        elif("find my ip" in query):
            ip_address = find_my_ip()
            speak(f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen sir.')
            print(f'Your IP Address is {ip_address}')


#location
        elif 'location' in query:
            speak('What is the location?')
            location = takeCommand()
            url = 'https://google.nl/maps/place/' + location + '/&amp;'
            wb.get('chrome').open_new_tab(url)
            speak('Here is the location ' + location)

#jokes
        elif ("tell me a joke" in query or "joke" in query):
            jokes()

#weather
        elif ("weather" in query or "temperature" in query):
            ip_address = find_my_ip()
            city = requests.get(f"https://ipapi.co/{ip_address}/city/").text
            speak(f"Getting weather report for your city {city}")
            weather, temperature, feels_like = get_weather_report(city)
            speak(f"The current temperature is {temperature}, but it feels like {feels_like}")
            speak(f"Also, the weather report talks about {weather}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(f"Description: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")

#Sunday features
        elif ("tell me your powers" in query or "help" in query
              or "features" in query):
            features = ''' i can help to do lot many things like..
            i can tell you the current time and date,
            i can tell you the current weather,
            i can tell you battery and cpu usage,
            i can draw a square spiral for you,
            i can draw the following shapes for you circle,square,rectangle
            i can take screenshots,
            i can tell you non funny jokes,
            i can open any website,
            i can search the thing on wikipedia,
            My boss is working on this system to add more features...,
            tell me what can i do for you??
            '''
            print(features)
            speak(features)

        elif ("hii" in query or "hello" in query or "good morning" in query
              or "good afternoon" in query or "goodnight" in query
              or "morning" in query or "noon" in query or "night" in query):
            query = query.replace("Sunday", "")
            query = query.replace("hi", "")
            query = query.replace("hello", "")
            if ("morning" in query or "night" in query or "goodnight" in query
                    or "afternoon" in query or "noon" in query):
                checktime(query)
            else:
                speak("what can i do for you")

#changing voice
        elif ("voice" in query):
            speak("for female say female and, for male say male")
            q = takeCommand()
            if ("female" in q):
                voice_change(1)
            elif ("male" in q):
                voice_change(0)
        elif ("male" in query or "female" in query):
            if ("female" in query):
                voice_change(1)
            elif ("male" in query):
                voice_change(0)

#exit function

        elif ('i am done' in query or 'bye bye Sunday' in query
              or 'go offline Sunday' in query or 'bye' in query
              or 'nothing' in query):
            wishme_end()

        elif ("draw a square" in query):
            square()
            speak("Done!,what else would you like me to draw")

        elif ("draw a rectangle" in query or "how about a rectangle then" in query or "a rectangle then" in query or
        "how about a rectangle" in query or "rectangle" in query or "a rectangle" in query ):
            rectangle()
            speak("Done!")

        elif ("draw a spiral" in query or "spiral"in query ):
            square_spiral()
            speak("Done!")
        elif ("open netflix" in query or 'netflix' in query):
            netflix()
            speak("Done!")
        elif ("open YouTube " in query or 'youtube' in query):
            youtube()
            speak("Done!")
        elif ("open chatgpt " in query or 'open chat GPT' in query or  'chat' in query):
            chatgpt()
            speak("Done!")
        elif ("word" in query or 'open word' in query or'open word file for me' in query):
            word()
            speak("Done!")
        elif ("ppt" in query or 'open powerpoint' in query or 'open a new ppt for me' in query):
            ppt()
            speak("Done!")
        elif ("notepad" in query or 'open notepad' in query or 'open a new text file for me' in query):
            notepad()
            speak("Done!")