import speech_recognition as sr


r = sr.Recognizer()


with sr.Microphone() as source:
    print('speak Anything: ')
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print('you said : {}'.format(text.dest))
    except:
        print('sorry could not recognize your voice')

