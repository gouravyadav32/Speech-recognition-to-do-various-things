import speech_recognition as sr
import webbrowser as wb

r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()

with sr.Microphone() as source:
    print('Say My Name : Gourav')
    print("Say It!")
    audio = r3.listen(source)

    p = r2.recognize_google(audio)
    print(p)
    if 'India' in r2.recognize_google(audio):
        r2 = sr.Recognizer()
        url = "https://www.youtube.com/results?search_query="
        for i in range(3):
            with sr.Microphone() as source:
                print("Search your Query")
                audio  = r2.listen(source)

                try:
                    get = r2.recognize_google(audio)
                    print(get)
                    if get == 'terminate':
                        exit()
                    wb.get().open_new(url+get)
                except sr.UnknownValueError:
                    print("Error")
                except sr.RequestError as e:
                    print("failed".format(e))
