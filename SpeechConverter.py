import tkinter
from tkinter import *
import threading
import time
import os
import speech_recognition as sr
import textwrap
import gtts
from playsound import playsound
from translate import Translator

exitFlag = 0


class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("Starting " + self.name)
        text = Text(root)
        r = sr.Recognizer()  # define the microphone
        mic = sr.Microphone(device_index=0)  # record your speech
        with mic as source:
            audio = r.listen(source)  # speech recognition
            print(audio)

        result = r.recognize_google(audio)  # export the result
        with open('my_result.txt', mode='w') as file:
            file.write("Recognized text:")
            file.write("\n")
            file.write(result)
            print("Exporting process completed!")
        print(textwrap.fill(result, 100))

        # translateIt(result,lang)

        translator = Translator(to_lang="Hindi")
        translation = translator.translate(result)
        print(translation)

        translator_2 = Translator(to_lang="Gujarati")
        translation_2 = translator_2.translate(result)
        print(translation_2)

        translator_3 = Translator(to_lang="Spanish")
        translation_3 = translator_3.translate(result)
        print(translation_3)
        print("Exiting " + self.name)


def print_time(threadName, counter, delay):
    while counter:
        if exitFlag:
            return
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1


root = tkinter.Tk()


root.title("Speech Translator")

from PIL import Image, ImageTk

img = Image.open("doctor-sm.png")
photo = ImageTk.PhotoImage(img)
panel = Label(root, image=photo)
panel.image = img
panel.pack()

def recordIt():
    os.system('say ""')
    # global exitFlag
    # exitFlag = 0
    # global thread1
    r = sr.Recognizer()  # define the microphone
    mic = sr.Microphone(device_index=0)  # record your speech
    with mic as source:
        audio = r.listen(source ,timeout=60)  # speech recognition
        print(audio)

    result = r.recognize_google(audio)  # export the result
    with open('my_result.txt', mode='w') as file:
        file.write("Recognized text:")
        file.write("\n")
        file.write(result)
        print("Exporting process completed!")
    print(textwrap.fill(result, 100))

    Display_Text(result)

    if CheckVar1.get()==1:
        lang="Hindi"

    if CheckVar2.get()==1:
        lang="Spanish"

    if CheckVar3.get()==1:
        lang="Gujarati"

    if CheckVar4.get()==1:
        lang="Telugu"

    if CheckVar5.get()==1:
        lang="French"

    if CheckVar6.get()==1:
        lang="Bengali"

    translateIt(result,lang)

def translateIt(result,lang):
    translator = Translator(to_lang=lang)
    translation = translator.translate(result)
    print(translation)
    Display_Converted_Text(translation)

def stopIt():
    root.quit()

top = Frame(root)
bottom = Frame(root)
top.pack(side=TOP)
bottom.pack(side=BOTTOM, fill=BOTH, expand=True)

CheckVar1 = IntVar()
CheckVar2 = IntVar()
CheckVar3 = IntVar()
CheckVar4 = IntVar()
CheckVar5 = IntVar()
CheckVar6 = IntVar()


c = tkinter.Checkbutton(root, text = "Hindi",variable = CheckVar1,onvalue = 1, offvalue=0,anchor= CENTER)
c.pack()

d = tkinter.Checkbutton(root, text = "Spanish", variable = CheckVar2, onvalue = 1, offvalue =0 ,anchor= CENTER)
d.pack()

e = tkinter.Checkbutton(root, text = "Gujarati", variable = CheckVar3, onvalue = 1, offvalue =0,anchor= CENTER)
e.pack()

f = tkinter.Checkbutton(root, text = "Telugu",variable = CheckVar4,onvalue = 1, offvalue=0,anchor= CENTER)
f.pack()

g = tkinter.Checkbutton(root, text = "French", variable = CheckVar5, onvalue = 1, offvalue =0 ,anchor= CENTER)
g.pack()

h = tkinter.Checkbutton(root, text = "Bengali", variable = CheckVar6, onvalue = 1, offvalue =0,anchor= CENTER)
h.pack()

# entry = Entry(root)
# entry.pack()
b = Button(root,  fg = "Red" ,text="Start/Convert", width=30, height=5, command=recordIt)
b.configure(bg="Blue")

c = Button(root, text="Quit", fg = "Red" , width=30, height=5, command=stopIt)

b.pack(in_=top, side=LEFT)
c.pack(in_=top, side=RIGHT)

def Display_Text(data):
    tkinter.Message(bottom, text=data, width=600).pack()

def Display_Converted_Text(data):
    tkinter.Message(bottom, text=data, width=600).pack()




print("A UI Has Opened in another window")
root.mainloop()





