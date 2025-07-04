import pyttsx3

import speech_recognition as sr

import random

#from googletrans import Translator
#translator = Translator()

engine = pyttsx3.init()

r = sr.Recognizer()

with sr.Microphone() as source:
    print('speak Anything: ')
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print('you said : {}'.format(text))
    except:
        print('sorry could not recognize your voice')

voices = engine.getProperty('voices')
for voice in voices:
   engine.setProperty('voice', voice.id)


#Say
if text=="hello" :
   a=engine.say("Hello sir. how can I help you, sir.")
   print("Hello sir. how can I help you, sir.")
elif text=="hello hello":
   b=engine.say("hello. how are you?, Sir.")
   print("hello. how are you?, Sir.")
elif text=="testing testing":
    engine.say("Yes sir, I am working you could ask me, Sir")
    print("Yes sir, I am working you could ask me, Sir")
elif text=="how are you":
   engine.say("I am fine ,sir. What about you?")
   print("I am fine ,sir. What about you?")
elif text=="are you there":
   engine.say("yes sir, how can i help you")
   print("yes, how can i help you")
else:
     print('sorry could not recognize your voice')



# For end
engine.runAndWait()
