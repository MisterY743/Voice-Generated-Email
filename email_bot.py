import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def get_info():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()     #all the text will be in lower
    except:
        pass

def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('\\senders email\\', 'senders password')   #add senders email and password
    email = EmailMessage()
    email['From'] = 'senders email'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)

email_list = {
    'name1': 'gmail address 1',
    'name2': 'gmail address 2',
    'name3': 'gmail address 3',
}   #this is contact list who will receive the email

def get_email_info():
    talk('To whom you want to send email')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk('What is subject of your email?')
    subject = get_info()
    talk('Tell me the contents of your mail')
    message = get_info()
    send_email(receiver, subject, message)

get_email_info()
