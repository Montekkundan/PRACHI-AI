import pyttsx3

def Speak(audio):
    prachi = pyttsx3.init()
    voices = prachi.getProperty('voices')
    prachi.setProperty("rate", 179)
    prachi.setProperty('voice', voices[33].id)
    print("   ")
    print(f"PRACHI: {audio}")
    prachi.say(audio)
    print("   ")
    prachi.runAndWait()