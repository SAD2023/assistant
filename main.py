import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import time
import subprocess
import wolframalpha
import json
import requests


# Potentially ask for this at the start and store it for later use, but
# for now, I'm just going to hardcode it in.
user_name = "Sadman"




# This simply sets up the machine
assistant=pyttsx3.init('sapi5')
voices=assistant.getProperty('voices')
assistant.setProperty('voice', voices[1].id)

# Setting the path for chrome on my device. May need to be changed later
chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path),1)


"""
Greets the user using various greetings depending on the time of day.

No args passed in.
"""
def greet_user():
    hour=datetime.datetime.now().hour
    print(hour)

    if (hour>=5 and hour<12):
        say("Hi " + user_name + ", Good Morning! Have a wonderful day!")

    elif (hour>=12 and hour<=17):
        say("Hi " + user_name + ", Good Afternoon! Hope you're having a great day!")

    elif(hour>=17 and hour<21):
        say("Good evening " + user_name + "!")

        

  

"""
This function takes a text and makes the machine speak it out loud.

Args:
    text: string
"""
def say(text: str):
    assistant.say(text)
    assistant.runAndWait()


"""
Listens for a user audio input, transforms into text, and returns the text.

No args for this.
"""
def userinput(counter):
    r = sr.Recognizer()
    #counter += 1
    print(counter)
    with sr.Microphone() as source:
        print("Assistant is Listening...")

        if (counter == 0):

            # Specify time limit so it doesn't keep listening forever.
            audio = r.listen(source, timeout=2, phrase_time_limit=4)
            statement = ""

            try:
                # TODO currently only works for english
                statement=r.recognize_google(audio,language='en-in')
                print(f"input:{statement}\n")

            except Exception:
                say("Sorry, could you repeat that?")
                return "None"

        else:
            
            # Specify time limit so it doesn't keep listening forever.
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
            statement = ""

            try:
                # TODO currently only works for english
                statement=r.recognize_google(audio,language='en-in')
                print(f"input:{statement}\n")

            except Exception:
                return "None"

        return statement

# print("Loading your AI personal assistant G-One")
# say("Loading your AI personal assistant G-One")
# wishMe()

def main():
    c = webbrowser.get('chrome')
    counter = 0
    greet_user()

    while True:
        say("...")
        statement = userinput(counter).lower()
        print(statement)
                   
        if statement=="none" and counter==1:
            break

        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            say('Okay')
            break

        elif 'open google' in statement:
            c.open_new_tab("https://www.google.com")
            say("Google chrome is open")
            counter = 1
            time.sleep(2)

        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            say(f"the time is {strTime}")
            counter = 1
        
        elif 'google'  in statement:
            query = statement.partition("google")
            print(query)
            # statement = statement.replace("search", "")
            c.open_new_tab("http://www.google.com/search?q="+query[2])
            counter = 1
            time.sleep(2)	

        elif "good night" in statement or "goodnight" in statement:
            say("Good night " + user_name + "! Sleep tight!")
            break

#TODO make it so that its always listening, and 'turns on' when called
if __name__=='__main__':
    # set c as chrome
    main()
    
"""
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source, timeout=3, phrase_time_limit=5)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

    return said

get_audio()

"""