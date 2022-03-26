import datetime
from speak import Speak
import pywhatkit
import wikipedia


def Time():
    time = datetime.datetime.now().strftime("%H:%M")
    Speak(time)


def Date():
    date_1 = datetime.date.today().strftime("%B %d, %Y")
    Speak(date_1)


def Day():
    day = datetime.datetime.now().strftime("%A")
    Speak(day)


def NonInputExecution(query):
    query = str(query)

    if "time" in query:
        Time()

    elif "date" in query:
        Date()

    elif "day" in query:
        Day()

def InputExecution(tag, query):
    if "wikipedia" in tag:
        name = str(query).replace("who is", "").replace("about", "").replace("what is", "").replace("wikipedia", "")
        result = wikipedia.summary(name)
        Speak(result)

    elif "google" in tag:
        query = str(query).replace("google", "")
        query = query.replace("search", "")
        Speak("Redirecting to Google...")
        pywhatkit.search(query)
