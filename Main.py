###Imports###
import tkinter as tk
from twilio.rest import Client
import speech_recognition as sr
import threading
import os
import time
import geocoder
######

account_sid = 'Account sid as str'
auth_token = 'Auth Token as str'
client = Client(account_sid, auth_token)

def send_sms(): # function to send sms using api
    g = geocoder.ip('me')
    coors = g.latlng

    sms = f'Distress signal recieved by resident from {coors}'
    
    message = client.messages.create(
        from_='Your twilio number',
        body=f'{sms}',
        to='Number of closest contact'
    )
    print(f'Sms code: {message.sid}')
    print('Help request sent...')
    print(f'Copy of sms: {sms}')
    os._exit(0)

def recognise_speech(): #funtion to recognise speech and start gui

    with sr.Microphone() as source:
        print('Listening for cries...')
        x = threading.Thread(target=create_button)
        x.start()
        audio = r.listen(source)
        print('Listening stopped.')
    try:
        text = r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Couldn't recognise pls try again")
        time.sleep(5)
        os._exit(0)
    except sr.RequestError as e:
        text = 'server error'

    return text


def create_button(): #function to greate the gui
    root = tk.Tk()
    root.config(bg="black")
    root.title('Voice or touch activated distrss signal (Prototype 2)')

    canvas = tk.Canvas(root, width=550, height=450, bg="black", highlightthickness=0)

    heading = tk.Label(root, text="VOTADS PROJECT", fg="white", bg="black", font=("Arial", 30))
    heading.place(relx=0.5, rely=0.2, anchor=tk.S)

    sub_text = tk.Label(root, text="Speak into mic...\n OR \n  Press Button To Activate...", fg="white", bg="black", font=("Arial", 20))
    sub_text.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

    button = tk.Button(root, text="  Activating Distress  \nSignal", command=send_sms, bg="red", fg="red", font=("Arial", 20), borderwidth=0)
    button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

    canvas.pack()
    root.mainloop()

r = sr.Recognizer()
speech = recognise_speech()

print(f'"{speech}" detected')

if 'help' in speech: # checking for help in speech
    send_sms()
else:
    print('Program ending...')
    time.sleep(5)
    exit()
