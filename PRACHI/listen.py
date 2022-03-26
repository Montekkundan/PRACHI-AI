import speech_recognition as sr


def take_command():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        command.pause_threshold = 0.6
        audio = command.listen(source,0,4)

    try:
        print("Recognizing....")
        query = command.recognize_google(audio, language="en-in")
        print(f"You said: {query}")
    except:
        return "none"

    return query.lower()
