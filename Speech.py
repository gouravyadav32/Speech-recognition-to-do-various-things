import speech_recognition as sr
import webbrowser as wb
import os

r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()

with sr.Microphone() as source:
    print("Select Task")
    print("Wikipedia or youtube or Location")
    audio = r1.listen(source)
    if "Wikipedia" in r1.recognize_google(audio):
        os.system("python speech2.py")
        exit()

    if "location" in r1.recognize_google(audio):
        os.system("python speech3.py")
        exit()

with sr.Microphone() as source:
    print('Say My Country Name : India')
    print("Say It! Now")
    audio = r3.listen(source)

    p = r2.recognize_google(audio)
    print(p)
    if 'India' in r2.recognize_google(audio):
        r2 = sr.Recognizer()
        url = "https://www.youtube.com/results?search_query="
        for i in range(4):
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
